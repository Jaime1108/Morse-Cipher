import sys

# Morse code dictionary
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/', '!':'-.-.--'
}

def translate_from_text(text):
    translated_text = ""
    for char in text:
        if char.upper() in morse:
            translated_text += morse[char.upper()] + " "
    return translated_text.strip()

def translate_from_morse(morse_code):
    translated_morse = ""
    array_text = morse_code.split(" ")
    for morse_text in array_text:
        for key, value in morse.items():
            if morse_text == value:
                translated_morse += key.lower()
    return translated_morse

if __name__ == "__main__":
    # Read arguments passed from PHP
    mode = sys.argv[1]  # 'text_to_morse' or 'morse_to_text'
    input_text = sys.argv[2]

    if mode == "text_to_morse":
        print(translate_from_text(input_text))
    elif mode == "morse_to_text":
        print(translate_from_morse(input_text))
