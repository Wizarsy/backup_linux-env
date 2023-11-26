#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *sum(char *n1, char *n2, int n){
  int op1[n], op2[n];
  int *r = malloc((n + 1) * sizeof(int));
  int aux_sum, aux_div = 0;
  
  for (int i = (n - 1); i > -1; i--){
    op1[i] = (n1[i] - '0') > 0 ? n1[i] - '0' : 0;
    op2[i] = (n2[i] - '0') > 0 ? n2[i] - '0' : 0;
    aux_sum = op1[i] + op2[i] + aux_div;
    r[i + 1] = aux_sum % 10;
    aux_div = aux_sum / 10;
  }
  r[0] = aux_div;
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