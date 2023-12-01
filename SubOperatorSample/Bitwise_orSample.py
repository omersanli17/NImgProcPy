import cv2
import numpy as np

# Create two simple binary images
image1 = np.zeros((300, 300), dtype=np.uint8)
image2 = np.zeros((300, 300), dtype=np.uint8)

# Draw white rectangles on the images
cv2.rectangle(image1, (50, 50), (250, 250), 255, -1)
cv2.rectangle(image2, (150, 150), (300, 300), 255, -1)

# Apply bitwise OR operation
result = cv2.bitwise_or(image1, image2)

# Display the original images and the result
cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Bitwise OR Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
