<?php
$s = str_split(trim(fgets(STDIN)));
$n = intval(trim(fgets(STDIN)));
$factors = [];
foreach($s as $value1){
    foreach($s as $value2){
        array_push($factors, $value1.$value2);
    }
}
sort($factors);
print("{$factors[$n-1]}\n");
?>
