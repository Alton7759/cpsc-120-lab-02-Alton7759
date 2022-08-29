#!/usr/bin/env python3
#
# Copyright 2021-2022 Michael Shafae
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
""" Check student's submission; requires the main file and the
    template file from the original repository. """
# pexpect documentation
#  https://pexpect.readthedocs.io/en/stable/index.html

# ex.
# .action/solution_check_p1.py  part-1 asgt


import logging
import pexpect
import sys
from srcutilities import solution_check_simple


def run_p1(binary):
    """Run part-1"""
    status = True
    values = ('No parameters',)
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p1(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p1(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))
    try:
        proc.expect(
            r'(?i)\s*451\s+degrees\s+Fahrenheit\s+is\s+843.8[0-9]*\s+degrees\s+Celsius.'
        )
        # proc.expect(
        #     r'(?i)\s*The\s+distance\s+from\s+CSUF\s+to\s+Sacremento\s+is\s+614.1[0-9]*\s+kilometers\s+or\s+383.8[0-9]* miles.'
        # )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    # proc.sendline(values[0])

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


def run_p2(binary):
    """Run part-2"""
    status = True
    values = ('No parameters',)
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p2(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p2(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))
    try:
        # proc.expect(
        #     r'(?i)\s*451\s+degrees\s+Fahrenheit\s+is\s+843.8[0-9]*\s+degrees\s+Celsius.'
        # )
        proc.expect(
            r'(?i)\s*There\s+are\s+two\s+solutions\s+for\s+4x\^2\s+\+\s+7x\s+-\s+13\s+=\s+0.\s+The\s+first\s+is\s+1.1[0-9]*\s+and\s+the\s+second\s+is\s+-2.8[0-9]*\.\s+'
        )
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    # proc.sendline(values[0])

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


def run_p3(binary):
    """Run part-3"""
    status = True
    values = ('No parameters',)
    for index, val in enumerate(values):
        logging.info('Test %d - %s', index + 1, val)
        status = status and _run_p3(binary, val)
        if not status:
            logging.error("Did not receive expected response. Halting test.")
            break
    return status


def _run_p3(binary, values):
    """The actual test with the expected input and output"""
    status = False
    proc = pexpect.spawn(binary, timeout=1)
    # proc.logfile = sys.stdout.buffer
    values = list(map(str, values))
    try:
        proc.expect(r'(?i)\s*Hello\s+World!')
    except (pexpect.exceptions.TIMEOUT, pexpect.exceptions.EOF) as exception:
        logging.error('Could not find expected output.')
        logging.debug("%s", str(exception))
        logging.debug(str(proc))
        return status

    # proc.sendline(values[0])

    proc.expect(pexpect.EOF)
    proc.close()
    if proc.exitstatus == 0:
        status = True
    return status


if __name__ == '__main__':
    tidy_opts = (
        '-checks="*,-misc-unused-parameters,'
        '-modernize-use-trailing-return-type,-google-build-using-namespace,'
        '-cppcoreguidelines-avoid-magic-numbers,-readability-magic-numbers"'
        ' -config="{CheckOptions: [ {key: readability-identifier-naming.VariableCase, value: lower_case},'
        ' { key: readability-identifier-naming.FunctionCase, value: CamelCase }, '
        '{key: readability-identifier-naming.GlobalConstantCase,  value: UPPER_CASE}, '
        '{key: readability-identifier-naming.GlobalConstantPrefix, value: k} ]}"'
    )
    if sys.argv[1] == 'part-1':
        solution_check_simple(
            run=run_p1, files=['celius_to_fahrenheit.cc'], do_lint_check=False
        )
    elif sys.argv[1] == 'part-2':
        solution_check_simple(
            run=run_p2,
            files=['quadratic_formula.cc'],
            do_format_check=False,
            tidy_options=tidy_opts,
            skip_compile_cmd=True,
        )
    elif sys.argv[1] == 'part-3':
        solution_check_simple(
            run=run_p3,
            files=['hello.cc'],
            tidy_options=tidy_opts,
            skip_compile_cmd=True,
        )
    else:
        print('Error: no match.')
