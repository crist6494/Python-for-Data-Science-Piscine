import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    np_weight = np.array(weight)
    np_height = np.array(height)

    assert np_height.size == np_weight.size, "The size must by be the same"
    assert (np.issubdtype(np_height.dtype, np.integer)
            or np.issubdtype(np_height.dtype, np.floating)), "Type must be integer o float"
    assert (np.issubdtype(np_weight.dtype, np.integer)
            or np.issubdtype(np_weight.dtype, np.floating)), "Type must be integer o float"
    
    bmi = np_weight / np_height**2

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(limit, int):
        raise AssertionError("Type must be integer")
    
    np_list = np.array(bmi)

    assert (np.issubdtype(np_list.dtype, np.integer)
            or np.issubdtype(np_list.dtype, np.floating)), "Type must be integer o float"
    result = np_list > limit
    return result.tolist()

try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 0))
except AssertionError as e:
    print("Assertion error: {}".format(e))