<?php
$n = array_reverse(str_split(decbin(intval(trim(fgets(STDIN))))));
$ans = 0;
$factors = [];
for ($tmp = 0; $tmp < count($n); $tmp++){
    if ($n[$tmp] == '1'){
        array_push($factors, 2**$tmp);
        $ans += 1;
    }
}
print("$ans\n");
for ($tmp = 0; $tmp < count($factors); $tmp++){
    print("$factors[$tmp]\n");
}
?>
