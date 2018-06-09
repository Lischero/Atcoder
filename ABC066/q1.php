<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$ans = min($a+$b, min($a+$c, $b+$c));
print("$ans\n");
?>
