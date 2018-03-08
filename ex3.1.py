import pprint

import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(24, 6))

plt.subplot(141); plt.imshow(img, cmap="gray"); plt.axis("off"); plt.title("Original");
plt.subplot(142); plt.imshow(img.T, cmap="gray"); plt.axis("off"); plt.title("Transpose");
plt.subplot(143); plt.imshow(np.fliplr(img), cmap="gray"); plt.axis("off"); plt.title("Flip Horizontal");
plt.subplot(144); plt.imshow(np.flipud(img), cmap="gray"); plt.axis("off"); plt.title("Flip Vertical");

plt.show()
