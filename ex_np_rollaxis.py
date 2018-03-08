from utils import *

gray_img = cv2.imread("rubiks1.jpeg")
print(gray_img.shape)
# Changes the rows to columns.
img2 = np.rollaxis(gray_img, 1)
print(img2.shape)
opencv2_showimg("gray", img2)

# this will crash.
# why?
img3 = np.rollaxis(gray_img, 2)
print(img3.shape)
opencv2_showimg("img3", img3)

