<?php
fscanf(STDIN, "%s %s", $a, $b);
if ($a == 'H'){
    print("$b\n");
} else {
    if ($b == 'H'){
        print("D\n");
    } else {
        print("H\n");
    }
}
?>
