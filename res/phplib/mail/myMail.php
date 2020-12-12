<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'src/Exception.php';
require 'src/PHPMailer.php';
require 'src/SMTP.php';

function sendM($to,$s,$m, $f = 0, $h = false)
{
//	$passs = "1234123235123423532112341232351234235321";
    $passs = "Agricos25042020!"; //google account password
//	$passs = "rywtxgroxqqgxrgb!"; //google application password
//	$passs = "***"; //yandex

//	$from = 'no-reply@agricole.md';
    $from = 'agricos.md@gmail.com';
//	$from = 'agricole.md@yandex.ru';
    $mail = new PHPMailer(true);
    $mail->isSMTP();
    $mail->SMTPDebug = 0;
//	$mail->Host = "smtp.agricole.md";
    $mail->Host = "smtp.gmail.com";
//	$mail->Host = "smtp.yandex.ru";
//	$mail->Port = "25"; // typically 587
    $mail->Port = 465;
    $mail->SMTPSecure = 'ssl'; // ssl is depracated
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
    $mail->SMTPAuth = true;
    $mail->Username = $from;
    $mail->CharSet = "utf-8";
    $mail->Password = $passs;
    $mail->addReplyTo($from);
    $mail->setFrom($from, "Agricole");
    $mail->addAddress($to);
    $mail->Subject = $s;



    if($h)
    {
        $mail->MsgHTML($m); // remove if you do not want to send HTML email
        $mail->AltBody = 'HTML not supported';
    }
    else
    {
        $mail->IsHTML(false);
        $mail->Body = $m;
    }

    if($f!=0)
        $mail->AddAttachment($f['tmp_name'], $f['name']);
    $mail->send();
}

?>
