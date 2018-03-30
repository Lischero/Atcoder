<?php
$n = intval(trim(fgets(STDIN)));
fscanf(STDIN, "%d %d", $d, $x);
$a = [];
$ans = 0;
for ($tmp = 0; $tmp < $n; $tmp++){
    array_push($a, intval(trim(fgets(STDIN))));
}
for ($tmp = 0; $tmp < $n; $tmp++){
    $factor = 0;
    while ($factor*$a[$tmp]+1 <= $d){
        $ans++;
        $factor++;
    }
}
$ans += $x;
print("$ans\n");
?>
