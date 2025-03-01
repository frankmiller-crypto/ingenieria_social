<?php
function pc_permute($items, $perms = array()) {
    if (empty($items)) { 
        echo join('', $perms) . "<br/>";
    } else {
        for ($i = count($items) - 1; $i >= 0; --$i) {
             $newitems = $items;
             $newperms = $perms;
             list($foo) = array_splice($newitems, $i, 1);
             array_unshift($newperms, $foo);
             pc_permute($newitems, $newperms);
         }
    }
}

$arr = array('09', 'septiembre', '1941');

pc_permute($arr);
?>