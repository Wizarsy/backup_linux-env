#include <stdio.h>

int main(void) {
  int x, a, p;
  p = 1;
  do{
    printf("\n Digite um numero inteiro positivo: ");
    scanf("%d", &x);
  } while( x <= 0);
  printf("\n Digite o expoente: ");
  scanf("%d", &a);
  while(a-- > 0){
    p *= x;
  }
  printf("\nPow = %d\n", p);
  return 0;
}