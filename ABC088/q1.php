<?php
$n = intval(trim(fgets(STDIN)));
$a = intval(trim(fgets(STDIN)));
$n -= 500*intval($n/500);
if ($n <= $a){
    print "Yes\n";
} else {
    print "No\n";
}
?>
