<?php
$a = trim(fgets(STDIN));
$b = trim(fgets(STDIN));
if (strlen($a) > strlen($b)){
    print("$a\n");
} else {
    print("$b\n");
}
?>
