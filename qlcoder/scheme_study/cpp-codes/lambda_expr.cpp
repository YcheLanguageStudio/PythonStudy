#include <functional>
#include <iostream>

using namespace std;

// normal impl
int factorial0(int x) {
  if (x == 0)
    return 1;
  else
    return factorial0(x - 1) * x;
}

template <typename T> int factorial2(function<T> func) {
  auto inner = [&func](int x) {
    if (x == 0)
      return 1;
    else
      return func(func)(x - 1);
  };
}

int main() {
  // bind function obj as the first argument
  function<int(int)> factorial1 = [&factorial1](int x) -> int {
    if (x == 0)
      return 1;
    else
      return factorial1(x - 1) * x;
  };

  cout << factorial0(4) << endl;
  cout << factorial1(4) << endl;
  cout << factorial2(factorial2)(4) << endl;
}
