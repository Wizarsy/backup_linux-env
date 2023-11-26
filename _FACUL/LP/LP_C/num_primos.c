#include <stdio.h>

int main(void){
  int fim, resto;
  fim = 1000;
  for(int num = 0; num < fim; num++){
    if (num == 1){
      continue;
    }
    else{
      if(num % 2 || num == 2){
        for(int div = 2; div < num; div++){
          resto = num % div;
          if(resto == 0){
          break;
          }
        }
        if(resto || num == 2){
          printf("%d\t", num);
        }
      }
    }
  }
  return 0;
}