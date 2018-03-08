import pprint

import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)


plt.figure(figsize=(12, 6));
plt.suptitle("Sobel Approximation")
plt.subplot(131); plt.imshow(img, cmap="gray"); plt.axis("off"); plt.title("Original");
plt.subplot(132); plt.imshow(dy, cmap="gray"); plt.axis("off"); plt.title("dy");
plt.subplot(133); plt.imshow(dx, cmap="gray"); plt.axis("off"); plt.title("dx");

plt.show()
