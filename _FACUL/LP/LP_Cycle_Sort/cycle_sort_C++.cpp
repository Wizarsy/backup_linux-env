#include <iostream>

using namespace std;

void printArray(int *array, int size){
  for(int i = 0; i < size; i++){
    cout << array[i] << " ";
  }
  cout << "\n\n";
}
///////////////////////////////////////////////////////////////////////////////////////////////////
void CycleSort(int *array, int size){
  for(int start = 0; start < size; start++){
    int item = array[start];
    int index = start;
    for(int i = start + 1; i < size; i++){
      if(array[i] < item){
        index++;
      }
    }
    if(index == start){
      continue;
    }
    while(item == array[index]){
      index++;
    }
    swap(array[index], item);
    while(index != start){
      index = start;
      for(int i = start + 1; i < size; i++){
        if(array[i] < item){
          index++;
        }
      }
      while(item == array[index]){
        index++;
      }
      swap(array[index], item);
    }
  }
}


int array_teste[] = {10, 3, 5, 7, 1, 9, 6, 0, 4, 2};
int array_size = sizeof(array_teste) / sizeof(int);

int main(){
  cout << "Entrada: ";
  printArray(array_teste, array_size);
  CycleSort(array_teste, array_size);
  cout << "Saida: ";
  printArray(array_teste, array_size);
}