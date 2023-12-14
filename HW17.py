# Shi-Tomasi Corner Detector 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image, chessboard.png and real_chessboard.jpg
chessboard = cv2.imread('Assets/chessboard.png')
real_chessboard = cv2.imread('Assets/real_chessboard.jpg')

# Grayscale version
chessboard_gray = cv2.cvtColor(chessboard, cv2.COLOR_BGR2GRAY)
real_chessboard_gray = cv2.cvtColor(real_chessboard, cv2.COLOR_BGR2GRAY)

# goodFeaturesToTrack finds N strongest corners in the image by Shi-Tomasi method

# image, maxCorners, qualityLevel, minDistance 
# qualityLevel: Parameter characterizing the minimal accepted quality of image corners.
# minDistance: Minimum possible Euclidean distance between the returned corners.
# -1 for detecting all corners, instead of 5

corners = cv2.goodFeaturesToTrack(chessboard_gray, 64, 0.01, 10)

# Draw circle around the corners

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.circle(chessboard_gray, (x, y), 10, (255, 0, 0), -1)

# Display the image with the corners
plt.imshow(chessboard_gray, cmap='gray')
plt.show()

# Doing the samething for real_chessboard_gray

cornersReal = cv2.goodFeaturesToTrack(real_chessboard_gray, 32, 0.01, 10)
print(cornersReal)

for corner in cornersReal:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.circle(real_chessboard_gray, (x, y), 10, (255, 0, 0), -1)

plt.imshow(real_chessboard_gray, cmap='gray')
plt.show()