<?php
$db = "";
$l = "root";
$p = "";
$setup = R::setup('mysql:host=localhost;dbname='.$db, $l, $p);
R::addDatabase($db,'mysql:host=localhost;dbname='.$db, $l, $p);
?>