from load_image import ft_load

try:
    print(ft_load("landscape.jpg"))
except AssertionError as e:
    print("Assertion error: {}".format(e))