<?php
$n = str_split(trim(fgets(STDIN)));
$factors = array_values(array_unique($n));
if (count($factors) == 1){
    print("SAME\n");
} else {
    print("DIFFERENT\n");
}
?>
