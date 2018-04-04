<?php
fscanf(STDIN, "%d %d %d %d", $a, $b, $c, $k);
fscanf(STDIN, "%d %d", $s, $t);
if ($s+$t >= $k){
    $ans = $s*($a-$c)+$t*($b-$c);
} else {
    $ans = $s*$a+$t*$b;
}
print("$ans\n");
?>
