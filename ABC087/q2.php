<?php
$a = (int)trim(fgets(STDIN));
$b = (int)trim(fgets(STDIN));
$c = (int)trim(fgets(STDIN));
$x = (int)trim(fgets(STDIN));
$ans = 0;
for($tmp = 0; $tmp <= $a; $tmp++){
    for($tmp2 = 0; $tmp2 <= $b; $tmp2++){
        for($tmp3 = 0; $tmp3 <= $c; $tmp3++){
            if (500*$tmp+100*$tmp2+50*$tmp3 == $x){
                $ans++;
            }
        }
    }
}
echo ($ans)."\n";
?>
