<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];
    $text_input = escapeshellarg($_POST['text_input']); // Sanitize input

    $command = "";

    if ($action === 'text_to_morse') {
        $text_input = $_POST['text_input'];
        $command = "python3 morse_translator.py text_to_morse $text_input";
    } elseif ($action === 'morse_to_text') {
        $command = "python3 morse_translator.py morse_to_text $text_input";
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