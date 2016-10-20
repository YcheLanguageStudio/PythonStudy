#include <bitset>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

long long twist(long long u, long long v) {
  return (((u & 0x80000000L) | (v & 0x7fffffffL)) >> 1) ^
         ((v & 1) == 1 ? 0x9908b0dfL : 0);
}
long long state[624];
int left_index = 1;

void next_state() {
  int p = 0;
  left_index = 624;
  for (int j = 228; --j > 0; p++)
    state[p] = state[p + 397] ^ twist(state[p], state[p + 1]);

  for (int j = 397; --j > 0; p++)
    state[p] = state[p - 227] ^ twist(state[p], state[p + 1]);

  state[p] = state[p - 227] ^ twist(state[p], state[0]);
}

long long next() {
  if (--left_index == 0)
    next_state();
  return state[624 - left_index];
}

int main() {
  for (int j = 1; j < 624; j++) {
    state[j] = (1812433253L * (state[j - 1] ^ (state[j - 1] >> 30)) + j);
    state[j] &= 0xfffffffffL;
  }
  cout << "?" << endl;
  bitset<1073741823> &statistic_bitset = *(new bitset<1073741823>());
  cout << "?" << endl;
  for (long long i = 0; i < 50000000000L; i++) {
    long long tmp_long = next();
    if ((tmp_long & 0x000000000000003f) == 0x0000000000000000)
      tmp_long >>= 6;
    else
      continue;
    statistic_bitset.set(tmp_long, true);
  }
  cout << statistic_bitset.count() * 64 << endl;
  return 0;
}
