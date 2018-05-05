<?php
$n = intval(trim(fgets(STDIN)));
$k = intval(trim(fgets(STDIN)));
$x = intval(trim(fgets(STDIN)));
$y = intval(trim(fgets(STDIN)));
if ($n <= $k){
    $ans = $n*$x;
} else {
    $ans = $k*$x+($n-$k)*$y;
}
print("$ans\n");
?>
