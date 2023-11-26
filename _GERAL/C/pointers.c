#include <stdio.h>
#include <stdlib.h>
int *teste(int *x){
  return x;
}
void main(){
  int x = 10;
  int *y = &x;
  int n[] = {10, 9};
  int *m = n;
  int *res = teste(&x);
  printf("%d", m[0]);
  // printf("%d\n", x);
  // printf("%d", y);
}