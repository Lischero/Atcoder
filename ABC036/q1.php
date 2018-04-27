<?php
fscanf(STDIN, "%d %d", $a, $b);
$ans = intval(floor($b/$a));
if ($b%$a == 0){
    print("$ans\n");
} else {
    $ans += 1;
    print("$ans\n");
}
?>
