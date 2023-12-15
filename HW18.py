# Canny Edge Detection

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Steps of Canny Edge Detection
# 1. Noise Reduction
# 2. Gradient Calculation
# 3. Non-maximum Suppression
# 4. Double Threshold
# 5. Edge Tracking by Hysteresis

# 1. Noise Reduction

# We use 5x5 Gaussian filter to remove the noise
# The kernel size can be changed, but it must be odd number
# The sigmaX and sigmaY are standard deviation in X and Y direction respectively
# If only sigmaX is given, sigmaY is taken as same as sigmaX
# If both are given as zeros, they are calculated from kernel size

# Read the image
img = cv2.imread('Assets/sammy_face.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Run canny edge detection on the image, threshold1 and threshold2 are the thresholds for hysteresis procedure
# Any edges with intensity gradient more than threshold2 are sure to be edges and those below threshold1 are sure to be non-edges
edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
plt.imshow(edges)
plt.show()


# Median of the image
# Median is the middle value of the sorted pixel values

median = np.median(img)
print(median) # 64.0

# Lower threshold to either 0 or 70% of the median value whichever is greater
lower = int(max(0, 0.7 * median))

# Upper threshold to either 130% of the median or the max 255, whichever is smaller
upper = int(min(255, 1.3 * median))

# Apply Gaussian Blur
imgBlur = cv2.blur(img, (7, 7), 0)

# Display the image
plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(imgBlur)
plt.title('Blurred Image')
plt.xticks([])
plt.yticks([])
plt.show()

# Run canny edge detection on the image by lower and upper thresholds, two plot the images side by side blurred canny edge and unblurred canny edge
edgeNotBlurred = cv2.Canny(image=img, threshold1=lower, threshold2=upper)
edges = cv2.Canny(image=imgBlur, threshold1=lower, threshold2=upper)

plt.subplot(121)
plt.imshow(edgeNotBlurred)
plt.title('Canny Original Image Not Blurred')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(edges)
plt.title('Canny Edge Detection with Gaussian Blur')
plt.xticks([])
plt.yticks([])
plt.show()