<?php
$wordList = [ 'a', 'b', 'c' ];
$list = [];
for ($tmp = 0; $tmp < 3; $tmp++){
    $n = intval(trim(fgets(STDIN)));
    $list[$wordList[$tmp]] = $n;
}
arsort($list);
for ($tmp = 0; $tmp < 3; $tmp++){
    $word = key(array_slice($list, $tmp, 1, true));
    $list[$word] = $tmp+1;
}
for ($tmp = 0; $tmp < 3; $tmp++){
    $ans = $list[$wordList[$tmp]];
    print("$ans\n");
}
?>
