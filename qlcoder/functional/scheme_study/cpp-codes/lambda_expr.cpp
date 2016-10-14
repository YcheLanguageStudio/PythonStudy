#include <functional>
#include <iostream>

using namespace std;

int factorial0(int x) {
  if (x == 0)
    return 1;
  else
    return factorial0(x - 1) * x;
}

// template <typename T> function<int(int)> factorial2(T &func) {
//   function<int(int)> inner = [&func](int x) {
//     if (x == 0)
//       return 1;
//     else
//       return func(func)(x - 1);
//   };
//   return inner;
// }

int main() {
  function<int(int)> factorial1;
  factorial1 = [&factorial1](int x) -> int {
    if (x == 0)
      return 1;
    else
      return factorial1(x - 1) * x;
  };

  cout << factorial0(4) << endl;
  cout << factorial1(factorial1, 4) << endl;
  // cout << factorial2(factorial2)(4) << endl;
}
