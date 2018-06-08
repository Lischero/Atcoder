<?php
fscanf(STDIN, "%d %d %d", $x, $a, $b);
$factor = $a-$b;
if ($factor >= 0){
    print("delicious\n");
} else {
    if (abs($factor) <= $x){
        print("safe\n");
    } else {
        print("dangerous\n");
    }
}
?>
