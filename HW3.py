# Blended images by openCV formula = alpha * img1 + beta * img2 + gamma
# The gamma value of blended images by openCV formula defined as scalar added to each sum
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in RGB Mode 
swiftImg = cv2.imread('DATA/adv.jpeg')
shutterImg = cv2.imread('DATA/shutter.webp')

# Convert the image from BGR to RGB
swiftImg = cv2.cvtColor(swiftImg, cv2.COLOR_BGR2RGB)
shutterImg = cv2.cvtColor(shutterImg, cv2.COLOR_BGR2RGB)

# Resize the images
swiftImg = cv2.resize(swiftImg, (600, 600))
shutterImg = cv2.resize(shutterImg, (600, 600))

# Blending the images, alpha = 0.5, beta = 0.5, gamma = 0. Alpha stands for the weight of the first array elements and beta stands for the weight of the second array elements.
blendedImg = cv2.addWeighted(src1=swiftImg, alpha=0.5, src2=shutterImg, beta=0.5, gamma=0)

# Display the blended image
plt.imshow(blendedImg)
plt.show()

# Displaying blended images with different sizes will not work ( ERR: Sizes of input arguments do not match)

"""
swiftImg = cv2.imread('DATA/adv.jpeg')
shutterImg = cv2.imread('DATA/shutter.webp')

swiftImg = cv2.cvtColor(swiftImg, cv2.COLOR_BGR2RGB)
shutterImg = cv2.cvtColor(shutterImg, cv2.COLOR_BGR2RGB)

# Resize the only shutter image, swiftImg will be the larger image
shutterImg = cv2.resize(shutterImg, (100, 100))

# Blending the images, alpha = 0.5, beta = 0.5, gamma = 0. Alpha stands for the weight of the first array elements and beta stands for the weight of the second array elements.
blendedImg = cv2.addWeighted(src1=swiftImg, alpha=0.5, src2=shutterImg, beta=0.5, gamma=0)

# Display the blended image
plt.imshow(blendedImg)
plt.show()
"""

# Read Images in RGB Mode
swiftImg2 = cv2.imread('DATA/adv.jpeg')
shutterImg2 = cv2.imread('DATA/shutter.webp')

swiftImg2 = cv2.cvtColor(swiftImg2, cv2.COLOR_BGR2RGB)
shutterImg2 = cv2.cvtColor(shutterImg2, cv2.COLOR_BGR2RGB)

# Resize the images
shutterImg2 = cv2.resize(shutterImg2, (300, 300))

# Set the small images' starting position that will be placed on the larger image
xOffset = 0
yOffset = 0

# Set the small images' ending position that will be placed on the larger image
xEnd = xOffset + shutterImg2.shape[1]
yEnd = yOffset + shutterImg2.shape[0]

# Place the small image on the larger image
swiftImg2[yOffset:yEnd, xOffset:xEnd] = shutterImg2

# Display the image
plt.imshow(swiftImg2)
plt.show()