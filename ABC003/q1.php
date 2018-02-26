<?php
$n = intval(trim(fgets(STDIN)));
$ans = array_sum(range(1, $n))*(1/$n)*10000;
echo "$ans\n";
?>
