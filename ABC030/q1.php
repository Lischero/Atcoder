<?php
fscanf(STDIN, "%d %d %d %d", $a, $b, $c, $d);
if ($b/$a > $d/$c){
    print("TAKAHASHI\n");
} else if ($b/$a < $d/$c){
    print("AOKI\n");
} else {
    print("DRAW\n");
}
?>
