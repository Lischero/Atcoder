<?php
$ans = 0;
fscanf(STDIN, "%d %d", $a, $b);
for ($tmp = $a; $tmp <= $b; $tmp++){
    if (strval($tmp) == strrev(strval($tmp))){
        $ans++;
    }
}
print("$ans\n");
?>
