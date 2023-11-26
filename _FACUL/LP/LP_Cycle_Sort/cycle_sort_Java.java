import java.util.Arrays;
public class cycle_sort_Java {
  static void CycleSort(int[] array){
    int size = array.length;
    for(int start = 0; start < size; start++){
      int item = array[start];
      int index = start;
      for(int i = start +1; i < size; i++){
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
      int temp = array[index];
      array[index] = item;
      item = temp;
      while(index != start){
        index = start;
        for(int i = start +1; i < size; i++){
          if(array[i] < item){
            index++;
          }
        }
        while(item == array[index]){
          index++;
        }
        temp = array[index];
        array[index] = item;
        item = temp;
      }
    }
  }
  public static void main(String[] args) {
    int[] array_test = {8, 3, 5, 7, 1, 9, 6, 0, 4, 2};
    System.out.println("Entrada: " + Arrays.toString(array_test) + "\n");
    CycleSort(array_test);
    System.out.println("Saida: " + Arrays.toString(array_test));
  }
}