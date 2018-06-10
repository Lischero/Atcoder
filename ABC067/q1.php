<?php
fscanf(STDIN, "%d %d", $a, $b);
if ($a%3 == 0 or $b%3 == 0 or ($a+$b)%3 == 0){
    print("Possible\n");
} else {
    print("Impossible\n");
}
?>
