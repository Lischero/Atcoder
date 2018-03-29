<?php
$a = intval(trim(fgets(STDIN)));
$b = intval(trim(fgets(STDIN)));
$c = intval(trim(fgets(STDIN)));
$d = intval(trim(fgets(STDIN)));
$ans = min($a, $b) + min($c, $d);
print("$ans\n");
?>
