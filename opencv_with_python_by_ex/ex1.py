import cv2

img = cv2.imread("../images/example.png", cv2.IMREAD_COLOR)
cv2.imshow("Image", img)
cv2.waitKey(-1)
