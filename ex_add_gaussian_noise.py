import pprint

import cv2
import numpy as np

import matplotlib.pyplot as plt


def add_gaussian_noise(img):
    row, col, ch = img.shape
    mean = 0
    var = 0.0001
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = img + gauss
    return noisy

def add_guassian_noise_2d(img):
    row, col = img.shape
    mean = 0
    var = 1000
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    noisy = img + gauss
    return noisy


def add_sp_noise(img):
    #row,col,ch = img.shape
    s_vs_p = 0.5
    amount = 0.004
    out = img
    # Salt mode
    num_salt = np.ceil(amount * img.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in img.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in img.shape]
    out[coords] = 0
    return out


def add_gaussian_noise(image_in, noise_sigma):
    temp_image = np.float64(np.copy(image_in))

    h = temp_image.shape[0]
    w = temp_image.shape[1]
    noise = np.random.randn(h, w) * noise_sigma

    noisy_image = np.zeros(temp_image.shape, np.float64)
    if len(temp_image.shape) == 2:
        noisy_image = temp_image + noise
    else:
        noisy_image[:,:,0] = temp_image[:,:,0] + noise
        noisy_image[:,:,1] = temp_image[:,:,1] + noise
        noisy_image[:,:,2] = temp_image[:,:,2] + noise

    """
    print('min,max = ', np.min(noisy_image), np.max(noisy_image))
    print('type = ', type(noisy_image[0][0][0]))
    """

    return noisy_image

def show_gaussian_rubiks():
    img = cv2.imread("../rubiks2.jpg", cv2.IMREAD_COLOR)
    channels = blue, green, red = np.rollaxis(img, 2)
    rgb_img = np.dstack([red, green, blue])
    noisy_rgb_img = add_gaussian_noise(rgb_img)
    plt.imshow(noisy_rgb_img)
    plt.title("Rubiks2")
    plt.show()


def show_single_pixel_img():
    img = np.zeros((10, 10), dtype=np.uint8)
    img[:] = 130
    pprint.pprint(img)
    plt.imshow(img)
    plt.title("Single pixel value")
    plt.show()
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    noisy = add_gaussian_noise(img, 350)
    plt.imshow(noisy); plt.show()
    plt.hist(noisy.ravel(),256,[0,256]); plt.show()


def show_single_pixel_img_add_sp():
    img = np.zeros((10, 10), dtype=np.uint8)
    img[:] = 130
    pprint.pprint(img)
    plt.imshow(img)
    plt.title("Single pixel value")
    plt.show()
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    noisy = add_sp_noise(img)
    plt.imshow(noisy); plt.show()
    plt.hist(noisy.ravel(),256,[0,256]); plt.show()


def add_gaussian_grayscale():
    img = cv2.imread("../rubiks2.jpg", cv2.IMREAD_GRAYSCALE)
    pprint.pprint(img)
    plt.imshow(img, cmap="gray")
    plt.title("Single pixel value")
    plt.show()
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    noisy = add_guassian_noise_2d(img)
    plt.imshow(noisy, cmap="gray"); plt.show()
    plt.hist(noisy.ravel(),256,[0,256]); plt.show()


if __name__ == '__main__':
    show_single_pixel_img_add_sp()
