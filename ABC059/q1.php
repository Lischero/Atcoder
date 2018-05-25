<?php
fscanf(STDIN, "%s %s %s", $a, $b, $c);
$ans = strtoupper(substr($a, 0, 1).substr($b, 0, 1).substr($c, 0, 1));
print("$ans\n");
?>
