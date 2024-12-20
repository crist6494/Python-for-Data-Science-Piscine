from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: <funtion {function.__name__} at"
                      f"{hex(id(function))}> call to many times")
        return limit_function
    return callLimiter
