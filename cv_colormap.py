import cv2

img = cv2.imread("images/rubiks1.jpeg", 1)
assert img is not None
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
jet_colormap = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)

super_imposed = cv2.addWeighted(jet_colormap, 0.7, img, 0.3, 0)

cv2.imshow("colormap.jpg", jet_colormap)
cv2.imshow("superimposed", super_imposed)
cv2.waitKey(-1)
