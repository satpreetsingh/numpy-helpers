import cv2
import matplotlib.pyplot as plt
import numpy as np

color_img = cv2.imread("example.png", cv2.IMREAD_COLOR)

channels = blue, green, red = np.rollaxis(color_img, 2)

rgb_img = np.dstack([red, green, blue])

plt.imshow(rgb_img)
plt.axis("off")
plt.title("Color Buzz (Corrected)")

plt.show()
