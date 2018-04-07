<?php
$n = array_map('intval', explode(" ", trim(fgets(STDIN))));
$factors = array_values(array_unique($n));
$factorsNum = [];
if (count($factors) == 1){
    print("$factors[0]\n");
} else {
    for ($tmp = 0; $tmp < count($factors); $tmp++){
        $factorsNum[$factors[$tmp]] = 0;
    }
    for ($tmp = 0; $tmp < count($n); $tmp++){
        $factorsNum[$n[$tmp]] += 1;
    }
    asort($factorsNum);
    $ans = key($factorsNum);
    print("$ans\n");
}
?>
