# HW1- Image Basic Assignment

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Read the image
img = cv2.imread('DATA/dog_backpack.jpg')

# Convert the image from BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image in RGB Mode
plt.imshow(img_rgb)
plt.show()

# Flip the image upside down (vertically) and display it
img_flip = cv2.flip(img_rgb, 0)
plt.imshow(img_flip)
plt.show()

# Draw an empty RED rectangle around the dogs face and display the image
cv2.rectangle(img_rgb, pt1=(200, 380), pt2=(600, 700), color=(255, 0, 0), thickness=10)
plt.imshow(img_rgb)
plt.show()

# Draw a BLUE TRIANGLE in the middle of the image and display the image
pts = np.array([[250, 700], [425, 400], [600, 700]], dtype=np.int32)
cv2.polylines(img_rgb, [pts], isClosed=True, color=(0, 0, 255), thickness=10)
plt.imshow(img_rgb)
plt.show()

# Fill the triangle with GREEN color and display image
cv2.fillPoly(img_rgb, [pts], color=(0, 255, 0))
plt.imshow(img_rgb)
plt.show()

