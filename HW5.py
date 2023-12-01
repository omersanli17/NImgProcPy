import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the image in Assets folder and convert it to grayscale
img = cv2.imread('Assets/kerem.jpeg',0)
plt.imshow(img,cmap='gray')
plt.show()

# Define what threshold do in opencv and give example code
# Thresholding is the assignment of pixel values in relation to the threshold value provided.
# Any values below the threshold are set to 0, and values above the threshold are set to a maximum value.

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
print(ret)
print(thresh1)
plt.imshow(thresh1,cmap='gray')
plt.show()

'''
THRESH_TRUNC: If pixel intensity value is greater than a threshold value, it is assigned to a new value.
THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0.
THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
'''
 # Read crossword image
img2 = cv2.imread('Assets/crossword.jpg',0)

# Define a function taht show the image 
def show(img):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

show(img2)

ret, th1 = cv2.threshold(img2, 180, 255, cv2.THRESH_BINARY)
show(th1)

'''
// Parameters:  
// src: Source Image
// maxValue: Maximum Value
// adaptiveMethod: Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C
// thresholdType: Thresholding type, THRESH_BINARY or THRESH_BINARY_INV
// blockSize: Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on. (Odd numbers only)
// C: Constant subtracted from the mean or weighted mean. Normally, it is positive but may be zero or negative as well.
'''
th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)

show(th2)

# Blend two images with different weights
blended = cv2.addWeighted(src1=th1,alpha=0.6,src2=th2,beta=0.4,gamma=0)
show(blended)