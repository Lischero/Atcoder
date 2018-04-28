<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$ans = intval($c/min($a, $b));
print("$ans\n");
?>
