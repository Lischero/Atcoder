<?php
$priority = [];
for ($count = 1, $tmp = 2; $tmp < 14; $tmp++){
    $priority[$tmp] = $count;
    $count++;
}
$priority[1] = 13;
fscanf(STDIN, "%d %d", $a, $b);
if ($priority[$a] > $priority[$b]){
    print("Alice\n");
} else if($priority[$a] < $priority[$b]){
    print("Bob\n");
} else {
    print("Draw\n");
}
?>
