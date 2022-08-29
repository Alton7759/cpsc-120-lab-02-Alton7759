![Lint](../../../actions/workflows/part-2.yml/badge.svg)

_Complete `part-1` before starting `part-2`._

# C++ Linting

A linter is a tool that analyzes code without running the code and helps a programmer identify errors or bad practices that can lead to errors. In this exercise, we have a program that 'works' however it does not follow all the rules.

You may say, "well if it works, that's good enough." That is not the standard that we shoot for.

Using a linter will help you spot small mistakes that can become part of a much larger problem later on. For example, there are rules in the [Google C++ coding style](https://google.github.io/styleguide/cppguide.html) about how to name variables. A linter can identify when a variable is not following the rules. Another example is when we forget to use braces or do not indent correctly, the linter can warn us about those problems as well.

The program that you are working on is a program that uses the [Quadratic Formula](https://en.wikipedia.org/wiki/Quadratic_formula) to find the solutions to the equation $4x^2 + 7x - 13 = 0$. The program takes no input and always performs the same calculation. The program is defined in the file named `quadratic_formula.cc`. The formatting of this program is OK. This program has some linter errors that need to be fixed.

A few important conventions or rules that we should follow are:

* [Snake case](https://en.wikipedia.org/wiki/Snake_case) is how we format variable names. For example if we have a variable that we would like to call _degrees Fahrenheit_, then using snake case it would be formatted as `degrees_fahrenheit`, all lower case and each new word separated by an underscore.

* [Camel case](https://en.wikipedia.org/wiki/Camel_case) is how we format constants, function names, and class names. If it's a constant, then we prefix the name with `k`. For example, _speed of light_ is a universal constant. If we created a constant in C++, we would format the name as `kSpeedOfLight`. Camel case is where each word is capitalized. The lowercase `k` means it is a constant.

Spending the time to format and document your programs are well worth it.

Bookmark the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html). Reference it whenever you are not sure how to format your code.

## Compiling

Make sure your program is always compiling correctly. Compile early and compile often.

When you make a small change to a C++ source file, save your work, and compile the program. This will tell you immediately if you have made any mistakes.

_Do not write many, many lines of code and then compile._ This is a bad strategy. You will not catch small mistakes until there are many small mistakes. Correcting a small mistake hidden under many other small mistakes is more difficult than you can imagine.

The compiler we are using is `clang++`. To compile your program, use the following command:
```
$ clang++ quadratic_formula.cc
```

If the program compiles correctly, there will be nothing printed to the screen. Instead a new file will be created named `a.out`.

To run the program, use the following command:
```
$ ./a.out 
There are two solutions for 4x^2 + 7x - 13 = 0.
The first is 1.1289 and the second is -2.8789.
```

The program will execute and print out that 451ºF is 843.8ºC.

If your program does not compile, make sure you undo your changes. _If your program does not compile, then it will receive a 0 grade without being graded._



## Requirements

Improve the code quality by using the special tool named `check_for_lint` to see if the program has any linting errors or warnings. When you identify a linter warning or error, fix the problem in the source code and check again. When the linter does not generate any warnings or errors and the program compiles and runs correctly, then you have a complete and correct program.

For example, to check the formatting, run the command `check_for_lint`. In the following example, we'll assume that `quadratic_formula.cc` is correctly formatted.

```
$ ./check_for_lint 
2022-08-25 23:01:25,212 - INFO - Linting file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc
2022-08-25 23:01:30,832 - INFO - 😀 Linting passed 🥳
2022-08-25 23:01:30,832 - INFO - This is not an auto-grader.
2022-08-25 23:01:30,832 - INFO - Make sure you followed all the instructions and requirements.
```

If we make a change that causes the program to no longer compile, then running `check_for_lint` will show something similar to the following:

```
$ ./check_for_lint 
2022-08-25 23:44:57,228 - INFO - Linting file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc
2022-08-25 23:44:58,904 - INFO - stderr: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:18:1: error: unknown type name 'nt'
nt main(int argc, char const *argv[]) {
^
1 error generated.
2022-08-25 23:44:58,904 - ERROR - /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc is no longer compiling!
2022-08-25 23:44:58,904 - WARNING - A program that does not compile does not get graded.
2022-08-25 23:44:58,904 - WARNING - Use the compiler to see where the program is broken.
2022-08-25 23:44:58,904 - WARNING - You can use git to revert your changes and ask your instructor for help.
```

On the other hand, the file `quadratic_formula.cc` will start out with the following errors.


```
$ ./check_for_lint 
2022-08-25 22:59:10,363 - INFO - Linting file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc
2022-08-25 22:59:16,800 - ERROR - Linter found improvements.
2022-08-25 22:59:16,800 - WARNING - /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:2:1: warning: missing username/bug in TODO [google-readability-todo]
// TODO: don't forget to put your header at the top of every file. And don't forget to remove this comment!
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// TODO(mshafae): don't forget to put your header at the top of every file. And don't forget to remove this comment!
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:19:10: warning: invalid case style for variable 'B' [readability-identifier-naming]
  double B = NAN;
         ^
         b
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:21:10: warning: invalid case style for variable 'DISCRIMINANT' [readability-identifier-naming]
  double DISCRIMINANT = NAN;
         ^~~~~~~~~~~~
         discriminant
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:30:10: warning: invalid case style for variable 'FirstSolution' [readability-identifier-naming]
  double FirstSolution = (-B + sqrt(DISCRIMINANT)) / (2 * a);
         ^~~~~~~~~~~~~
         first_solution
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:34:9: warning: statement should be inside braces [google-readability-braces-around-statements]
  } else
        ^
         {
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:34:9: warning: statement should be inside braces [hicpp-braces-around-statements]
  } else
        ^
         {
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:34:9: warning: statement should be inside braces [readability-braces-around-statements]
  } else
        ^
         {
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:36:3: warning: misleading indentation: statement is indented too deeply [readability-misleading-indentation]
  return 0;
  ^
/home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-2/quadratic_formula.cc:29:3: note: did you mean this line to be inside this 'if'
  if (DISCRIMINANT >= 0 and a != 0.0) {
  ^
2022-08-25 22:59:16,801 - ERROR - 🤯😳😤😫🤬
2022-08-25 22:59:16,802 - ERROR - Use the output from this program to help guide you.
2022-08-25 22:59:16,802 - ERROR - If you get stuck, ask your instructor for help.
2022-08-25 22:59:16,802 - ERROR - Remember, you can find the Google C++ style online at https://google.github.io/styleguide/cppguide.html.
```


## Don't Forget

Please remember that:

- You need to put a [header](https://docs.google.com/document/d/17WkDlxO92zpb26pYM1NIACPcMWtCOlKO7WCrWC6YxRo/edit) in every file.
- You need to follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).
- Remove the `TODO` comments.

## Using Git

Git is a utility that allows you and your instructor to collaborate together on this project. You use the `git` command to clone (copy) your repository to your computer, then to track the changes you make to your files.

Before you can use `git` effectively, it must be configured correctly so you can authenticate with the online service GitHub. Please read, understand, and follow the [instructions posted online](https://docs.google.com/document/d/1eDZTdrzFZadon2Drp6bo-txDhHBi3HXaRjQd7QslZas/edit).

You will be using `git` throughout your computer science education. It is in your best interest to learn how to use it well. Your instructor recommends
[Pro-Git by Scott Chacon](https://git-scm.com/book/en/v2) as an introductory book on `git`. A more advanced student may want to visit [Think Like (a) Git by Sam Livingston-Gray](https://think-like-a-git.net/).

The best way to use `git` is to make many, many commits. Make a small change in your source code, verify that your program still works, and then make a commit. Small commits means that you can track your changes in small steps rather than big leaps. More advance use of `git` will let you roll back your changes to undo mistakes.

It is a good practice to use the command `git status` to check to see if anything needs to be committed before your end your programming session. And at the end of every session it is a very good practice to use `git push` to send your changes to GitHub so your instructor can see them too.

You are encouraged to use `git commit` and `git push` as much as you like. You can do it 10 times, 100 times or 10,000 times. It does not matter. What your instructor will see is the last commit.

As a reminder, here are the key commands that you will need to use to complete this assignment.

* `git clone` This command is used to clone (or copy) your repository from GitHub (or other online service) to your own computer. An example of the command looks like the following:
```
$ git clone https://github.com/mshafae/hello_world.git
Cloning into 'hello_world'...
remote: Enumerating objects: 4, done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 4
Receiving objects: 100% (4/4), done.
```

* `git status` Status will tell you if any files are modified or not. This is useful to determine if you need to `add` or `commit` files to your repository. An example of a repository that has no changes looks like the following:
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```
If there is a file that is changed, then the output of `git status` will identify the name of the file.
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello_world.cc

no changes added to commit (use "git add" and/or "git commit -a")
```
Notice that the output identifies the file `hello_world.cc` as having changes that need to be staged for a commit.

* `git add` When a file has changes that need to be staged for a commit, then the file needs to be _added_. You can use this command with `git status` to see if a file has been successfully staged for a commit.
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   hello_world.cc

no changes added to commit (use "git add" and/or "git commit -a")
$ git add hello_world.c c
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello_world.cc
```
Notice that the first time `git status` is used it shows that `hello_world.cc` has changes that need to be staged for a commit. Then the command `git add hello_world.cc` is used to stage the file. We confirm that `git add` was successful using the `git status` command one more time. We can see that `hello_world.cc` is now staged for a commit.

* `git commit` Committing a file is committing the changes that have been staged using `git add`. It is best to use this command with `git status` to verify that your commit was successful. And commits will not work if you have not [configured your `git` client](https://docs.google.com/document/d/1eDZTdrzFZadon2Drp6bo-txDhHBi3HXaRjQd7QslZas/edit). The best way to use `git commit` is with the `-m` option so you can add your log message right on the command line. If you do not include the log message using the `-m` option, then a text editor will open up prompting you for a log message. _Remember to use the `-m` option and write meaningful log messages._
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   hello_world.cc

$ git commit -m "I made a small change and this is the log message."
[master c6b9a72] I made a small change and this is the log message.
 1 file changed, 2 insertions(+), 2 deletions(-)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

* `git push` Pushing your changes sends all your commits to GitHub so your instructor can see your work. Sometimes people will refer to this as _uploading_ a homework assignment. The better way to think about it is that you are synchronizing the two repositories so your instructor can see all your work. The output below will not be exactly like your output - it will look similar. Checking with `git status` it will show that you have sent all your changes to GitHub.
```
$ git push
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 3.30 KiB | 3.30 MiB/s, done.
Total 8 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
To https://github.com/mshafae/hello_world.git
   b3c33c3..bc64563  main -> main
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
