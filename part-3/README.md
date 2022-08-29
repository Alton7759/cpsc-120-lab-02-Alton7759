![Formatting and Linting](../../../actions/workflows/part-3.yml/badge.svg)

_Complete `part-2` before starting `part-3`._

# Putting It Together

We had an exercise focusing on formatting and the next exercise was focused on linting. In this exercise, we have a program that compiles and works, yet is not formatted correctly and it may have some lint that needs to be removed.

In this exercise, you are provided a file named `hello.cc`. Let us start by compiling the program and running the resulting executable binary file. Use the compiler `clang++` to translate the C++ source code in `hello.cc` to a binary file, which is named `a.out` by default. We can execute the resulting binary file using the command `./a.out`. Below is an example of how this can be done.

```
$ clang++ prompt_hello.cc 
$ ls
README.md       check_lint_and_format
a.out           hello.cc
$ ./a.out 
Hello World!
```

Open `hello.cc` in your text editor and you will find a very sloppy C++ program. We can see that compiling and running the program 'works' yet the program is not following the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).

```c++
// TODO: Add a header and remove this comment.
#include <iostream>
// TODO: clean up the programs formatting and address anything the linter identifies.
using namespace std;int main(int argc,char const*argv[]){cout<<"Hello World!\n";return 0;}
```

Using the special tool `check_lint_and_format` to see what problems your tool can detect. (Remember an automatic tool is no replacement for your intellect and your sharp eyes.) You can run the tool using the command  `./check_lint_and_format`. If you look at the example output below, you will see that it first checks to see if the formatting is OK. If the formatting is OK it will then lint the file. If the formatting is not OK, linting is skipped.

```
$ ./check_lint_and_format 
2022-08-26 11:23:17,149 - INFO - Processing file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-3/hello.cc
2022-08-26 11:23:18,762 - ERROR - Error: Formatting needs improvement.
2022-08-26 11:23:18,763 - WARNING - Linting skipped.
2022-08-26 11:23:18,763 - WARNING - Contextual Diff
*** Student Submission (Yours)

--- Correct Format

***************

*** 1,4 ****

  // TODO: Add a header and remove this comment.
  #include <iostream>
! // TODO: clean up the programs formatting and address anything the linter identifies.
! using namespace std;int main(int argc,char const*argv[]){cout<<"Hello World!\n";return 0;}
--- 1,9 ----

  // TODO: Add a header and remove this comment.
  #include <iostream>
! // TODO: clean up the programs formatting and address anything the linter
! // identifies.
! using namespace std;
! int main(int argc, char const* argv[]) {
!   cout << "Hello World!\n";
!   return 0;
! }
2022-08-26 11:23:18,763 - ERROR - 🤯😳😤😫🤬
2022-08-26 11:23:18,763 - ERROR - Your formatting doesn't conform to the Google C++ style.
2022-08-26 11:23:18,763 - ERROR - Use the output from this program to help guide you.
2022-08-26 11:23:18,763 - ERROR - If you get stuck, ask your instructor for help.
2022-08-26 11:23:18,763 - ERROR - Remember, you can find the Google C++ style online at https://google.github.io/styleguide/cppguide.html.
```

## Requirements

Using the tool `check_lint_and_format`, determine what you need to change in `hello.cc` to conform to the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).

Start by correcting the formatting and spacing until it passes the formatting test.

Next, check for any lint in the program and addresses those problems.


## Don't Forget

Please remember that:

- You need to put a header in every file.
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
