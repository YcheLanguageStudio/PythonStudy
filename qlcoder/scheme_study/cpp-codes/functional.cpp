#include <iostream>
using namespace std;

template <int T> int find_number() {
  constexpr int ARRAY_SIZE = T;
  cout << ARRAY_SIZE << endl;

  auto array = new int[ARRAY_SIZE];
  for (auto i = 0; i < ARRAY_SIZE; i++) {
    array[i] = i;
  }

  constexpr int MARK_DONE = -1;
  for (auto start = 0, remain_size = ARRAY_SIZE; remain_size > 1;
       --remain_size) {
    do {
      start = (start + 1) % ARRAY_SIZE;
    } while (array[start] == MARK_DONE);
    // cout << start << ":" << array[start] << endl;
    array[start] = MARK_DONE;
    // cout << start << ":" << array[start] << endl;
    do {
      start = (start + 1) % ARRAY_SIZE;
    } while (array[start] == MARK_DONE);
  }

  for (auto i = 0; i < ARRAY_SIZE; i++) {
    if (array[i] != MARK_DONE) {
      cout << "right" << endl;
      return array[i];
    }
  }

  cout << "error" << endl;
  return -1;
}

int main() {
  cout << find_number<8>() << endl;
  cout << find_number<4321>() << endl;
  cout << find_number<987654321>();
}
