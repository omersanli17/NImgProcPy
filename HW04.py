import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)
import cv2
from matplotlib import pyplot as plt

# Read Images (Assets/dog_backpack.jpg, Assets/watermark_no_copy.png) in RGB Mode
dogImg = cv2.imread('Assets/dog_backpack.jpg')
watermarkImg = cv2.imread('Assets/watermark_no_copy.png')

# Convert the images from BGR to RGB
dogImg = cv2.cvtColor(dogImg, cv2.COLOR_BGR2RGB)
watermarkImg = cv2.cvtColor(watermarkImg, cv2.COLOR_BGR2RGB)

# Resize the watermark image
watermarkImg = cv2.resize(watermarkImg, (600, 600))

plt.imshow(watermarkImg)
plt.show()

# Create a Region of Interest (ROI) in the dog image, 984 is the width of the dog image, 600 is the width and height of the watermark image
x_offset = 934 - 600
y_offset = 1401 - 600

# 600, 600, 3 is the width, height and channel of the watermark image
rows, cols, channels = watermarkImg.shape 

# Create a ROI in the dog image
roi = dogImg[y_offset:1401, x_offset:984]

# Gray scale of watermark image, (water mark array = white background and black text)
watermarkGray = cv2.cvtColor(watermarkImg, cv2.COLOR_RGB2GRAY)
plt.imshow(watermarkGray, cmap='gray')
plt.show()

# Remove the white background of the watermark image,  bitwise_not: meaning it converts all 0s to 1s and all 1s to 0s.
mask = cv2.bitwise_not(watermarkGray)
plt.imshow(mask, cmap='gray')
plt.show()

# Create a white background for the watermark image
whiteBackground = np.full(watermarkImg.shape, 255, dtype=np.uint8)

# Mask shape has(600,600) in order to have 3 channels, bitwise operator used by mask
# It is just to show you can use bitwise or to use a mask to mask certain region of the image. The results is the same as before, since it is just a white background.
bk = cv2.bitwise_or(whiteBackground, whiteBackground, mask=mask)
plt.imshow(bk)
plt.show()

# Below code, we mask the watermark image to get red original watermark image
fg = cv2.bitwise_or(watermarkImg, watermarkImg, mask=mask)
plt.imshow(fg)
plt.show()

final_roi = cv2.bitwise_or(roi, fg)
plt.imshow(final_roi)
plt.show()

# Paste the watermark image on the original dog image
large_img = dogImg
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

plt.imshow(large_img)
plt.show()