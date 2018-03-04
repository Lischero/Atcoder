<?php
$n = intval(trim(fgets(STDIN)));
$ans = intval($n/2);
if ($n%2){
    $ans += 1;
    print ("$ans\n");
} else {
    print ("$ans\n");
}
?>
