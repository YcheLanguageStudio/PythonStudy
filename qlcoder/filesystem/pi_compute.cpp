#include <fcntl.h>
#include <iostream>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>

#define WINDOW_SIZE 512 * 1024 * 1024

using namespace std;
int main() {
  int fd = open("/home/cheyulin/PiDec.txt", O_RDONLY);
  struct stat st;
  fstat(fd, &st);
  long long whole_size = st.st_size;
  // char compared_chars[] = {2, 7, 1, 8, 2, 8, 1, 8, 2, 8};
  char compared_chars[] = {5, 9, 2, 6, 5, 3, 5, 8, 9, 8};

  int count = 0;
  for (long long current_offset = 0; current_offset < whole_size;
       current_offset += WINDOW_SIZE) {
    cout << "offset:" << current_offset << endl;
    long long mmap_size = WINDOW_SIZE + 10;
    if (current_offset + mmap_size > whole_size) {
      mmap_size = whole_size - current_offset - 1;
    }
    char *mmap_chars = (char *)mmap(NULL, mmap_size, PROT_READ, MAP_PRIVATE, fd,
                                    current_offset);
    char three = '3';
    cout << (int)mmap_chars[0];
    cout << (mmap_chars[0] == three);
    for (long long i = 0; i < mmap_size - 10; i++) {
      if (count < 20)
        cout << mmap_chars[i];
      count++;
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
