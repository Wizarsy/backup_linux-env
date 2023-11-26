#include <stdio.h>
#include <string.h>

int main(void){
  char origem[100], copia[100];
  int j = 0;

  printf("\nDigite uma string: ");
  gets(origem);

  for(int i = 0; origem[i] != '\0'; i++){
    if(origem[i] >= 97 && origem[i] <= 122){
      copia[j] = origem[i] - 32;
      j++;
    }
    else if ((origem[i] >= 48 && origem[i] <= 57) || (origem[i] >= 65 && origem[i] <= 90)){
      copia[j] = origem[i];
      j++;
    }
  }
  copia[j] = '\0';
  printf("\n%s", copia);
  return 0;
}