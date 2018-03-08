import pprint

import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

sub_img = img[::10, ::10]

res_img = cv2.resize(img, sub_img.shape[::-1])

pprint.pprint(sub_img.shape)
pprint.pprint(res_img.shape)


bs_img = cv2.GaussianBlur(img, ksize=(13, 13), sigmaX=2.5)[::10, ::10]

interp_img = cv2.resize(img, sub_img.shape[::-1], interpolation=cv2.INTER_AREA)

plt.figure(figsize=(12, 4));
plt.subplot(141); plt.imshow(img, cmap="gray"); plt.axis("off"); plt.title("Original");
plt.subplot(142); plt.imshow(sub_img, cmap="gray"); plt.axis("off"); plt.title("Subsampled");
plt.subplot(143); plt.imshow(bs_img, cmap="gray"); plt.axis("off"); plt.title("Blur + Subsampled");
plt.subplot(144); plt.imshow(interp_img, cmap="gray"); plt.axis("off"); plt.title("cv2.resize - Area Interpolation");

plt.show()
