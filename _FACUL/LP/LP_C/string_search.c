#include <stdio.h>
#include <string.h>

int main(void){
  char word[100], phrase[100], temp[100];
  int i, j = 0, vezes = 0;

  printf("Digite uma frase: ");
  gets(phrase);
  printf("Digite uma palavra: ");
  gets(word);

  for(i = 0; i < strlen(phrase); i++){
    temp[j] = phrase[i];
    j++;
    temp[j] = '\0';
    if(!strcmp(temp, word)){
      j = 0;
      vezes++;
    }
    if(strlen(temp) == (strlen(word))){
      j = 0; 
      i-= (strlen(word) - 1);
    }
  }
  printf("\nA palavra %s aparece %d vezes", word, vezes);
  return 0;
}