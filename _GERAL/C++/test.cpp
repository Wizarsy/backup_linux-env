#include <iostream>
using namespace std;

  float cv = 6.00;
  float cf = 60.000;
  float p = 8.00;

  float custo(float x){
    return cf + (cv * x);
  }
  float receita(float x){
    return p * x;
  }
  float lucro(float x){
    return receita(x) - custo(x);
  }
int main() {
  float x = 10;
  
  cout << custo(x);
}