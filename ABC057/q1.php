<?php
fscanf(STDIN, "%d %d", $a, $b);
$ans = $a+$b;
if ($a+$b >= 24){
    $ans -= 24;
}
print("$ans\n");
?>
