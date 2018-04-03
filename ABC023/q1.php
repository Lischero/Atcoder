<?php
$x = str_split(trim(fgets(STDIN)));
$ans = 0;
for ($tmp = 0; $tmp < count($x); $tmp++){
    $ans += intval($x[$tmp]);
}
print("$ans\n");
?>
