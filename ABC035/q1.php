<?php
fscanf(STDIN, "%d %d", $w, $h);
if (3*$w == 4*$h){
    print("4:3\n");
}
if (9*$w == 16*$h){
    print("16:9\n");
}
?>
