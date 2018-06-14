<?php
fscanf(STDIN, "%d %d", $a, $b);
$ans = ($b-$a)*($b-$a+1)/2 - $b;
print("$ans\n");
?>
