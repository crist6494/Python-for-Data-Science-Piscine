def square(x: int | float) -> int | float:
    """Function to calculate the square of a number"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Function to calculate the power of a number"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Function that returns the inner function.
        The result of this function depends of the value of count.
    """

    count = 0

    def inner() -> float:
        """
        Inner function that calculates the result of the function passed in
        the outer function. The result is calculated based on count value.
        variable (nonlocal) count accumulates the value of the function result.
        """

        nonlocal count
        count = function(count if count > 0 else x)
        return count
    return inner
