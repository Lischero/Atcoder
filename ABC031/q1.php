<?php
fscanf(STDIN, "%d %d", $a, $b);
$factor = ($a+1)*$b;
$factor2 = $a*($b+1);
if ($factor >= $factor2){
    print("$factor\n");
} else {
    print("$factor2\n");
}
?>
