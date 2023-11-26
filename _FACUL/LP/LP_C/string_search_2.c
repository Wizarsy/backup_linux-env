#include <stdio.h>
#include <string.h>

int main(void){
  char word[100], phrase[100], temp[100];
  int i, j = 0, vezes = 0;

  printf("Digite uma frase: ");
  gets(phrase);
  printf("Digite uma palavra: ");
  gets(word);

  for(i = 0; phrase[i] != '\0'; i++){
    temp[j] = phrase[i];
    if(strlen(temp) > (strlen(word))){
      temp[j] = '\0';
      printf("%s\n", temp);
      if(!strcmp(temp, word)){
        j = 0;
        vezes++;
      }
      else{
        j = 0;
        i-= (strlen(word) - 1);
      }
    }
    j++;
  }
  printf("\nA palavra %s aparece %d vezes", word, vezes);
  return 0;
}