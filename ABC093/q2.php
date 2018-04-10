<?php
fscanf(STDIN, "%d %d %d", $a, $b, $k);
$factors = [];
if ($b-$a >= 2*$k){
    for ($tmp = $a; $tmp < $a+$k; $tmp++){
        array_push($factors, $tmp);
    }
    for ($tmp = $b-$k+1; $tmp <= $b; $tmp++){
        array_push($factors, $tmp);
    }
} else {
    for ($tmp = $a; $tmp <= $b; $tmp++){
        array_push($factors, $tmp);
    }
}
sort($factors);
for ($tmp = 0; $tmp < count($factors); $tmp++){
    print("{$factors[$tmp]}\n");
}
?>
