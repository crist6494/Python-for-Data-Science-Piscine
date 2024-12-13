import sys
from ft_filter import ft_filter


def check_special_chars(string: str) -> bool:
    """
    Check if the string contains special characters
    """

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
                  0123456789 ")
    return any(char not in allowed_chars for char in string)


def generatList(string: str, size: int) -> list:
    """
    Generate a list of words that are longer than the size
    """
    array = string.split(' ')
    return list(ft_filter(lambda x: len(x) > size, array))


def main():
    """
    This function is the main function
    Checks the arguments and calls the generatList function
    """
    try:
        if (len(sys.argv) != 3) or (not sys.argv[2].isdigit()):
            raise AssertionError("the arguments are bad")
        if (check_special_chars(sys.argv[1])):
            raise AssertionError("the arguments are bad")
        print(generatList(sys.argv[1], int(sys.argv[2])))
    except AssertionError as e:
        print("AssertionError: {}".format(e))


if __name__ == "__main__":
    main()
