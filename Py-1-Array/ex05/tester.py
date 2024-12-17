import numpy as np
import load_image as li
import pimp_image as pi

array = li.ft_load("landscape.jpg")
pi.ft_invert(array)
pi.ft_red(array)
pi.ft_green(array)
pi.ft_blue(array)
pi.ft_grey(array)
print(pi.ft_invert.__doc__)