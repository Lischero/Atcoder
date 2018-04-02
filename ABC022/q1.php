<?php
fscanf(STDIN, "%d %d %d", $n, $s, $t);
$w = intval(trim(fgets(STDIN)));
$ans = 0;
for ($tmp = 0; $tmp < $n; $tmp++){
    if ($w >= $s && $w <= $t){
        $ans += 1;
    }
    if ($tmp == $n-1){
        break;
    }
    $w += intval(trim(fgets(STDIN)));
}
print("$ans\n");
?>
