import cv2
import numpy as np
import scipy as sp

import matplotlib as mpl
import matplotlib.pyplot as plt


def opencv2_showimg(title, _img):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, _img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mp_showimg(img):
    plt.imshow(img)
    plt.axis("off")
    plt.title("Image")
    plt.show()


def mp_showimg_gray(img):
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.title("Image")
    plt.show()
