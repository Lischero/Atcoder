<?php
$c = trim(fgets(STDIN));
if ($c == 'a' or $c == 'e' or $c == 'i' or $c == 'o' or $c == 'u'){
    print("vowel\n");
} else {
    print("consonant\n");
}
?>
