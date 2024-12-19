from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:

    def mean(*args: Any) -> float:
        return sum(args) / len(args)

   
    def median(*args: Any) -> float:
        args = sorted(args)
        n = len(args)
        if(n == 0):
            return 0
        median_index = n // 2
        return (args[median_index] + args[median_index - 1]) / 2 if n % 2 == 0 else args[median_index]


    def quartile(*args: Any) -> list[float]:
        args = sorted(args)
        n = len(args)
        if(n == 0):
            return [0, 0]

        q1_index = (n + 1) // 4
        q3_index = (3 * (n + 1)) // 4

        q1 = (args[q1_index - 1] + args[q1_index]) / 2 if n % 4 == 0 else args[q1_index - 1]
        q3 = (args[q3_index - 1] + args[q3_index]) / 2 if (3 * n) % 4 == 0 else args[q3_index - 1]

        return [q1, q3]

    def variance(*args: Any) -> float:
        if len(args) == 0:
            return 0
        mean_value = mean(*args)
        return sum((i - mean_value) ** 2 for i in args) / len(args)


    def std(*args: Any) -> float:
        return variance(*args) ** 0.5


    numbers = [i for i in args if isinstance(i, (int, float))]
    print(numbers)
    if not numbers:
        for i in kwargs.values():
            print("ERROR")
        return
    
    for i in kwargs.values():
        match i:
            case "mean":
                print(f"mean : {mean(numbers)}")
            case "median":
                print(f"median: {median(numbers)}")
            case "quartile":
                print(f"quartile: {quartile(numbers)}")
            case "std":
                print(f"std : {std(numbers)}")
            case "var":
                print(f"var : {variance(numbers)}")
         