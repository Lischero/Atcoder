<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$ans = count(array_values(array_unique([$a, $b, $c])));
print("$ans\n");
?>
