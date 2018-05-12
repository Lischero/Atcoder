<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
if ($a == $b+$c or $b == $a+$c or $c == $b+$a){
    print("Yes\n");
} else {
    print("No\n");
}
?>
