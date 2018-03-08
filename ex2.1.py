import pprint

import cv2

import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)

print "Shape of you ", img.shape
print "Image type:", type(img)
print "Pixels are represented by unsigned 8-bit values:", img.dtype

# Example ndarray object properties

img_dims = img.ndim
img_shape = img.shape
img_size = img.size

print(img_dims)

# What is this type of format specifier?
print "\n{:^70}".format("NDARRAY ATTRIBUTES")
print "{:^70}\n".format("====================")
print "{:^30}{:^20}{:^20}".format("Description", "Example", "Value")
print "{:^30}{:^20}{:^20}".format("-------------", "---------", "-------")
print "{:^30}{:^20}{:^20}".format("Number of dimensions", "img.ndim", img_dims)
print "{:^30}{:^20}{:^20}".format("Image Shape", "img.shape", img_shape)
print "{:^30}{:^20}{:^20}".format("Pixel Count", "img.size", img_size)

print "What is the difference between Basic indexing and Better Indexing?"

print "Although you can use multiple slices for each axis, it is better to combine the indices to a single slice."

print "Using multiple slices incurs the overhead of parsing the indexes for every pair of brackets."

print img[37][73]
print img[37, 73]

pprint.pprint(img[0:3, img.shape[1]-4: img.shape[1]])
pprint.pprint(img[:3, -4:])

print "Original img.shape", img.shape
print "Shape of the first column of pixels (all rows, column 0): ", img[:, 0].shape
print "Shape of the first row of pixels (row 0, all columns):", img[0, :].shape

# Index arrays

rows = [0, 2, 4, 6, 8]
cols = [1, 3, 5, 7, 9]

print "rows = ", rows
print "cols = ", cols
print "img[rows, cols] =", img[rows, cols]


mask = np.zeros(img.shape, dtype=bool)
mask[:3, :4] = True

pprint.pprint(img[mask])

pprint.pprint(img[img > 230])

# Basic Methods

print "Minimum pixel intensity ", img.min()
print "Maximum pixel intensity ", img.max()
print "Mean pixel intensity ", img.mean()
print "Cumulative pixel intensity ", img.sum()

# How does the axis work?
# axis is tricky.
# https://stackoverflow.com/questions/17079279/how-is-axis-indexed-in-numpys-array
print "maximum column sum: ", img.sum(axis=0, dtype=float).max()

img64 = img.astype(np.float64)

print "old type: ", img.dtype
print "new type: ", img64.dtype

img3d = np.atleast_3d(img)

# equivalent to img[:, :, np.newaxis]

print "old shape: ", img.shape
print "new shape: ", img3d.shape

