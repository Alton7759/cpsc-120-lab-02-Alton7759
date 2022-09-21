// Christian Bonilla
// CPSC 120-01
// 2022-9-15
// alton77@csu.fullerton.edu
// @alton7759
//
<<<<<<< HEAD
// Lab 2
// Partners: @annavera38
=======
// Lab 02-01
// Partners: @peteranteater
>>>>>>> 627e88394c35b051750191e9ee26513012332a6b
//
// Tthis helpes us get clesius from fahrenheit!
//

#include <cmath>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  // It is a good practice to initialize variables when they are
  // declared. Rewrite the declarations to initialize them to reasonable values.
  // For integer variables assigning them 0 or other integer value is a good
  // practice. For doubles and floats using NAN which means 'not a number' is a
  // good value to use.
  int fahrenheit = 0;
  double celsius = NAN;
  fahrenheit = 451;
  celsius =

      fahrenheit * 9.0 / 5.0 + 32.0;
  cout << fahrenheit << " degrees Fahrenheit is " << celsius
       << " degrees Celsius.\n";
  return 0;
}