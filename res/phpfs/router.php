<?php
$ssurl=explode("/", $_SERVER['REQUEST_URI'])[1];
if(count($ssurl)>0)
{
    $main_page=array_keys($ssurl)[0];
    $available_pages=["reg"];
    if(in_array($main_page,$available_pages))
        $current_main_page = $main_page;
    else
        $current_main_page = "main";
}
else
    $current_main_page = "main";

?>