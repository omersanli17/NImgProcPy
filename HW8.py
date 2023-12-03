# Image gradient is the directional change in the intensity or color in an image.
# Gradients can be calculated in specific directions, such as vertical or horizontal.
# Rate of change is derivative of the image

'''
Sobel operator 
Sobel operator is a discrete differentiation operator. 
It computes an approximation of the gradient of the image intensity function.
'''

import cv2 
import numpy as np
import matplotlib.pyplot as plt


def show(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(6,6))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

# Q: 0 mean in img is read as grayscale
img = cv2.imread('Assets/sudoku.jpg',0)
show(img)

# Second parameter is the desired depth of the destination image.
# Depth is the precision of the image, 8 bit, 16 bit, 32 bit float etc.
# dx and dy is the derivative order in x and y respectively.
# ksize is the size of the extended Sobel kernel, it must be 1,3,5 or 7

sobelx = cv2.Sobel(img,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
show(sobelx)

sobely = cv2.Sobel(img,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
show(sobely)

# Laplacian operator is a second order derivative mask
# It calculates differences in both x and y directions
# It is more sensitive to noise
# It is used for edge detection

laplacian = cv2.Laplacian(img,ddepth=cv2.CV_64F)
show(laplacian)

blended = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
show(blended)

ret, th1 = cv2.threshold(blended,100,255,cv2.THRESH_BINARY)
show(th1)

kernel = np.ones(shape=(4,4),dtype=np.uint8)
gradient = cv2.morphologyEx(blended,cv2.MORPH_GRADIENT,kernel)
show(gradient)