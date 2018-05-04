<?php
$n = intval(trim(fgets(STDIN)));
$ans = 0;
for ($tmp = 1; $tmp <= $n; $tmp++){
    $ans += $tmp;
}
print("$ans\n");
?>
