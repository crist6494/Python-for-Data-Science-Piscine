from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Function to calculate the mean, median, quartile, 
        variance and standard deviation of a list of numbers
    """

    def mean(*args: Any) -> float:
        """Function to calculate the mean of a list of numbers"""
        return sum(args) / len(args)

    def median(*args: Any) -> float:
        """Function to calculate the median of a list of numbers"""
        args = sorted(args)
        n = len(args)

        median_index = n // 2
        median = ((args[median_index] + args[median_index - 1]) / 2
                  if n % 2 == 0 else args[median_index])

        return median

    def quartile(*args: Any) -> list[float]:
        """Function to calculate the quartile of a list of numbers"""
        args = sorted(args)
        n = len(args)

        q1_index = n // 4
        q3_index = 3 * n // 4

        q1 = float((args[q1_index - 1] + args[q1_index]) / 2
                   if n % 4 == 0 else args[q1_index])
        q3 = float((args[q3_index - 1] + args[q3_index]) / 2
                   if (3 * n) % 4 == 0 else args[q3_index])

        return [q1, q3]

    def variance(*args: Any) -> float:
        """Function to calculate the variance of a list of numbers"""
        mean_value = mean(*args)
        return sum((i - mean_value) ** 2 for i in args) / len(args)

    def std(*args: Any) -> float:
        """Function to calculate the standard deviation of a list of numbers"""
        return variance(*args) ** 0.5

    numbers = [i for i in args if isinstance(i, int)]
    if len(numbers) != len(args):
        print("ERROR: the arguments must be integers")
        return

    if not numbers:
        for i in kwargs.values():
            print("ERROR")
        return

    for i in kwargs.values():
        match i:
            case "mean":
                print(f"mean : {mean(*args)}")
            case "median":
                print(f"median: {median(*args)}")
            case "quartile":
                print(f"quartile: {quartile(*args)}")
            case "std":
                print(f"std : {std(*args)}")
            case "var":
                print(f"var : {variance(*args)}")
