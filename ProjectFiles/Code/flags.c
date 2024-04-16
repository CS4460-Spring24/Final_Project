
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc > 1 && strcmp(argv[1], "-help") == 0) {
        printf("ejmCTF{real_flag} is the real flag\n");
        
    } else {
        printf("ejmCTF{fake_flag} is a fake flag\n");
        printf("execute me again with a \"-help\" parameter to reveal the real flag\n");
    }
    return 0;
}