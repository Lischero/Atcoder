<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$factors = [ $a, $b, $c ];
sort($factors);
print("$factors[1]\n");
?>
