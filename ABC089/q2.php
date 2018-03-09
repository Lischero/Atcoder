<?php
$n = intval(trim(fgets(STDIN)));
$s = explode(" ", trim(fgets(STDIN)));
$factor = array_values(array_unique($s));
$ans = count($factor);
if ($ans == 4){
    print ("Four\n");
} else {
    print ("Three\n");
}
?>
