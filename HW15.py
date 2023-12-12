# Template Matching
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image and show
fullImage = cv2.imread("Assets/sammy.jpg")
fullImage = cv2.cvtColor(fullImage, cv2.COLOR_BGR2RGB)
plt.imshow(fullImage)
plt.show()

# Read the template and show, face is the scaled version of the template
face = cv2.imread("Assets/sammy_face.jpg")
face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
plt.imshow(face)
plt.show()

# Template matching
# TM_CCOEFF is the correlation coefficient
# TM_CCOEFF_NORMED is the normalized correlation coefficient
# TM_CCORR is the cross correlation
# TM_CCORR_NORMED is the normalized cross correlation
# TM_SQDIFF is the sum of squared differences
# TM_SQDIFF_NORMED is the normalized sum of squared differences

# Whole computational methods in array
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# Loop through the methods

for m in methods:
    
    # Create a copy of the image
    fullImageCopy = fullImage.copy()

    # Get the method
    method = eval(m)

    # Template matching
    result = cv2.matchTemplate(fullImageCopy, face, method)

    # Get the min and max values
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(minVal, maxVal, minLoc, maxLoc)

    # Draw the rectangle around the matched area
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        topLeft = minLoc
    else:
        topLeft = maxLoc

    height, width, channels = face.shape

    bottomRight = (topLeft[0] + width, topLeft[1] + height)

    cv2.rectangle(fullImageCopy, topLeft, bottomRight, (255,0,0), 10)

    # Show the image, means of plt.subplot(121) ? 
    # plt.subplot(121) means 1 row, 2 columns, 1st subplot
    plt.subplot(121)
    plt.imshow(result)
    plt.title("Heatmap of template matching")
    plt.subplot(122)
    plt.imshow(fullImageCopy)
    plt.title("Detection of template")
    plt.suptitle(m)
    plt.show()


selectedMethod = methods[0]
method = eval(selectedMethod)
result = cv2.matchTemplate(fullImage, face, method)

plt.imshow(result)
plt.show()