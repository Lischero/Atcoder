<?php
$s = str_split(trim(fgets(STDIN)));
$i = intval(trim(fgets(STDIN)));
print("{$s[$i-1]}\n");
?>
