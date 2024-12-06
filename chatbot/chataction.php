<?php
    $json = trim(file_get_contents('php://input'));
    
    $url = 'https://www.gyaagl.app/apis/chatbot/chataction';
    $ch = curl_init($url);
     
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, $json);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        'Content-Type: application/json',
        'Content-Length: ' . strlen($json)
    ));
    
    curl_setopt($ch, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_1_1);
    $response = curl_exec($ch);
    if(curl_errno($ch)) {
        echo 'Error: ' . curl_error($ch);
    } else {
        echo $response;
    }
    curl_close($ch);

?>