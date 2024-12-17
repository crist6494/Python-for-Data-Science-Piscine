import numpy as np
import cv2


def create_window(name: str, array: np.array) -> None:
    """
    Create a window with the name and the image received
    """

    array = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
    cv2.imshow(f"{name}", array)
    cv2.moveWindow(f"{name}", 600, 200)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ft_invert(array) -> np.array:
    """
    Inverts the colors of the image received
    """

    np_copy = np.copy(array)
    np_copy = 255 - np_copy
    create_window("Inverted", np_copy)


def ft_red(array) -> np.array:
    """
    Keep only the red color of the image received
    """

    np_copy = np.copy(array)
    np_copy[:, :, 1] = 0
    np_copy[:, :, 2] = 0
    create_window("Red", np_copy)


def ft_green(array) -> np.array:
    """
    Keep only the green color of the image received
    """

    np_copy = np.copy(array)
    np_copy[:, :, 0] = 0
    np_copy[:, :, 2] = 0
    create_window("Green", np_copy)


def ft_blue(array) -> np.array:
    """
    Keep only the blue color of the image received
    """

    np_copy = np.copy(array)
    np_copy[:, :, 0] = 0
    np_copy[:, :, 1] = 0
    create_window("Blue", np_copy)


def ft_grey(array) -> np.array:
    """
    Convert the image received to grey
    """

    np_copy = np.copy(array)
    np_copy = (np_copy[:, :, 0] // 3 + np_copy[:, :, 1] // 3
               + np_copy[:, :, 2] // 3)
    create_window("Grey", np_copy)
