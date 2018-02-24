<?php
fscanf(STDIN, "%s %s", $x, $y);
$factors = [];
for ($tmp = 0; $tmp < 6; $tmp++){
    $factors[chr(ord('A')+$tmp)] = $tmp+10;
}
if ($factors[$x] < $factors[$y]){
    print "<\n";
} else if($factors[$x] > $factors[$y]){
    print ">\n";
} else {
    print "=\n";
}
?>
