
// TODO: don't forget to put your header at the top of every file. And don't forget to remove this comment!

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
  double a = NAN;
  double B = NAN;
  double c = NAN;
  double DISCRIMINANT = NAN;
  // In 4x^2, a is 4
  a = 4.0;
  // In + 7x, b is 7
  B = 7.0;
  // In - 13, c is -13
  c = -13.0;
  DISCRIMINANT = (B * B) - (4 * a * c);
  if (DISCRIMINANT >= 0 and a != 0.0) {
  double FirstSolution = (-B + sqrt(DISCRIMINANT)) / (2 * a);
  double second_solution = (-B - sqrt(DISCRIMINANT)) / (2 * a);
  cout << "There are two solutions for 4x^2 + 7x - 13 = 0.\n";
  cout << "The first is " << FirstSolution << " and the second is " << second_solution << ".\n";
  } else
  cout << "There are no Real roots for 4x^2 + 7x - 13 = 0\n";
  return 0;
}
