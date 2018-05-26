<?php
fscanf(STDIN, "%s %s %s", $a, $b, $c);
if (substr($a, strlen($a)-1, 1) == substr($b, 0, 1) and substr($b, strlen($b)-1, 1) == substr($c, 0, 1)){
    print("YES\n");
} else {
    print("NO\n");
}
?>
