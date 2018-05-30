<?php
$n = intval(trim(fgets(STDIN)));
$s = trim(fgets(STDIN));
$ans = -1;
$place = ($n-1)*(-1);
for ($tmp = 0; $tmp < $n-1; $tmp++){
    $factor = 0;
    $sentence1 = array_values(array_unique(str_split(substr($s, 0, $tmp+1))));
    $sentence2 = array_values(array_unique(str_split(substr($s, $place))));
    for ($tmp2 = 0; $tmp2 < count($sentence1); $tmp2++){
        $val = $sentence1[$tmp2];
        if (in_array($val, $sentence2, TRUE)){
            $factor++;
        }
    }
    $ans = max($ans, $factor);
    $place += 1;
}
print("$ans\n");
?>
