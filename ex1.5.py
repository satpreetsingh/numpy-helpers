import cv2
import matplotlib.pyplot as plt
import numpy as np

color_img = cv2.imread("example.png", cv2.IMREAD_COLOR)

channels = blue, green, red = np.rollaxis(color_img, 2)

"""
OpenCV Error: Unspecified error (could not find a writer for the specified extension) in imwrite_, file 
"""

cv2.imwrite("blue.senthil", blue)
cv2.imwrite("green.png", green)
cv2.imwrite("red.png", red)
