<?php
header('Access-Control-Allow-Origin: localhost');
header('Content-Type: application/json; charset=utf-8');
$output = ["Hello"=>"World"];

echo json_encode($output,JSON_PRETTY_PRINT);
?>