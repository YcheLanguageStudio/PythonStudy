<?php
$lineSize = 256000;
$n = 0;
$charLen = 0;
$static = [
    'hz'=>0,
    'sh'=>0,
    'bj'=>0,
    'sz'=>0,
];
$fh=fopen("./ip.data","r");
while (!feof($fh)) {
    $str = fread($fh,$lineSize);
    calcLine($str);
    $n ++;
    if ($n>10) break;
}
fclose($fh);
function calcLine($str) {
    global $charLen;
    global $static;
    //$charLen += strlen($str);
    $len = strlen($str);
    $step = $len/5;
    for ($i=0; $i<$step; ++$i) {
        $loc1 = $i*5+2;
        $loc2 = $loc1+1;
        $city_id1 = ord($str[$loc1]);
        $city_id2 = ord($str[$loc2]);
        $city_id = $city_id1*256+$city_id2;
        $static['hz'] += $city_id==242;//245
        $static['sh'] += $city_id==133;//136
        $static['bj'] += $city_id==29;//32
        $static['sz'] += $city_id==75;//78
    }
}
echo 'lines='.$n." charLen=$charLen\n";
print_r($static);
