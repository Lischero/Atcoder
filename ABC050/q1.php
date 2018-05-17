<?php
fscanf(STDIN, "%d %s %d", $a, $op, $b);
$ans = 0;
if ($op == '+'){
    $ans = $a+$b;
} else {
    $ans = $a-$b;
}
print("$ans\n");
?>
