#include <fcntl.h>
#include <iostream>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

using namespace std;
int main() {
  int fd = open("PiDec.txt", O_RDONLY);
  struct stat st;
  fstat(fd, &st);
  long long whole_size = st.st_size;
  char compared_chars[] = {2, 7, 1, 8, 2, 8, 1, 8, 2, 8};

  for (long long current_offset = 0; current_offset < whole_size;
       current_offset += 1024 * 1024 * 1024) {
    cout << "offset:" << current_offset << endl;
    long long mmap_size = 1024 * 1024 * 1024 + 10;
    if (current_offset + mmap_size > whole_size) {
      mmap_size = whole_size - current_offset - 1;
      cout << "updated mmap_si:" << mmap_size << endl;
    }
    char *mmap_chars = (char *)mmap(NULL, mmap_size, PROT_READ, MAP_PRIVATE, fd,
                                    current_offset);
    for (long long i = 0; i < mmap_size - 10; i++) {
      bool same = true;
      for (long long j = 0; j < 10; j++) {
        if (compared_chars[j] != mmap_chars[i + j]) {
          same = false;
          break;
        }
      }
      if (same) {
        cout << current_offset + i << endl;
      }
    }
    munmap(mmap_chars, mmap_size);
  }
}
