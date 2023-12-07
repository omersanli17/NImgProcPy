import cv2
import matplotlib.pyplot as plt
import numpy as np

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)
    plt.show()

# Open and display the giaraffes.jpg image that is located in the Assets folder.
img = cv2.imread('Assets/giraffes.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
display_img(img)

# Apply a binary threshold onto the image.
img = cv2.imread('Assets/giraffes.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
display_img(thresh1, cmap='gray')

# BGR TO HSV
img = cv2.imread('Assets/giraffes.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
display_img(img)

# 4x4 Kernel
kernel = np.ones((4,4),np.float32)/10
print(kernel)

'''
A low pass filter is the basis for most smoothing methods. 
An image is smoothed by decreasing the disparity between pixel values by averaging nearby pixels
'''
# Create a low pass filter with a 4 by 4 Kernel filled with values of 1/10 (0.01)
# and then use 2-D Convolution to blur the giraffer image (displayed in normal RGB)

img = cv2.imread('Assets/giraffes.jpg') 
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
dst = cv2.filter2D(img,-1,kernel)
display_img(dst)

# Create a Horizontal Sobel Filter
# with a kernel size of 5 to the grayscale version of the giaraffes image
# and then display the resulting gradient filtered version of the image

img = cv2.imread('Assets/giraffes.jpg',0)
display_img(img, cmap='gray')
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_img(sobelx, cmap='gray')

# Plot the color histograms for the RED, BLUE, and GREEN channel of the giaraffe image.
# Pay careful attention to the ordering of the channels

img = cv2.imread('Assets/giraffes.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
color = ('r','g','b')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.title('Color Histogram for Giaraffe')
plt.show()