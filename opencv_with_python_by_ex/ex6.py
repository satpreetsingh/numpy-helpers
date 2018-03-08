import numpy as np
import cv2

rubiks1 = cv2.imread("../images/rubiks1.jpeg")
rows, cols = rubiks1.shape[:2]

# The translation matrix should be
# x y delta
# 80 is cols
# 100 is rows

translation_matrix = np.float32([
    [1, 0, 80],
    [0, 1, 100]])


translated_matrix = cv2.warpAffine(rubiks1, translation_matrix, (cols + 80, rows + 100))

translation_matrix2 = np.float32([
    [1, 0, -40],
    [0, 1, -50]])

centered_translated_matrix = cv2.warpAffine(translated_matrix, translation_matrix2, (cols + (40+ 80), rows + (50 +
                                                                                                              100)))

cv2.imshow("affine wrapped", centered_translated_matrix)
cv2.waitKey(-1)
