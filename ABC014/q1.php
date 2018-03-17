<?php
$a = intval(trim(fgets(STDIN)));
$b = intval(trim(fgets(STDIN)));
$ans = ($a%$b)?($b-($a%$b)):0;
print("$ans\n");
?>
