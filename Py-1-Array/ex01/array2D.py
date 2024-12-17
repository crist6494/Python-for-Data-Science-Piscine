import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on
    the provided start and end arguments with the slice method.
    """

    np_family = np.array(family)

    assert isinstance(family, list), "Input must be a list."

    assert (isinstance(start, int) and isinstance(end, int)), \
        "Start and end must be integers."

    assert np_family.ndim == 2, "Input must be a 2D list."

    print("My shape is {}".format(np_family.shape))
    truncated_family = np_family[start:end]
    print("My new shape is {}".format(truncated_family.shape))
    return truncated_family.tolist()
