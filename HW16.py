# Steps of Harris Corner Detection Algorithm
# 1. Compute the gradient of the image (I_x, I_y)
# 2. Compute the products of gradients at each pixel (I_x^2, I_y^2, I_x*I_y)
# 3. Compute the sum of the products of gradients for a given window
# 4. Compute the matrix M
# 5. Compute the response of the detector at each pixel
# 6. Threshold the corner response
# 7. Perform non-maximum suppression
# 8. Display the detected corners on the original image

import cv2  
import numpy as np
import matplotlib.pyplot as plt

flatChess = cv2.imread("Assets/chessboard.png")
flatChess = cv2.cvtColor(flatChess, cv2.COLOR_BGR2RGB)
plt.imshow(flatChess)
plt.show()

# Gray Chessboard
grayChessBoard = cv2.cvtColor(flatChess, cv2.COLOR_RGB2GRAY)
plt.imshow(grayChessBoard, cmap="gray")
plt.show()

# Real Chessboard
realChessBoard = cv2.imread("Assets/real_chessboard.jpg")
realChessBoard = cv2.cvtColor(realChessBoard, cv2.COLOR_BGR2RGB)
plt.imshow(realChessBoard)
plt.show()

# Gray Real Chessboard
grayRealChessBoard = cv2.cvtColor(realChessBoard, cv2.COLOR_RGB2GRAY)
plt.imshow(grayRealChessBoard, cmap="gray")
plt.show()

# Float32 Gray Real Chessboard
gray = np.float32(grayRealChessBoard)

# Harris Corner Detection, blocksize is the size of the neighborhood considered for corner detection, eigenvalues are the float32 values
# Blocksize is the size of the neighborhood considered for corner detection
# ksize is the aperture parameter for the Sobel() operator, k is the Harris detector free parameter in the equation

destination = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)
destination = cv2.dilate(destination, None)
realChessBoard[destination > 0.01 * destination.max()] = [255, 0, 0] # highlighted in red in the original RGB image 
plt.imshow(realChessBoard)
plt.show()
 

"""
Dilation; bir pikselin etrafındaki bölgeyi tanımlar ve bu bölge içindeki en yüksek (maksimum) değeri seçer.
Dilation, bu maksimum değeri, orijinal görüntüdeki piksel değeriyle değiştirir.
"""