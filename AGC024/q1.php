<?php
fscanf(STDIN, "%d %d %d %d", $a, $b, $c, $k);
if (abs($a-$b) > 10**18){
    print("Unfair\n");
    exit(0);
}
if ($k%2){
    $ans = $b-$a;
} else {
    $ans = $a-$b;
}
print("$ans\n");
?>
