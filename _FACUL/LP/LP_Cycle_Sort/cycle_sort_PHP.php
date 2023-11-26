<?php
function swap(&$a, &$b){
  $temp = $a;
  $a = $b;
  $b = $temp;
}

function printArray(array $array){
  for($i = 0; $i < count($array); $i++){
    echo $array[$i] . " ";
  }
  echo "\n\n";
}
///////////////////////////////////////////////////////////////////////////////////////////////////
function CycleSort(array &$array){
  $size = count($array);
  for($start = 0; $start < $size; $start++){
    $item = $array[$start];
    $index = $start;
    for($i = $start + 1; $i < $size; $i++){
      if($array[$i] < $item){
        $index++;
      }
    }
    if($index == $start){
      continue;
    }
    while($item == $array[$index]){
      $index++;
    }
    swap($array[$index], $item);
    while($index != $start){
      $index = $start;
      for($i = $start + 1; $i < $size; $i++){
        if($array[$i] < $item){
          $index++;
        }
      }
      while($item == $array[$index]){
        $index++;
      }
      swap($array[$index], $item);
    }
  }
}

$array_teste = array(8, 3, 5, 7, 1, 9, 6, 0, 4, 2);
echo "Entrada: ";
printArray($array_teste);
CycleSort($array_teste);
echo "Saida: ";
printArray($array_teste);
?>