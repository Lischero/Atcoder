<?php
fscanf(STDIN, "%d %d", $n, $x);
$ans = min($x-1, $n-$x);
print("$ans\n");
?>
