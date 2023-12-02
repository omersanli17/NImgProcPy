'''
Gamma is an important but seldom understood characteristic of virtually all digital imaging systems.
It defines the relationship between a pixel's numerical value and its actual luminance
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Write a function that read the image as RGB in 'Assets' folder with name, 
# also take imread by .astype(np.float32) / 255 to get between 0 and 1

def readRGB(imageName):
    img = cv2.imread('Assets/'+imageName).astype(np.float32) / 255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

# Write a function that show the image with plt.imshow and plt.show() commands

def show(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(6,6))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

image = readRGB('bricks.jpg')
show(image)

# Higher gamma value will darken the image, and a lower gamma value will brighten it.
gamma = 1/4

# It takes the image and raises it to the power of gamma
result = np.power(image,gamma)
show(result)

# Create a font HERSHEY_COMPLEX
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image, text='bricks', org=(10,600), fontFace=font, fontScale=10, color=(255,0,0), thickness=4, lineType=cv2.LINE_AA)
show(image)

# 0.04 every value 
kernel = np.ones(shape=(5,5),dtype=np.float32)/25

# The function convolves the source image with the specified kernel.
# -1 means that the output image will have the same depth as the source.
# Depth is the number of channels in an image.

destination = cv2.filter2D(image,-1,kernel)
show(destination)

# Blur the image with cv2.blur
blur = cv2.blur(image,ksize=(5,5))
show(blur)


# Displaying Kernel.gif to understand kernel size 

from SubOperatorSample.GIFLoading import show_loading_gif

if __name__ == "__main__":
    gif_file_name = "kernel"  # Replace with the desired GIF file name without extension
    show_loading_gif(gif_file_name)
