<?php
fscanf(STDIN, "%d %d", $a, $b);
$ans = $a+$b;
if ($ans >= 10){
    print("error\n");
} else {
    print("$ans\n");
}
?>
