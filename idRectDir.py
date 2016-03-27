import numpy as np
import cv2
from matplotlib import pyplot as plt

#------------------------------------------------------------------
# do the processing for the vertical rectangle
#------------------------------------------------------------------

# load the image of the vetical rectangle
img = cv2.imread('rectVert.jpg',0)

# invert the binary image
img = cv2.bitwise_not(img)

# threshold the image
ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# show the image
imgplot = plt.imshow(img,cmap = 'gray', interpolation = 'bicubic')
plt.show()

# find the contours to the image
_,contours,hierarchy = cv2.findContours(img, 1, 2)

# extract the first contour and the moments of the first contour
cnt = contours[0]
M = cv2.moments(cnt)


# calculate the centroid and print
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print 'cx : ' + str(cx)
print 'cy : ' + str(cy)

# print the moments
print 'm01 : ' + str(M['m01'])
print 'm10 : ' + str(M['m10'])
print 'm02 : ' + str(M['m02'])
print 'm20 : ' + str(M['m20'])

# calculate the area and print the result
area = cv2.contourArea(cnt)
print 'Area :' + str(area)


# draw the 1 st contour on the image and show
cv2.drawContours(img,contours,0,(128,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#------------------------------------------------------------------
# do the processing for the horizontal rectangle
#------------------------------------------------------------------


# load an color image in grayscale
img2 = cv2.imread('rectHoriz.jpg',0)


# invert the binary image
img2 = cv2.bitwise_not(img2)


# threshold the image
ret,img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)


# show the image
imgplot = plt.imshow(img2,cmap = 'gray', interpolation = 'bicubic')
plt.show()


# find the contours to the image
_,contours,hierarchy = cv2.findContours(img2, 1, 2)

# extract the first contour and the moments of the first contour
cnt = contours[0]
M = cv2.moments(cnt)


# calculate the centroid and print
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print 'cx : ' + str(cx)
print 'cy : ' + str(cy)

# print the moments
print 'm01 : ' + str(M['m01'])
print 'm10 : ' + str(M['m10'])
print 'm02 : ' + str(M['m02'])
print 'm20 : ' + str(M['m20'])


# calculate the area and print the result
area = cv2.contourArea(cnt)
print 'Area :' + str(area)

# draw the 1 st contour on the image and show
cv2.drawContours(img2,contours,0,(128,25,0),3)
cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

