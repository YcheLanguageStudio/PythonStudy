#include <cstdlib>
#include <experimental/random>
#include <iostream>
#include <random>
using namespace std;

int main() {
  constexpr int LIMIT = 10000000;
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> dis(1, 10000000);
  for (int i = 0; i < 10; i++) {
    int rand_num = dis(gen);
    cout << rand_num << endl;
    int x = std::experimental::randint(0, 100);
    cout << x << endl
  }
}
