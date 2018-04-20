<?php
$a = intval(trim(fgets(STDIN)));
$b = intval(trim(fgets(STDIN)));
$n = intval(trim(fgets(STDIN)));
for ($tmp = $n; ;$tmp++){
    if (!($tmp%$a)&&!($tmp%$b)){
        print("$tmp\n");
        break;
    }
}
?>
