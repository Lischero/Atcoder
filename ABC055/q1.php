<?php
$n = intval(trim(fgets(STDIN)));
$ans = 800*$n - 200*floor($n/15);
print("$ans\n");
?>
