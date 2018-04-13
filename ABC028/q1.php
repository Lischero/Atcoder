<?php
$n = intval(trim(fgets(STDIN)));
if ($n <= 59){
    print("Bad\n");
} else if ($n <= 89){
    print("Good\n");
} else if ($n <= 99){
    print("Great\n");
} else {
    print("Perfect\n");
}
?>
