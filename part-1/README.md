![Formatting](../../../actions/workflows/part-1.yml/badge.svg)

# C++ Style & Formatting

[Programming style or coding style](https://en.wikipedia.org/wiki/Programming_style) are a set of conventions or rules that help keep source code consistently organized and formatted. When our C++ source code, also known as code, is well formatted and organized, it is easy to read, understand, and improve our programs.

There are many different C++ styles available. In the C++ community, there is not one, correct style. In other programming language communities, there is a agreement on one widely adopted style.

The style that we have adopted for our course is the [Google C++ coding style](https://google.github.io/styleguide/cppguide.html). The reason we are adopting this style is because Google has published a document that is well organized and well explained to show a learner how to have great programming style.

The following program is a well organized and formatted program. Every line that starts with `//` is what's called a _comment_. A comment is a message written to the programmer, by the programmer, for the programmer. The computer ignores all comments.

In a typical program, we do not have so many comments. You can see the value of the comments. It makes it easy for a beginner to read and understand the program. The formatting makes it clear what steps happen in which order. The indentation shows the hierarchical relationship in the code that some lines are _inside_ of a function. Our text editor uses the formatting and the special meaning of the words to color the text. The colors are not part of the programming language.

```c++
// Tuffy Titan
// CPSC 120-01
// 2050-01-31
// tuffy.titan@csu.fullerton.edu
// @tuffytitan
//
// Lab 01-01
// Partners: @peteranteater, @ivclasers
//
// Add two numbers together.
//

// We read this line as 'pound include I O stream'. The 'I' stands for input.
// The 'O' stands for output. C++ works with input and output as streams of ones
// and zeros. We do not want to spend our time fiddling with bits (ones and
// zeros) so we're going to use some pre-made tools. Technically, this is not C++
// however we use this to help our compiler know how to use code saved in
// libraries. In this case we wish to have some tools to perform some output to
// print text (strings and integers) to the terminal.
#include <iostream>

// This places our program in the standard namespace. In our day-to-day lives,
// people have a first name and a last name. We use our last names to
// distinguish between different people with the same first name. Ideas like
// 'multiply', 'combine', 'minimum', 'sort', and 'maximum' are so commonly use
// we give ideas in a program a first name and a last name. We can imagine `std`
// as the last name for all the ideas in our program.

// As a rule, all your programs in CPSC 120 will have this line.
using namespace std;

// This is a function. The name of the function is AddTwoNumbers. The function
// has two parameters which are integers. The first parameter is left_hand_side
// and the second is right_hand_side. The order of the parameters matter. The
// return type is `int` and it's the first thing on the line. It tells the
// programmer what to expect 'in return' for 'calling' the function
// `AddTwoNumbers`. A call to the function looks like: AddTwoNumbers(5, 6) and
// it would return the integer value 11.
int AddTwoNumbers(int left_hand_side, int right_hand_side) {
  // Between the braces {} is the body of the function. The steps of the
  // function are given between the braces.

  // This is a variable declaration. The first word (or token) is the type. In
  // this case, `int`, which means that the variable will be of integer type.
  // The next word (or token) is the variable name. In this example it is `sum`.
  // The next word (or token) is the assignment operator which looks like the
  // equal sign. This means that we are assigning the value on the right hand
  // side of the `=` to the left hand side. In other words, the integer value of
  // 0 is 'assigned to' the integer variable 'sum'. Notice that reading it from
  // right to left would read "int sum is assigned 0". Reading it from left to
  // right, it would read "0 is assigned to sum which is an integer".
  int sum = 0;
  // The sum variable is assigned the sum of the variables left_hand_side and
  // right_hand_side.
  sum = left_hand_side + right_hand_side;
  // At the end of the function, the work is complete. The value of sum is
  // returned to wherever the function was called.
  return sum;
}

// The main function is the entry point to a program. Entry point means starting
// point. In all of our C++ programs the starting point is always the main
// function. The instructions are performed sequentially. In other words, the
// instructions in the main function are performed by the computer in order, one
// by one.
int main(int argc, char const *argv[]) {
  // This is a variable declaration. The first word (or token) is the type. In
  // this case, `int`, which means that the variable will be of integer type.
  // The next word (or token) is the variable name. In this example it is
  // `my_favorite_number`. Notice that variable names with multiple words have
  // the words separated by underscores (_). We call this snake case. The next
  // word (or token) is the assignment operator which looks like the equal sign.
  // This means that we are assigning the value on the right hand side of the
  // `=` to the left hand side. In other words, the integer value of 2 is
  // 'assigned to' the integer variable 'my_favorite_number'.
  int my_favorite_number = 2;
  // This is a special variable declaration. It is constant. We often say
  // 'const' instead of constant. This means the value of the variable cannot
  // change. It is assigned once and it is always that value. In this example,
  // we have a constant integer variable (`const int`) named kNumHoursInDay.
  // Notice that when we have constant variables we use a different format to
  // make it clear to the programmer that this is special. We start the variable
  // with 'k' for constant and use upper case letters to separate each word. We
  // call this camel case. The integer value 24 is assigned to `kNumHoursInDay`.
  // After this line, `kNumHoursInDay` can never have it's value changed.
  const int kNumHoursInDay = 24;
  // This is a variable declaration. The first word (or token) is the type. In
  // this case, `int`, which means that the variable will be of integer type.
  // The next word (or token) is the variable name. In this example it is `sum`.
  // The next word (or token) is the assignment operator which looks like the
  // equal sign. This means that we are assigning the value on the right hand
  // side of the `=` to the left hand side. In other words, the integer value of
  // 0 is 'assigned to' the integer variable 'sum'.
  int sum = 0;
  // Add my_favorite_number and kNumberHoursInDay together, assign the sum
  // to the variable named sum.
  // In C++, we have addition (+), subtraction (-), multiplication (*), and
  // division (/) as basic mathematical operations.
  sum = my_favorite_number + kNumHoursInDay;
  // This is how we can send text to the terminal so we can see what our program
  // has done. The word (or token) `cout` means 'console output' which is a
  // fancy way to say 'our terminal'. The next word (or token) is `<<` which is
  // the insertion operator. This operator sends what's on it's right hand side
  // to it's left hand side. Another way to think about this is that we're
  // inserting or sending all the text on the right hand side of `cout` to
  // `cout` so we can see it. Magically, the variables are converted to text as
  // well.
  cout << "When you add " << my_favorite_number << " to " << kNumHoursInDay
       << " the sum is " << sum << ".\n";
  // At the end of the main function, the rule is that if everything worked as
  // we expected, we return 0. This is a convention or rule that goes back Unix
  // (1969), Multics (1964), and (probably) CTSS (1961). If the program
  // encountered a problem we return anything other than 0, like 1 or 127.
  return 0;
}
```

On the other hand, the programmer can completely disregard correct C++ programming style, provide no comments, and create a program that runs correctly. The drawback is that the program is very difficult to understand - for people.

The following program is identical in function to the previous program.

```c++
#include <iostream>
using namespace std;int main(int argc,char const *argv[]){int x=2;const int y=24;int z=0;z=x+y;cout<<"When you add "<<x<<" to "<<y<<" the sum is "<<z<<".\n";return 0;}
```

Spending the time to format and document your programs are well worth it.

Bookmark the [Google C++ style guide](https://google.github.io/styleguide/cppguide.html). Reference it whenever you are not sure how to format your code.

A few important conventions or rules that we should follow are:

* The assignment operator is `=`. What's on the right hand side of the `=` is _assigned to_ the left hand side. For example, `x = 5;` means that the value `5` is assigned to the variable `x`.

* [Snake case](https://en.wikipedia.org/wiki/Snake_case) is how we format variable names. For example if we have a variable that we would like to call _degrees Fahrenheit_, then using snake case it would be formatted as `degrees_fahrenheit`, all lower case and each new word separated by an underscore.

* A constant is a special variable that never changes. It is constant. Examples from our day to day life are Pi, the speed of light, and how many minutes are in a day. We use the special word `const` to label a C++ variable as a constant.

* [Camel case](https://en.wikipedia.org/wiki/Camel_case) is how we format constants, function names, and class names. If it's a constant, then we prefix the name with `k`. For example, _speed of light_ is a universal constant. If we created a constant in C++, we would format the name as `kSpeedOfLight`. Camel case is where each word is capitalized. The lowercase `k` means it is a constant.

The program that you are working on is a program that converts a temperature from degrees Fahrenheit to Celsius. The program takes no input and always performs the same conversion. The program is defined in the file named `fahrenheit_to_celsius.cc`. The formatting is incorrect however it compiles and works correctly.

## Compiling

Make sure your program is always compiling correctly. Compile early and compile often.

When you make a small change to a C++ source file, save your work, and compile the program. This will tell you immediately if you have made any mistakes.

_Do not write many, many lines of code and then compile._ This is a bad strategy. You will not catch small mistakes until there are many small mistakes. Correcting a small mistake hidden under many other small mistakes is more difficult than you can imagine.

The compiler we are using is `clang++`. To compile your program, use the following command:
```
$ clang++ fahrenheit_to_celsius.cc
```

If the program compiles correctly, there will be nothing printed to the screen. Instead a new file will be created named `a.out`.

To run the program, use the following command:
```
$ ./a.out 
451 degrees Fahrenheit is 843.8 degrees Celsius.
```

The program will execute and print out that 451ºF is 843.8ºC.

If your program does not compile, make sure you undo your changes. _If your program does not compile, then it will receive a 0 grade without being graded._


## Requirements

Edit the file `fahrenheit_to_celsius.cc` and change the files formatting to conform to Google's C++ style.

To verify that your formatting is conforming to the standards, you have a special tool named `check_formatting` for this assignment. You can use `check_formatting` to check the formatting of `fahrenheit_to_celsius.cc`.

Using the feedback from `check_formatting`, make changes to the source code. Continue to use the compiler and the `check_formatting` tool to check on your progress. Continue editing `fahrenheit_to_celsius.cc` until all warnings and errors have been addressed.

For example, to check the formatting, run the command `check_formatting`. In the following example, we'll assume that `fahrenheit_to_celsius.cc` is correctly formatted.

```
$ ./check_formatting 
2022-08-25 22:29:16,767 - INFO - Checking format for file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-1/fahrenheit_to_celsius.cc
2022-08-25 22:29:17,844 - INFO - 😀 Formatting looks pretty good! 🥳
2022-08-25 22:29:17,844 - INFO - This is not an auto-grader.
2022-08-25 22:29:17,844 - INFO - Make sure you followed all the instructions and requirements.
```

If we make a change that causes the program to no longer compile, then running `check_formatting` will something similar to the following:

```
$ ./check_formatting 
2022-08-25 22:30:43,141 - INFO - Checking format for file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-1/fahrenheit_to_celsius.cc
2022-08-25 22:30:43,959 - INFO - stderr: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-1/fahrenheit_to_celsius.cc:18:1: error: unknown type name 'nt'
nt main(int argc, char const *argv[]) {
^
1 error generated.
2022-08-25 22:30:43,960 - ERROR - /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-1/fahrenheit_to_celsius.cc is no longer compiling!
2022-08-25 22:30:43,960 - WARNING - A program that does not compile does not get graded.
2022-08-25 22:30:43,960 - WARNING - Use the compiler to see where the program is broken.
2022-08-25 22:30:43,960 - WARNING - You can use git to revert your changes and ask your instructor for help.
```

The error may be different yet the result is the same. The `check_formatting` tool will tell you that the program is no longer compiling. Undo the change you just made and try again.

If you are in the wrong directory, the output will look _identical_ to the example below.

```
$ ./check_formatting 
-bash: ./check_formatting: No such file or directory
``` 

This means you are in the wrong directory. Use the `pwd`, `cd`, and `ls` commands to get yourself in the right directory. Ask your instructor for help if you get stuck. If you experience this problem, add a note about the problem and how to solve it to your notebook.

In most cases, when you run `check_formatting` it will tell you that your formatting needs some work and it will show you what is called a [diff](https://en.wikipedia.org/wiki/Diff).

The example below is what `check_formatting` will report with no changes made to the file. Notice that it showing the contents of the input file first and then it is showing some suggested changes.

```
$ ./check_formatting 
2022-08-25 22:31:44,876 - INFO - Checking format for file: /home/mshafae/cpsc120/cpsc-120-lab-02-mshafae/part-1/fahrenheit_to_celsius.cc
2022-08-25 22:31:45,969 - ERROR - Error: Formatting needs improvement.
2022-08-25 22:31:45,969 - WARNING - Contextual Diff
*** Student Submission (Yours)

--- Correct Format

***************

*** 10,50 ****

    // For integer variables assigning them 0 or other integer value is a good
    // practice. For doubles and floats using NAN which means 'not a number' is a
    // good value to use.
! int fahrenheit = 0;double celsius = NAN;fahrenheit = 451;celsius =
  
  
  
! fahrenheit
!               *
  
  
  
  
-                         9.0
- /
- 
- 
- 
- 
-                                                                               5.0 +
- 
- 
- 
- 
- 
- 32.0;cout<<fahrenheit
- 
- 
- 
- 
- 
- << " degrees Fahrenheit is " <<
- celsius
- 
- 
- 
- 
- 
- 
-                                              << " degrees Celsius.\n";return 0;}
- 
--- 10,32 ----

    // For integer variables assigning them 0 or other integer value is a good
    // practice. For doubles and floats using NAN which means 'not a number' is a
    // good value to use.
!   int fahrenheit = 0;
!   double celsius = NAN;
!   fahrenheit = 451;
!   celsius =
  
+       fahrenheit *
  
+           9.0 /
  
!           5.0 +
  
+       32.0;
+   cout << fahrenheit
  
+        << " degrees Fahrenheit is " << celsius
  
+        << " degrees Celsius.\n";
+   return 0;
+ }
  
2022-08-25 22:31:45,969 - ERROR - 🤯😳😤😫🤬
2022-08-25 22:31:45,969 - ERROR - Your formatting doesn't conform to the Google C++ style.
2022-08-25 22:31:45,969 - ERROR - Use the output from this program to help guide you.
2022-08-25 22:31:45,969 - ERROR - If you get stuck, ask your instructor for help.
2022-08-25 22:31:45,969 - ERROR - Remember, you can find the Google C++ style online at https://google.github.io/styleguide/cppguide.html.
```


## Don't Forget

Please remember that:

- You need to put a [header](https://docs.google.com/document/d/17WkDlxO92zpb26pYM1NIACPcMWtCOlKO7WCrWC6YxRo/edit) in every file.
- You need to follow the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html).

## Using Git

Git is a utility that allows you and your instructor to collaborate together on this project. You use the `git` command to clone (copy) your repository to your computer, then to track the changes you make to your files.

Before you can use `git` effectively, it must be configured correctly so you can authenticate with the online service GitHub. Please read, understand, and follow the [instructions posted online](https://docs.google.com/document/d/1eDZTdrzFZadon2Drp6bo-txDhHBi3HXaRjQd7QslZas/edit).

You will be using `git` throughout your computer science education. It is in your best interest to learn how to use it well. Your instructor recomments
[Pro-Git by Scott Chacon](https://git-scm.com/book/en/v2) as an introductory book on `git`. A more advanced student may want to visit [Think Like (a) Git by Sam Livingston-Gray](https://think-like-a-git.net/).

The best way to use `git` is to make many, many commits. Make a small change in your source code, verify that your program still works, and then make a commit. Small commits means that you can track your changes in small steps rather than big leaps. More advance use of `git` will let you roll back your changes to undo mistakes.

It is a good practice to use the command `git status` to check to see if anything needs to be comitted before your end your programming session. And at the end of every session it is a very good practice to use `git push` to send your changes to GitHub so your instructor can see them too.

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