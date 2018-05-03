<?php
fscanf(STDIN, "%d %d %d", $a, $b, $c);
$array = [ $a, $b, $c ];
$five = 0;
$seven = 0;
for ($tmp = 0; $tmp < 3; $tmp++){
    if ($array[$tmp] == 5){
        $five += 1;
    }
    if ($array[$tmp] == 7){
        $seven += 1;
    }
}
if ($five == 2 and $seven == 1){
    print("YES\n");
} else {
    print("NO\n");
}
?>
