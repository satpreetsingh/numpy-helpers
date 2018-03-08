import pprint

import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

dy, dx = np.gradient(img.astype(float))

plt.figure(figsize=(12, 6))
plt.suptitle("Central Differences Approximation")

plt.subplot(131); plt.imshow(img, cmap="gray"); plt.axis("off"); plt.title("Original")

plt.subplot(132); plt.imshow(dy, cmap="gray"); plt.axis("off"); plt.title("dy")

plt.subplot(133); plt.imshow(dx, cmap="gray"); plt.axis("off"); plt.title("dx")

plt.show()
