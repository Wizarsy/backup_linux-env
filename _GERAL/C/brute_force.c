#include <stdio.h>
#include <string.h>

int main(void) {
  char chr[10];
  char p[10] = "555555";
  for (int x = 48; x < 122; x++){
    chr[0] = x;
    for (int x1 = 48; x1 < 122; x1++){
      chr[1] = x1;
      for (int x2 = 48; x2 < 122; x2++){
        chr[2] = x2;
        for (int x3 = 48; x3 < 122; x3++){
          chr[3] = x3;
          for (int x4 = 48; x4 < 122; x4++){
            chr[4] = x4;
            for (int x5 = 48; x5 < 122; x5++){
              chr[5] = x5;
              chr[6] = '\0';
              if(!strcmp(chr, p)){
                printf("%s\n", chr);
                return 0;
              }          
            }
          }
        }
      }
    }
  }
}