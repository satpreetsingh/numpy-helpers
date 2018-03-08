import cv2
import matplotlib.pyplot as plt
import numpy as np

color_img = cv2.imread("rubiks2.jpg", cv2.IMREAD_COLOR)

channels = blue, green, red = np.rollaxis(color_img, 2)

# Matplot lib window size in inches.
# columns vs rows
# width, height
plt.figure(figsize=(12, 4))

plt.subplot(131); plt.imshow(channels[0], cmap="gray"); plt.axis("off"); plt.title("Blue Channel")
plt.subplot(132); plt.imshow(channels[1], cmap="gray"); plt.axis("off"); plt.title("Green Channel")
plt.subplot(133); plt.imshow(channels[2], cmap="gray"); plt.axis("off"); plt.title("Red Channel")
plt.show()

# why is the channel information light in color.
