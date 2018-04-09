<?php
fscanf(STDIN, "%s", $s);
$factors = str_split($s);
$ans = count(array_unique($factors));
if ($ans == 3){
    print("Yes\n");
} else { 
    print("No\n");
}
?>
