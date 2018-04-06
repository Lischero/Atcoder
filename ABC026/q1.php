<?php
$a = intval(trim(fgets(STDIN)));
$ans = 0;
for ($x = 0; $x <= $a; $x++){
    $y = $a-$x;
    $ans = max($ans, $x*$y);
}
print("$ans\n");
?>
