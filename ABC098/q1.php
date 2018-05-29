<?php
fscanf(STDIN, "%d %d", $a, $b);
$ans = max($a+$b, max($a-$b, $a*$b));
print("$ans\n");
?>
