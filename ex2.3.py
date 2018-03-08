import cv2
import matplotlib.pyplot as plt


color_img = cv2.imread("example.png", cv2.IMREAD_COLOR)  # reload the sample image

color_img = color_img.astype(float)

bluePlusGreen = color_img[:, :, 0] + color_img[:, :, 1]
redTimesBlue = color_img[:, :, 2] * color_img[:, :, 0]
greenMinusRed = color_img[:, :, 1] - color_img[:, :, 2]

plt.figure(figsize=(12, 6))

plt.subplot(131); plt.imshow(bluePlusGreen, cmap="gray"); plt.axis("off"); plt.title("Sum")
plt.subplot(132); plt.imshow(redTimesBlue, cmap="gray"); plt.axis("off"); plt.title("Product")
plt.subplot(133); plt.imshow(greenMinusRed, cmap="gray"); plt.axis("off"); plt.title("Difference")

plt.show()
