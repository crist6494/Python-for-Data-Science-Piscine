import load_image as li
import cv2


def main():
    """
    Load an image, print information, and display it zoomed.
    """

    try:
        img_rgb = li.ft_load("animal.jpeg")
        print(f"The shape of image is: {img_rgb.shape} ")
        print(img_rgb)

        zoomed_img = img_rgb[100:500, 450:850, :1]
        print(f"New shape after slicing: {zoomed_img.shape} "
              f"or {zoomed_img.shape[:2]}")
        print(zoomed_img)

        zoomed_img_rgb = cv2.cvtColor(zoomed_img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Zoomed Image", zoomed_img_rgb)
        cv2.moveWindow("Zoomed Image", 600, 200)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except AssertionError as e:
        print(f"Assertion error: {e}")


if __name__ == "__main__":
    main()
