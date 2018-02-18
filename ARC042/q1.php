<?php
fscanf(STDIN, "%d %d", $n, $m);
$arr = range(1, $n);
for ($tmp = 0; $tmp < $m; $tmp++){
    $factor = intval(trim(fgets(STDIN)));
    $index = array_search($factor, $arr);
    $target = array_slice($arr, $index, 1)[0];
    unset($arr[$index]);
    array_unshift($arr, $target);
}
for ($tmp = 0; $tmp < count($arr); $tmp++){
    echo $arr[$tmp] . "\n";
}
?>
