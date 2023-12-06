# RGB ( RED GREEN BLUE ) is the most common way to represent an image.
# HSV and HSL are other ways to represent an image. 
# HSL, the opposite, is meant to be understandable by humans bette

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image in BGR mode
img = cv2.imread('Assets/dog_backpack.jpg')
plt.imshow(img)
plt.show()

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# Convert the image from BGR to HSV, same with 24th line
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
plt.imshow(img)
plt.show()

# Convert the image from RGB to HSV
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
plt.imshow(img_hsv)
plt.show()

# Convert the image from RGB to HSL
img_hsl = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HLS)
plt.imshow(img_hsl)
plt.show()