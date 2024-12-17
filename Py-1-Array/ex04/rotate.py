import load_image as li
import cv2
import numpy as np


def main():
    """
    Load an image, print information, and display it rotated.
    """

    try:
        img_rgb = li.ft_load("animal.jpeg")
        zoomed_img = img_rgb[100:500, 450:850, :1]
        print(f"The shape of image is: {zoomed_img.shape} "
              f"or {zoomed_img.shape[:2]}")
        print(zoomed_img)

        img_rotated = np.zeros((zoomed_img.shape[1], zoomed_img.shape[0]),
                               dtype=zoomed_img.dtype)
        for i in range(zoomed_img.shape[0]):
            for j in range(zoomed_img.shape[1]):
                img_rotated[j, i] = zoomed_img[i, j]

        print(f"New shape after Transpose: {img_rotated.shape}")
        print(img_rotated)

        img_rotated_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
        cv2.imshow("Rotated Image", img_rotated_rgb)
        cv2.moveWindow("Rotated Image", 600, 200)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except AssertionError as e:
        print(f"Assertion error: {e}")


if __name__ == "__main__":
    main()
