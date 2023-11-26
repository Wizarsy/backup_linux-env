#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *multi(char *n1, char *n2, int n){
  int op1[n], op2[n];
  int *r = malloc((n + n) * sizeof(int));
  int aux_sum, aux_div, r_aux[n + 1], aux_mult;
  for (int i = 0; i < (n + 1); i++){
    r[i] = 0;
  }
  for (int i = (n - 1); i > -1; i--){
    aux_div = 0;
    for (int j = (n - 1); j > -1; j--){
      aux_mult = 
    }
  }

  return r;
}

void main(){
  char n1[100], n2[100];
  printf("N1: ");
  fgets(n1, sizeof(n1), stdin);
  printf("N2: ");
  fgets(n2, sizeof(n2), stdin);
  
  int n1len = strlen(n1) - 1;
  int n2len =  strlen(n2) - 1;
  int n = n1len > n2len ? n1len : n2len;
  
  int *res = sum(n1, n2, n);

  for (int i = 0; i < n + 1; i++){
    printf("%d ", res[i]);
  }
}