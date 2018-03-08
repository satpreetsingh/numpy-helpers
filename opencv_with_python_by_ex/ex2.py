import cv2

img = cv2.imread("../images/example.png", cv2.IMREAD_COLOR)
cv2.imwrite("../output/example_output.png", img)
