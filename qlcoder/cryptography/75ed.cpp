#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int d(int keys[], char c[], char m[]) {
  int clen = strlen(c);
  int mindex = 0;
  for (int i = 0; i < clen; i += 6) {
    int tmp = 0;
    sscanf(c + i, "%6x", &tmp);
    for (int j = 0; j < 3; ++j) {
      tmp = (tmp << 17) | (tmp >> 7);
      tmp = tmp & ((1 << 24) - 1);
      tmp ^= (keys[tmp & 3] << 8);
    }
    m[i / 2] = ((tmp & 0xff0000) >> 16);
    m[i / 2 + 1] = ((tmp & 0xff00) >> 8);
    m[i / 2 + 2] = (tmp & 0xff);
    for (int j = 0; j < 3; ++j) {
      if ((m[i / 2 + j] < 32) || (m[i / 2 + j] > 126))
        return 0;
    }
  }
  return 1;
}

int main() {
  char c[] =
      "bb2af286e3ec8ead77cf81d0e7299fef8fd0a3837a4621fef3827dd0887c51aa168b4f09"
      "53aa3f070dfffc2cb0df8afdbdacbddce28165efe57ceac945cde63c28d23ce6e927a9f2"
      "624b4f8683fa51e8683da6fdaba13a2b055d0b2f7e0583f299081139027275089311cc6b"
      "112a124f85d3070dff6b237d53aa1f51805ed3aa3efd66e4dce2eb50ea29870dfffe26f4"
      "e66988116041b12073dda2f71d2292e381305ce28baf8dd3c643e1f92c90b1a45f1c86d6"
      "190e700ba932838d7794205669c54591205329eb468683fac9095e85c3cc51e868d1a05e"
      "6a4b4b8683fabb2af286e3ece9e546d02e504f85d36b0b5f6aa532bdacbde38530dce2e1"
      "130a12254fc8e9213751e868eb2137b1406ca72dff4601ff4aaf32a3837ad38a1f71827d"
      "7024139d22da5f64c56769c962215e0bab721340447c88fe5da29dd8805e6a412b6b237f"
      "590e33d16c464aaf327904132f89f0fc8adea589d2e8a550f50ed2250fdedcca814d095f"
      "990a334643a8ddaafdd0887ceb21175ca2bfd1a05ea9eb46d0887cc723d7bd28b2caaf30"
      "bf86ffdce2eb7faadfff46e45ce28b1f42a54603ff750eb305079658c2ab2ba313072dff"
      "6b237d53aa1f7f66e5d1c04fbfaeded1a05ab4267a152a12ea4361caaf324601ff6b2b5d"
      "8683fa1ca4dea6a9f2a60fdd690b5fd1aa3e5de280af89d28be925c643a1c5c5c6e729dc"
      "d90c50c723d73c2ad2ea21371d22923508923d2ad0d34e46620b5d8683fa71a05d8b2f3d"
      "3c2a92190830536c659ca4dc91281370827d7e26f3eb4b4bd0887ceb211705e3e61f84de"
      "eb6121d36c4490005245ede406a3f33d86fe074deb502e50620b5d71a05d53aa1f3508d2"
      "d3887ed0805fc643c167299ff0a0775ca2bf5da2d64f85d3d1805ffd8a9f50c82951805e"
      "7cea892a255e050dff6b237d53aa1fff66e6e9233ef50ed023813045c5c4b1ac5edfa2fd"
      "4aaf324f85d3870dfdbcee887daad63c4ae55f04d3e7618fbfaeded1a05ab4267a152a12"
      "ea4361aaa13abd2a92a6a9d227c9c4790413a3837a7ccae8ebc5467904122381536ba772"
      "50ea08936044c643c1716405d3887eea41216a237d53aa1f750e937ccac92a47608f85d3"
      "3da6ff27a9f2b50ab2a9eb4586a3b3f08077930a12102a32870dffc4adf0fdaa9e7daabf"
      "a9c12c256fe80e0dffea610149095f438f5385e1ccc585d0df8ad7918e5d916a0507c3e4"
      "8f81d33da6ff27a9f2a589d292205245ede4dfa2971d22926385533deec94aaf3258c04c"
      "a7a991af89d306e3e48f81d3bda6ffe5cfc67f06f2a9c366e68fd2936044c643c18b4f09"
      "e92137dce2814621fef3827dd0887c0727b649095f4f85d33f6aa4934045ff66e3314266"
      "50ea4929c366702413604bce\0";
  char m[1968];
#pragma omp parallel num_threads(16), private(m)
  for (int i0 = 0; i0 < 255; i0++) {
    for (int i1 = 0; i1 < 255; i1++) {
      for (int i2 = 0; i2 < 255; i2++) {
        for (int i3 = 0; i3 < 255; i3++) {
          int keys[] = {0, 0, 0, 0};
          keys[0] = i0;
          keys[1] = i1;
          keys[2] = i2;
          keys[3] = i3;
          if (d(keys, c, m) == 1) {
            cout << m << endl;
          }
        }
      }
    }
  }
  return 0;
}
