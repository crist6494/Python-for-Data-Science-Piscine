import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Takes as parameters a list of heights and a list of weights
    and returns a list of BMIs
    """

    np_weight = np.array(weight)
    np_height = np.array(height)

    assert np_height.size == np_weight.size, "The size must be the same"

    assert (np.issubdtype(np_height.dtype, np.integer) or
            np.issubdtype(np_height.dtype, np.floating)), \
           "Type must be integer or float"

    assert (np.issubdtype(np_weight.dtype, np.integer) or
            np.issubdtype(np_weight.dtype, np.floating)), \
           "Type must be integer or float"

    bmi = np_weight / (np_height**2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Takes as parameters a list of BMIs and a limit
    and returns a list of booleans indicating whether
    each BMI is above the limit
    """

    if not isinstance(limit, int):
        raise AssertionError("Type must be integer")

    np_list = np.array(bmi)

    assert (np.issubdtype(np_list.dtype, np.integer) or
            np.issubdtype(np_list.dtype, np.floating)), \
           "Type must be integer or float"

    result = np_list > limit
    return result.tolist()
