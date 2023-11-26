function CycleSort(array){
  for (let start = 0; start < array.length; start++){
    var item = array[start];
    var index = start;
    for(let i = (start + 1); i < array.length; i++){
      if(array[i] < item){
        index++;
      }
    }
    if(index == start){
      continue;
    }
    while(item ==  array[index]){
      index++;
    }
    [array[index], item] = [item, array[index]];
    while(index != start){
      index = start;
      for(let i = (start + 1); i < array.length; i++){
        if(array[i] < item){
          index++;
        }
      }
      while(item == array[index]){
        index++;
      }
      [array[index], item] = [item, array[index]];
    }
  }
}

const array_teste = [8, 3, 5, 7, 1, 9, 6, 0, 4, 2]

console.log("Entrada:");
console.log(array_teste);

CycleSort(array_teste)
console.log("\nSaida:");
console.log(array_teste);