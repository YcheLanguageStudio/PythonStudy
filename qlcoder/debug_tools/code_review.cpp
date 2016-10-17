#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

class Functor {
public:
  int32_t operator()(int32_t x) { return x * mulnum ^ xornum ^ twist(x); }
  Functor(int32_t mularg, int32_t xorarg) : mulnum(mularg), xornum(xorarg) {}

private:
  int32_t mulnum, xornum;
  int32_t twist(int32_t x) {
    return (((x >> 1) & 0x40000000) | (x & 0x3fffffff));
  }
};

int main() {
  Functor f(398, 0xfba802c7);
  vector<int32_t> solve32(Functor &);
  vector<int32_t> solns = solve32(f);
  for (int32_t ans : solns) {
    cout << ans << endl;
  }
  return 0;
}

vector<int32_t> solve32(Functor &f) {
  vector<int32_t> solns, tmp;
  void solve30(Functor &, int32_t, int, vector<int32_t> &solns);
  solve30(f, 0, 0, solns);
  solns.swap(tmp);
  int32_t y;
  for (auto x : tmp) {
    y = (x & 0x3fffffff) | 0x00000000;
    if (!f(y))
      solns.push_back(y);
    y = (x & 0x3fffffff) | 0x40000000;
    if (!f(y))
      solns.push_back(y);
    y = (x & 0x3fffffff) | 0x80000000;
    if (!f(y))
      solns.push_back(y);
    y = (x & 0x3fffffff) & 0xc0000000;
    if (!f(y))
      solns.push_back(y);
  }
  return solns;
}

void solve30(Functor &f, int32_t x, int i, vector<int32_t> &solns) {
  // if (false == solns.empty()) { return; }
  // you can determine when to return
  // if there are too many solutions
  if (i >= 30) {
    solns.push_back(x);
    return;
  }
  int32_t mask = (1 << (i + 1)) - 1;
  if ((f(x) & mask) == 0) {
    solve30(f, x, i + 1, solns);
  }
  x = x | (1 << i);
  if ((f(x) & mask) == 0) {
    solve30(f, x, i + 1, solns);
  }
}
