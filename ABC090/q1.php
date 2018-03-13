<?php
$factor = array();
for($tmp = 0; $tmp < 3; $tmp++){
    $c = str_split(trim(fgets(STDIN)));
    array_push($factor, $c);
}
$ans = $factor[0][0].$factor[1][1].$factor[2][2];
print("$ans\n");
?>
