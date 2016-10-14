#include <iostream>
using namespace std;

class MyDpClass {
private:
  int **arr{nullptr};

  int f(int m, int n) {
    if (arr[m][n] != -1)
      return arr[m][n];

    if (m == 0) {
      arr[m][n] = n + 1;
      return arr[m][n];
    }
    if (n == 0) {
      arr[m][n] = f(m - 1, 1);
      return arr[m][n];
    }
    arr[m][n] = f(m - 1, f(m, n - 1));
    return arr[m][n];
  }

public:
  int result_{-1};

  MyDpClass(int m, int n) {
    arr = new int *[m + 1];
    for (auto i = 0; i < m + 1; i++) {
      arr[i] = new int[n + 1];
      for (auto j = 0; j < n + 1; j++) {
        arr[i][j] = -1;
        cout << "i:" << i << ",j:" << j << ",val:" << arr[i][j] << endl;
      }
    }

    result_ = f(m, n);
    for (auto i = 0; i < m + 1; i++) {
      for (auto j = 0; j < n + 1; j++) {
        cout << "i:" << i << ",j:" << j << ",val:" << arr[i][j] << endl;
      }
    }
  }
};

int main() { cout << MyDpClass(7, 7).result_ << endl; }
