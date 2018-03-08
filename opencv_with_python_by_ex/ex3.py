import cv2

img = cv2.imread("../images/example.png")
colorspace_changed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray color image", colorspace_changed)
cv2.waitKey(-1)
