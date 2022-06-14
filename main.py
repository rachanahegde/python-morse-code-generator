# Morse code generator: takes any string input and converts it into morse code

# TODO Make dictionary with morse code alphabet and corresponding letters/numbers
morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    '¿': '..-.-',
    '¡': '--...-'
}

### Finish adding to the dictionary

# TODO Store user input as variable
text_string = input("Enter a string to convert into morse code: ")

# TODO Define function that accepts user input and returns morse code
# Set variable result to empty string
# Loop through user input string and append the corresponding value from the dict to the results string 
# Return result variable
# Catch errors that may occur if user enters a character that isn't in the dictionary

def morse_code(text_string):
    result = ""
    try:
        for item in text_string: 
            result += morse_code_dict[item.upper()] 
            result += " "
    except KeyError:
        print("That is not valid input.")
    return result

print(f"Here is your string in morse code: {morse_code(text_string)}")