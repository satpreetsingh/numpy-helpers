import cv2

img = cv2.imread("../images/rubiks1.jpeg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("rubiks original", img)

# CV_64F means double and not float
# dx is horizontal - sane
# dy is vertical - sane
horizontal_sobel = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
vertical_sobel = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow("Horizontal Sobel", horizontal_sobel)
cv2.imshow("Veritical Sobel", vertical_sobel)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow("Laplacian", laplacian)

# Since grayscale image, the thresholds of 50 and 240 are fine for detecting the edges.
canny = cv2.Canny(img, 50, 240)

cv2.imshow("Canny", canny)

cv2.waitKey(-1)


