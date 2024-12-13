import sys


def check_special_chars(string: str) -> bool:
    """
    Check if the string no contains space and alphanumeric characters
    """

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
                  0123456789 ")
    return any(char not in allowed_chars for char in string)


def convert_to_morse_code(string: str) -> str:
    """
    Convert a string to morse code
    """

    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    return ''.join((NESTED_MORSE[char] for char in string.upper()))


def main():
    try:
        if (len(sys.argv) != 2 or check_special_chars(sys.argv[1])):
            raise AssertionError("the arguments are bad")
        print(convert_to_morse_code(sys.argv[1]))
    except AssertionError as e:
        print("AssertionError: {}".format(e))


if (__name__ == "__main__"):
    main()
