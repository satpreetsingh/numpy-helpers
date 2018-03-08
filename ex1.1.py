import time
import cv2
import numpy as np
import scipy as sp

import matplotlib as mpl
import matplotlib.pyplot as plt

from utils import opencv2_showimg

"""
Q: What happens when the name of the image file doesn't exist?
A: Nothing

Q: Does OpenCV raise an error?
A: No

Q: What value does the variable take?
A: None
"""
gray_img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

# why the default is the Blue color?

plt.imshow(gray_img, cmap="gray")
# why should I have to use a different program (plt) and set the color map to gray here?
plt.axis("on")
plt.title("Grayscale Buzz")
plt.show()

"""
Q: What is the default color space for the images in Open CV?
A: BGR

"""
