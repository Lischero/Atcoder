<?php
$ans = 0;
for ($tmp = 0; $tmp < 3; $tmp++){
    fscanf(STDIN, "%d %d", $s, $e);
    $ans += $s*($e/10);
}
print("$ans\n");
?>
