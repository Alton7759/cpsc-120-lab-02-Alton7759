// Christian Bonilla
// CPSC 120-01
// 2022-9-15
// alton77@csu.fullerton.edu
// @alton7759
//
// Lab 02-02
// Partners: @peteranteater
//
// this will do the quadratic formula for us!
//

#include <cmath>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  // Here's a quadratic equation:
  //     4x^2 + 7x - 13 = 0
  // Let's solve it using the Quadratic Formula https://en.wikipedia.org/wiki/Quadratic_formula
  // It is a good practice to initialize variables when they are
  // declared. Rewrite the declarations to initialize them to reasonable values.
  // For integer variables assigning them 0 or other integer value is a good
  // practice. For doubles and floats using NAN which means 'not a number' is a
  // good value to use.
  double aaa = NAN;
  double bbb = NAN;
  double ccc = NAN;
  double discriminant = NAN;
  // In 4x^2, a is 4
  aaa = 4.0;
  // In + 7x, b is 7
  bbb = 7.0;
  // In - 13, c is -13
  ccc = -13.0;
  discriminant = (bbb * bbb) - (4 * aaa * ccc);
  if (discriminant >= 0 and aaa != 0.0) {
  double firstsolution = (-bbb + sqrt(discriminant)) / (2 * aaa);
  double second_solution = (-bbb - sqrt(discriminant)) / (2 * aaa);
  cout << "There are two solutions for 4x^2 + 7x - 13 = 0.\n";
  cout << "The first is " << firstsolution << " and the second is " << second_solution << ".\n";
  } else {
  cout << "There are no Real roots for 4x^2 + 7x - 13 = 0\n";
  return 0;}
  
}
