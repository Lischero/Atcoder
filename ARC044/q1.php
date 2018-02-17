<?php
function isPrime($num){
    $factor = 2;
    if ($num < 2){
        return False;
    } else {
        while (pow($factor,2) <= $num){
            if ($num%$factor == 0){
                return False;
            }
            $factor++;
        }
        return True;
    }
}

function likePrime($num){
    $arr = str_split(strval($num));
    $last = intval(end($arr));
    if ($last%2 != 0 and $last != 5 and array_sum($arr)%3){
        return True;
    } else {
        return False;
    }
}

$n = (int)trim(fgets(STDIN));
if (isPrime($n)){
    echo "Prime\n";
} else {
    if (likePrime($n) and $n != 1){
        echo "Prime\n";
    } else {
        echo "Not Prime\n";
    }
}
?>
