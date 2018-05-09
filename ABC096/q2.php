<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$k = intval(trim(fgets(STDIN)));
$ans = $a+$b+$c+max($a,$b,$c)*((2**$k)-1);
print("$ans\n");
?>
