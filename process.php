<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $text_input = escapeshellarg($_POST['text_input']); // Sanitize input


    $command = "";

    if ($action === 'text_to_morse') {    
        $command = "python3 morse_translator.py text_to_morse $text_input";
    } elseif ($action === 'morse_to_text') {
        $command = "python3 morse_translator.py morse_to_text $text_input";
    } elseif ($action === 'text_encryption') {
        $command = "python3 Encryption.py $text_input";
    } elseif ($action === 'text_decryption') {
        if(!isset($_POST['key'])|| !isset($_POST['IV'])){
            echo "Invalid Key or IV";
            exit;
        } else{
            $key = escapeshellarg($_POST['key']);
            $IV = escapeshellarg($_POST['IV']);
            $command = "python3 Decryption.py $text_input $key $IV";}
        
    } else {
        echo "Invalid action.";
        exit;
    }   

    // Execute the command and capture the output
    $output = shell_exec($command);

    if ($output === null) {
        echo "Error processing your request.";
    } else {
        echo trim($output); // Return only the result
    }
}
?>