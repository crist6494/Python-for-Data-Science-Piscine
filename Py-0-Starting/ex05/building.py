import sys


def analysis_text(text):
    """
    This script analyses a text and counts the number
    of upper letters, lower letters, punctuation marks, spaces,
    digits and characters in the text.
    """

    text_analysis = {
        'upper_letter': 0,
        'lower_letter': 0,
        'punctuation_marks': 0,
        'space': 0,
        'digit': 0,
        'characters': len(text)
    }

    for char in text:
        if char.isupper():
            text_analysis['upper_letter'] += 1
        elif char.islower():
            text_analysis['lower_letter'] += 1
        elif char.isdigit():
            text_analysis['digit'] += 1
        elif char.isspace():
            text_analysis['space'] += 1
        if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`´{|}~":
            text_analysis['punctuation_marks'] += 1

    return text_analysis


def print_text_analysis(text_analysis):
    """
    This function prints the text analysis
    """

    print("The text contains: {} characters"
          .format(text_analysis['characters']))
    print(" - {} upper letters".format(text_analysis['upper_letter']))
    print(" - {} lower letters".format(text_analysis['lower_letter']))
    print(" - {} punctuation marks".format(text_analysis['punctuation_marks']))
    print(" - {} spaces".format(text_analysis['space']))
    print(" - {} digits".format(text_analysis['digit']))


def main():
    """
    This function is the main function
    Checks if the text is provided as an argument
    If not, it asks the user to enter a text
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 1:
            try:
                text = input("Enter a text: What is the text to count?\n")
                text += ' '
            except EOFError:
                return
            except KeyboardInterrupt:
                return
        else:
            text = sys.argv[1]
        text_analysis = analysis_text(text)
        print_text_analysis(text_analysis)

    except AssertionError as e:
        print("AssertionError: {}".format(e))


if __name__ == "__main__":
    main()
