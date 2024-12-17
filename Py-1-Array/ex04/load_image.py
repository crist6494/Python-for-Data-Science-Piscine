import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Takes as parameter a path to an image file
    and loads an image, prints its format, and returns the image
    """

    assert path.lower().endswith(('.jpg', '.jpeg')), \
        "The file must be a jpg or jpeg file"

    img = cv2.imread(path)
    assert img is not None, "The file does not exist"

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img
