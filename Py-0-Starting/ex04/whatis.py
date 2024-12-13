import sys


def isOddorEven():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 1:
            return

        try:
            value = int(sys.argv[1])
            if value % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print("AssertionError: {}".format(e))


isOddorEven()
