import numpy as np
import cv2
from matplotlib import pyplot as plt

# create the convolution kernel
kernel = np.ones((6,6),np.uint8)

# load an color image in grayscale
img = cv2.imread('spoon.jpeg',0)

# show the original image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filter the image with an averaging filter
filterImg = cv2.bilateralFilter(img,15,75,75)

# show the average filtered image
cv2.imshow('bilateral',filterImg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# threshold the image to get only the spoon and set as a binary image
threshImg = cv2.adaptiveThreshold(filterImg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# show the thresholded image
cv2.imshow('image2',threshImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# invert the binary image
invImg = cv2.bitwise_not(threshImg)

# erode the inverted image to remove small pixel islands
erodedImg = cv2.erode(invImg,kernel,iterations = 1)

# dilate the eroded image 6 times to make spoon area bigger and pixels connected
dilatedImg = cv2.dilate(erodedImg,kernel,iterations = 1)
dilatedImg = cv2.dilate(dilatedImg,kernel,iterations = 1)
dilatedImg = cv2.dilate(dilatedImg,kernel,iterations = 1)
dilatedImg = cv2.dilate(dilatedImg,kernel,iterations = 1)
dilatedImg = cv2.dilate(dilatedImg,kernel,iterations = 1)
dilatedImg = cv2.dilate(dilatedImg,kernel,iterations = 1)


# show the dilated image
cv2.imshow('image2',dilatedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

