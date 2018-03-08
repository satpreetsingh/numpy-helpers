import cv2
import matplotlib.pyplot as plt
import numpy as np

color_img = cv2.imread("example.png", cv2.IMREAD_COLOR)

channels = blue, green, red = np.rollaxis(color_img, 2)

plt.imshow(color_img)
plt.axis("on")
plt.title("Color Buzz")
plt.show()


