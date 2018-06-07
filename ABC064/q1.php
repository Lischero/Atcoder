<?php
fscanf(STDIN, "%d %d %d", $r, $g, $b);
$ans = intval($r.$g.$b);
if ($ans%4){
    print("NO\n");
} else {
    print("YES\n");
}
?>
