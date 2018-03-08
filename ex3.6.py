import cv2
import numpy as np

import matplotlib.pyplot as plt

# generate a test image
vals = cv2.getGaussianKernel(9, 1.5)

img = (cv2.normalize(vals * np.rollaxis(vals, 1), alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)).astype(np.uint8)

# make a copy of the original that shares the same scale as the outputs -- the white border
# will not appear in the jupyter notebook
_img = cv2.copyMakeBorder(img, 4, 4, 4, 4, borderType=cv2.BORDER_CONSTANT, value=255)

#
zPadded = cv2.copyMakeBorder(img, 4, 4, 4, 4, borderType=cv2.BORDER_CONSTANT, value=127)
rPadded = cv2.copyMakeBorder(img, 4, 4, 4, 4, borderType=cv2.BORDER_REFLECT)
r101Padded = cv2.copyMakeBorder(img, 4, 4, 4, 4, borderType=cv2.BORDER_REFLECT_101)

plt.figure(figsize=(12, 6))
plt.subplot(141); plt.imshow(_img, cmap="gray"); plt.axis("off"); plt.title("Original")
plt.subplot(142); plt.imshow(zPadded, cmap="gray"); plt.axis("off"); plt.title("Constant Fill (127)")
plt.subplot(143); plt.imshow(rPadded, cmap="gray"); plt.axis("off"); plt.title("Border Reflect")
plt.subplot(144); plt.imshow(r101Padded, cmap="gray"); plt.axis("off"); plt.title("Border Reflect 101")

plt.show()
