#
# Copyright 2021 Michael Shafae
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
""" Utilities used to manipulate source code files from student
    assignments. """
import glob
import subprocess
import difflib
import os.path
import logging
import re
from datetime import datetime
import sys
import black
from mkcompiledb import create_clang_compile_commands_db
from logger import setup_logger
from parse_header import dict_header
from header_check import header_check


def remove_python_comments(file):
    """Removing comments from Python code. Inspiration from
    https://stackoverflow.com/questions/59270042/efficent-way-to-remove-docstring-with-regex
    see Alexandr Shurigin's answer"""
    import ast
    import astor

    no_comments = None

    try:
        with open(file) as file_handle:
            contents = file_handle.read()
    except FileNotFoundError as exception:
        logging.error('Cannot remove comments. No such file. %s', file)

    parsed = ast.parse(contents)

    for node in ast.walk(parsed):
        # let's work only on functions & classes definitions
        if not isinstance(
            node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)
        ):
            continue
        if not len(node.body):
            continue
        if not isinstance(node.body[0], ast.Expr):
            continue
        if not hasattr(node.body[0], 'value') or not isinstance(
            node.body[0].value, ast.Str
        ):
            continue
        # Uncomment lines below if you want print what and where we are removing
        # print(node)
        # print(node.body[0].value.s)
        node.body = node.body[1:]

    # print('***** Processed source code output ******\n=========================================')
    # print(astor.to_source(parsed))
    no_comments = astor.to_source(parsed)
    return no_comments


def remove_cpp_comments(file):
    """Remove CPP comments from a file using the CPP preprocessor"""
    # Inspired by
    # https://stackoverflow.com/questions/13061785/remove-multi-line-comments
    # and
    # https://stackoverflow.com/questions/35700193/how-to-find-a-search-term-in-source-code/35708616#35708616
    no_comments = None
    cmd = 'clang++ -E -P -'
    try:
        with open(file) as file_handle:
            # replace 'a', '__' and '#' to avoid preprocessor handling
            filtered_contents = (
                file_handle.read()
                .replace('a', 'aA')
                .replace('__', 'aB')
                .replace('#', 'aC')
            )
        proc = subprocess.run(
            [cmd],
            capture_output=True,
            shell=True,
            timeout=10,
            check=False,
            text=True,
            input=filtered_contents,
        )
        if proc.returncode == 0:
            no_comments = (
                proc.stdout.replace('aC', '#')
                .replace('aB', '__')
                .replace('aA', 'a')
            )
        else:
            logging.error('Errors encountered removing comments.')
            logging.error('stderr {}'.format(str(proc.stderr).rstrip("\n\r")))
    except FileNotFoundError as exception:
        logging.error('Cannot remove comments. No such file. %s', file)
    return no_comments


def makefile_has_compilecmd(target_makefile):
    """Given a Makefile, see if it has the compilecmd target which prints
    the compilation command to stdout."""
    has_compilecmd = False

    try:
        with open(target_makefile) as file_handle:
            has_compilecmd = file_handle.read().find('compilecmd:') != -1
    except FileNotFoundError as exception:
        logging.error('Cannot open Makefile "%s" for reading.', target_makefile)
    return has_compilecmd


def makefile_get_compilecmd(target_dir, compiler='clang++'):
    """Given a Makefile with the compilecmd target, return the string
    which represents the compile command. For use with making the
    compile database for linting."""
    logger = setup_logger()
    compilecmd = None
    makefiles = glob.glob(
        os.path.join(target_dir, '*Makefile'), recursive=False
    )
    # Break on the first matched Makefile with compilecmd
    matches = None
    for makefile in makefiles:
        if makefile_has_compilecmd(makefile):
            cmd = 'make -C {} compilecmd'.format(target_dir)
            proc = subprocess.run(
                [cmd],
                capture_output=True,
                shell=True,
                timeout=10,
                check=False,
                text=True,
            )
            matches = [
                line
                for line in str(proc.stdout).split('\n')
                if line.startswith(compiler)
            ]
            break
    if matches:
        compilecmd = matches[0]
    else:
        logger.debug('Could not identify compile command; using default.')
    return compilecmd

def strip_and_compare_files(base_file, submission_file):
    """ Compare two source files with a contextual diff, return \
    result as a list of lines. """
    base_file_contents_no_comments = remove_cpp_comments(base_file)
    contents_no_comments = remove_cpp_comments(submission_file)
    diff = ""
    if contents_no_comments and base_file_contents_no_comments:
        base_file_contents_no_comments = base_file_contents_no_comments.split(
            '\n'
        )
        contents_no_comments = contents_no_comments.split('\n')
        diff = difflib.context_diff(
            base_file_contents_no_comments,
            contents_no_comments,
            'Base',
            'Submission',
            n=3,
        )
    else:
        logging.error('Cannot perform contextual diff.')
    return list(diff)


def format_check(file):
    """ Use clang-format to check file's format against the \
    Google C++ style. """
    # logger = setup_logger()
    # clang-format
    cmd = 'clang-format'
    cmd_options = '-style=Google --Werror'
    cmd = cmd + ' ' + cmd_options + ' ' + file
    # logger.debug('clang format: %s', cmd)
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=10,
        check=False,
        text=True,
    )
    correct_format = str(proc.stdout).split('\n')
    with open(file) as file_handle:
        original_format = file_handle.read().split('\n')
    diff = difflib.context_diff(
        original_format,
        correct_format,
        'Student Submission (Yours)',
        'Correct Format',
        n=3,
    )
    # print('\n'.join(list(diff)))
    return list(diff)


def lint_check(file, tidy_options=None, skip_compile_cmd=False):
    """ Use clang-tidy to lint the file. Options for clang-tidy \
    defined in the function. """
    logger = setup_logger()
    # clang-tidy
    if not skip_compile_cmd:
        compilecmd = makefile_get_compilecmd(
            os.path.dirname(os.path.realpath(file))
        )
    if not skip_compile_cmd and compilecmd:
        logger.debug('Using compile command %s', compilecmd)
        create_clang_compile_commands_db(
            remove_existing_db=True, compile_cmd=compilecmd
        )
    elif not skip_compile_cmd and not compilecmd:
        logger.debug('Creating compile commands.')
        create_clang_compile_commands_db(files=[file], remove_existing_db=True)
    cmd = 'clang-tidy'
    if not tidy_options:
        logger.debug('Using default tidy options.')
        cmd_options = r'-checks="-*,google-*, modernize-*, \
        readability-*,cppcoreguidelines-*,\
        -google-build-using-namespace,\
        -google-readability-todo,\
        -modernize-use-trailing-return-type,\
        -cppcoreguidelines-avoid-magic-numbers,\
        -readability-magic-numbers,\
        -cppcoreguidelines-pro-type-union-access,\
        -cppcoreguidelines-pro-bounds-constant-array-index"'
        # cmd_options = '-checks="*"'
    else:
        cmd_options = tidy_options
    cmd = cmd + ' ' + cmd_options + ' ' + file
    if skip_compile_cmd:
        cmd = cmd + ' -- -std=c++17'
    logger.debug('Tidy command %s', cmd)
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=60,
        check=False,
        text=True,
    )
    linter_warnings = str(proc.stdout).split('\n')
    linter_warnings = [line for line in linter_warnings if line != '']
    return linter_warnings


def pylint_check(file, epsilon=1.0):
    """Use pylint to lint the input file."""
    from pylint import epylint as lint

    linting_passed = False
    linter_warnings = []
    if os.stat(file).st_size == 0:
        logging.warning('File %s is empty.', file)
    else:
        (pylint_stdout, pylint_stderr) = lint.py_run(
            file + ' -d no-member', return_std=True
        )
        stdout = '\n'.join(pylint_stdout.readlines())
        stderr = '\n'.join(pylint_stderr.readlines())
        # print(s)
        pattern = r"been rated at (-?\d?\d?\d?\d.\d\d)/10"
        search_results = re.search(pattern, stdout)
        if search_results:
            match = search_results.group(1)
            # print('\t{}: {}'.format(file, match))
        else:
            logging.error('%s: no match\n%s\n%s', file, stdout, stderr)
            match = '-999'
        pylint_best_score = 10.0
        score = float(match)
        if pylint_best_score - epsilon > score:
            logging.error(
                '%s does not pass linting. %.2f/%.2f',
                file,
                score,
                pylint_best_score,
            )
        else:
            logging.info(
                '%s passes linting. %.2f/%.2f', file, score, pylint_best_score
            )
            linting_passed = True
        linter_warnings = stdout.split('\n')
        linter_warnings = [
            line for line in linter_warnings if line != '' and line != ' '
        ]
    return (linting_passed, linter_warnings)


def pyformat_file_in_place(
    src: black.Path,
    fast: bool,
    mode: black.Mode,
    write_back: black.WriteBack = black.WriteBack.NO,
    lock: black.Any = None,  # multiprocessing.Manager().Lock() is some crazy proxy
) -> (bool, str):
    """This was taken from black so that the diff is captured to a string rather than sent directly to stdout. Format file under `src` path. Return True if changed.
    If `write_back` is DIFF, write a diff to stdout. If it is YES, write reformatted
    code to the file.
    `mode` and `fast` options are passed to :func:`format_file_contents`.
    """
    then = datetime.utcfromtimestamp(src.stat().st_mtime)
    with open(src, "rb") as buf:
        src_contents, encoding, newline = black.decode_bytes(buf.read())
    try:
        dst_contents = black.format_file_contents(
            src_contents, fast=fast, mode=mode
        )

    except black.NothingChanged:
        return (False, '')
    except black.JSONDecodeError:
        raise ValueError(
            f"File '{src}' cannot be parsed as valid Jupyter notebook."
        ) from None

    if write_back == black.WriteBack.YES:
        with open(src, "w", encoding=encoding, newline=newline) as f:
            f.write(dst_contents)
    elif write_back in (black.WriteBack.DIFF, black.WriteBack.COLOR_DIFF):
        now = datetime.utcnow()
        src_name = f"{src}\t{then} +0000"
        dst_name = f"{src}\t{now} +0000"
        diff_contents = black.diff(
            src_contents, dst_contents, src_name, dst_name
        )

        if write_back == black.WriteBack.COLOR_DIFF:
            diff_contents = black.color_diff(diff_contents)

        # print(diff_contents)
        # with lock or black.nullcontext():
        #    f = io.TextIOWrapper(
        #        sys.stdout.buffer,
        #        encoding=encoding,
        #        newline=newline,
        #        write_through=True,
        #    )
        #    f = black.wrap_stream_for_windows(f)
        #    f.write(diff_contents)
        #    f.detach()
    return (True, diff_contents)


def pyformat_check(file):
    """Use black to check the style of the input file."""
    diff_contents = None
    # black.freeze_support()
    # black.patch_click()
    # black.main()
    check = True
    diff = True
    color = False
    verbose = False
    line_length = 80
    fast = False
    write_back = False
    quiet = True
    write_back = black.WriteBack.from_configuration(
        check=check, diff=diff, color=color
    )
    versions = set()
    mode = black.Mode(
        target_versions=versions,
        line_length=line_length,
        is_pyi=False,
        is_ipynb=False,
        string_normalization=False,
        magic_trailing_comma=False,
        experimental_string_processing=False,
    )
    report = black.Report(check=check, diff=diff, quiet=quiet, verbose=verbose)
    sources = [black.Path(file)]
    # You can process multiple files very fast, a single file is all we need.
    if len(sources) == 1:
        # black.reformat_one(
        #    src=sources.pop(),
        #    fast=fast,
        #    write_back=write_back,
        #    mode=mode,
        #    report=report,
        # )
        src = sources.pop()
        try:
            changed = black.Changed.NO
            cache: Cache = {}
            if write_back not in (
                black.WriteBack.DIFF,
                black.WriteBack.COLOR_DIFF,
            ):
                cache = black.read_cache(mode)
                res_src = src.resolve()
                res_src_s = str(res_src)
                if res_src_s in cache and cache[
                    res_src_s
                ] == black.get_cache_info(res_src):
                    changed = black.Changed.CACHED
            if changed is not black.Changed.CACHED:
                (status, diff_contents) = pyformat_file_in_place(
                    src, fast=fast, write_back=write_back, mode=mode
                )
                if status:
                    changed = black.Changed.YES
            if (
                write_back is black.WriteBack.YES
                and changed is not black.Changed.CACHED
            ) or (
                write_back is black.WriteBack.CHECK
                and changed is black.Changed.NO
            ):
                black.write_cache(cache, [src], mode)
            report.done(src, changed)
        except Exception as exc:
            if report.verbose:
                black.traceback.print_exc()
            report.failed(src, str(exc))

    else:
        workers = 2
        black.reformat_many(
            sources=sources,
            fast=fast,
            write_back=write_back,
            mode=mode,
            report=report,
            workers=workers,
        )

    # print(diff_contents)
    # print(report.__dict__)
    # Pycodestyle
    # see https://pycodestyle.pycqa.org/en/latest/advanced.html
    # class TestCodeFormat(unittest.TestCase):
    #
    #    def test_conformance(self):
    #        """Test that we conform to PEP-8."""
    #        style = pycodestyle.StyleGuide(quiet=True)
    #        result = style.check_files(['file1.py', 'file2.py'])
    #        self.assertEqual(result.total_errors, 0,
    #                         "Found code style errors (and warnings).")
    # or
    # fchecker = pycodestyle.Checker('testsuite/E27.py', show_source=True)
    # file_errors = fchecker.check_all()
    if diff_contents:
        diff_contents = diff_contents.split('\n')
    return diff_contents


def glob_py_src_files(target_dir='.'):
    """Recurse through the target_dir and find all the .py files."""
    return glob.glob(os.path.join(target_dir, '**/*.py'), recursive=True)


def glob_cc_src_files(target_dir='.'):
    """Recurse through the target_dir and find all the .cc files."""
    return glob.glob(os.path.join(target_dir, '**/*.cc'), recursive=True)


def glob_h_src_files(target_dir='.'):
    """Recurse through the target_dir and find all the .h files."""
    return glob.glob(os.path.join(target_dir, '**/*.h'), recursive=True)


def glob_all_src_files(target_dir='.'):
    """Recurse through the target_dir and find all the .cc and .h files."""
    files = glob_cc_src_files(target_dir) + glob_h_src_files(target_dir)
    return files


def make_spotless(target_dir):
    """Given a directory that contains a GNU Makefile, clean with the `make
    spotless` target."""
    status = True
    status = make(target_dir, 'spotless')
    return status


def make_build(target_dir, always_clean=True):
    """Given a directory that contains a GNU Makefile, build with `make all`.
    This function call will call `make spotless` via make_spotless()"""
    status = True
    if always_clean:
        status = make_spotless(target_dir)
    if status:
        status = make(target_dir, 'all')
    return status


def make(target_dir, make_target):
    """Given a directory, execute make_target given the GNU Makefile in the
    directory."""
    status = True
    if not os.path.exists(os.path.join(target_dir, 'Makefile')):
        logging.error('Makefile does not exist in %s', target_dir)
        status = False
    else:
        cmd = 'make -C {} {}'.format(target_dir, make_target)
        logging.debug(cmd)
        proc = subprocess.run(
            [cmd],
            capture_output=True,
            shell=True,
            timeout=15,
            check=False,
            text=True,
        )
        # if proc.stdout:
        #    logging.info('stdout: %s', str(proc.stdout).rstrip("\n\r"))
        if proc.stderr:
            logging.info('stderr: %s', str(proc.stderr).rstrip("\n\r"))
        if proc.returncode != 0:
            status = False
    return status


def build(file, target='asgt', compiletimeout=10):
    """Given a C++ source file, build with clang C++14 with -Wall
    and -pedantic. Output is 'asgt'. Binary is left on the file system."""
    logger = setup_logger()
    # rm the file if exists
    if os.path.exists(target):
        os.unlink(target)
    status = True
    cmd = 'clang++ -Wall -pedantic -std=c++14 -o {} {}'.format(target, file)
    logger.debug(cmd)
    proc = subprocess.run(
        [cmd],
        capture_output=True,
        shell=True,
        timeout=compiletimeout,
        check=False,
        text=True,
    )
    if proc.stdout:
        logger.info('stdout: %s', str(proc.stdout).rstrip("\n\r"))
    if proc.stderr:
        logger.info('stderr: %s', str(proc.stderr).rstrip("\n\r"))
    if proc.returncode != 0:
        status = False
    return status


def identify(header):
    """String to identify submission's owner."""
    ident = '(Malformed Header)'
    if header:
        ident = 'Grading {} {} {}'.format(
            header.get('name'), header.get('email'), header.get('github')
        )
    return ident


def has_pymain_condition(file):
    """Check if the given file has the __name__ == __main__"""
    print('has_pymain_condition not implemented.')
    exit(1)


def has_main_function(file):
    """Check if a given file has a C++ main function."""
    status = False
    main_regex = re.compile(
        r'int\s*main\s*\(int\s*argc,\s*(const)?\s*char\s*(const)?\s*\*\s*argv\[\]\)'
    )
    with open(file, 'r') as file_handle:
        src_code = file_handle.read()
        matches = main_regex.search(src_code)
        if matches:
            status = True
    return status


def solution_check_simple(run=None, files=None, do_format_check=True, do_lint_check=True, tidy_options=None, skip_compile_cmd=False):
    """Main function for checking student's solution. Provide a pointer to a
    run function."""
    logger = setup_logger()
    if len(sys.argv) < 3:
        logger.error(
            'provide target directory, program name, and optionally a base directory to run a diff'
        )
        sys.exit(1)
    target_directory = sys.argv[1]
    if len(sys.argv) == 4:
        base_directory = sys.argv[3]
    else:
        base_directory = None
    if not files:
        files = glob_all_src_files(target_directory)
    else:
        files = [os.path.join(sys.argv[1], file) for file in files]
    if len(files) == 0:
        logger.error("❌ No files in %s.", target_directory)
        sys.exit(1)

    # Header checks
    files_missing_header = [file for file in files if not header_check(file)]
    files_with_header = [file for file in files if header_check(file)]
    header = None
    if len(files_with_header) == 0:
        logger.error('❌ No header provided in any file in %s. Exiting.', target_directory)
        logger.error('All files: %s', ' '.join(files))
        sys.exit(1)
    else:
        with open(files_with_header[0]) as file_handle:
            contents = file_handle.read()
        header = dict_header(contents)
    
    logger.info('Start %s', identify(header))
    logger.info('All files: %s', ' '.join(files))
    if len(files_missing_header) != 0:
        logger.warning(
            'Files missing headers: %s', ' '.join(files_missing_header)
        )

    # Check if files have changed
    if base_directory:
        count = 0
        for file in files:
            diff = compare_files(file, os.path.join(base_directory, file))
            if len(diff) == 0:
                count += 1
                logger.error('No changes made to the file %s.', file)
        if count == len(files):
            logger.error('No changes made to any files.')
            sys.exit(1)
    else:
        logger.debug('Skipping base file comparison.')

    # Format
    if do_format_check:
        for file in files:
            diff = format_check(file)
            if len(diff) != 0:
                logger.warning('❌ Formatting needs improvement in %s.', file)
                logger.info(
                    'Please make sure your code conforms to the Google C++ style.'
                )
                logger.debug('\n'.join(diff))
            else:
                logger.info('✅ Formatting passed on %s', file)

    # Lint
    if do_lint_check:
        for file in files:
            lint_warnings = lint_check(file, tidy_options, skip_compile_cmd)
            if len(lint_warnings) != 0:
                logger.warning('❌ Linter found improvements in %s.', file)
                logger.debug('\n'.join(lint_warnings))
            else:
                logger.info('✅ Linting passed in %s', file)


    status = 0
    # check to see if all the files end with .cc, if not, then we have to
    # find the file with the main function.
    if sum([True for file in files if file.endswith('.cc')]):
        cc_files = files
    else:
        cc_files = glob_cc_src_files(target_directory)
    # Clean, Build, & Run
    if len(cc_files) > 1:
        logger.info(
            'Found more than one C++ source file: %s', ' '.join(cc_files)
        )
    main_src_file = None
    for file in files:
        if has_main_function(file):
            if not main_src_file:
                main_src_file = file
                logger.info('Main function found in %s', file)
            else:
                logger.warning('Extra main function found in %s', file)
    if main_src_file:
        logger.info('Checking build for %s', main_src_file)
        if build(main_src_file):
            logger.info('✅ Build passed')
            # Run
            if not run:
                logger.info('No run function specified...skipping.')
            elif run and run('./' + sys.argv[2]):
                logger.info('✅ Run passed')
            else:
                logger.error('❌ Run failed')
                status = 1
        else:
            logger.error('❌ Build failed')
            status = 1
    else:
        logger.error('❌ No main function found in files: %s', ' '.join(cc_files))
        status = 1
    logger.info('End %s', identify(header))
    sys.exit(status)


def solution_check_make(run=None):
    """Main function for checking student's solution. Provide a pointer to a
    run function."""
    logger = setup_logger()
    if len(sys.argv) < 3:
        logging.error(
            'provide target directory, program name, and optionally a base directory'
        )
        sys.exit(1)
    target_directory = sys.argv[1]
    if len(sys.argv) == 4:
        base_directory = sys.argv[3]
    else:
        base_directory = None
    files = glob_all_src_files(target_directory)
    if len(files) == 0:
        logger.error("No files in %s.", target_directory)
    with open(files[0]) as file_handle:
        contents = file_handle.read()
    header = dict_header(contents)
    logger.info('Start %s', identify(header))
    logger.info('All files: %s', ' '.join(files))
    files_missing_header = [file for file in files if not header_check(file)]
    if len(files_missing_header) != 0:
        logger.warning(
            'Files missing headers: %s', ' '.join(files_missing_header)
        )

    # Check if files have changed
    if base_directory:
        count = 0
        for file in files:
            diff = compare_files(file, os.path.join(base_directory, file))
            if len(diff) == 0:
                count += 1
                logger.error('No changes made in file %s.', file)
        if count == len(files):
            logger.error('No changes made ANY file. Stopping.')
            sys.exit(1)
    else:
        logger.debug('Skipping base file comparison.')

    # Format
    for file in files:
        diff = format_check(file)
        if len(diff) != 0:
            logger.warning("Formatting needs improvement in %s.", file)
            # logging.warning('\n'.join(diff))
        else:
            logger.info('Formatting passed on %s', file)

    # Lint
    for file in files:
        lint_warnings = lint_check(os.path.join(target_directory, file))
        if len(lint_warnings) != 0:
            logger.warning('Linter found improvements in %s.', file)
            # logger.warning('\n'.join(lint_warnings))
        else:
            logger.info('XLinting passed in %s', file)

    status = 0
    # Clean, Build, & Run
    if make_build(target_directory):
        logger.info('Build passed')
        # Run
        if run(os.path.join(target_directory, sys.argv[2])):
            logger.info('Run passed')
        else:
            logger.error('Run failed')
            status = 1
    else:
        logger.error('Build failed')
        status = 1
    logger.info('End %s', identify(header))
    sys.exit(status)
