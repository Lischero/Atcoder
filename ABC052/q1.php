<?php
fscanf(STDIN, "%d %d %d %d", $a, $b, $c, $d);
$factor = $a*$b;
$factor2 = $c*$d;
if ($factor >= $factor2){
    print("$factor\n");
} else {
    print("$factor2\n");
}
?>
