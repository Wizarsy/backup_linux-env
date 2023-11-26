#include <stdio.h>

int main(void){
  int f;
  printf("\nDigite uma temp: ");
  scanf("%d", &f);
  double celsius = (double)((f - 32) * 5) / 9;
  printf("%lf", celsius);
  return 0;
}
