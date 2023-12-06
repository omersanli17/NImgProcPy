import cv2  
import numpy as np
import matplotlib.pyplot as plt

rainbow = cv2.imread('Assets/rainbow.jpg')
showRainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

img = rainbow
mask = np.zeros(img.shape[:2],np.uint8)

def showGray(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(6,6))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

showGray(mask)

# White 300:400,100:400
mask[300:400,100:400] = 255

showGray(mask)

def show(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(6,6))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

showMaskedImage = cv2.bitwise_and(showRainbow,showRainbow,mask=mask)
show(showMaskedImage)

# Histogram with mask and without mask 
histMaskValuesRed = cv2.calcHist([rainbow],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
histValuesRed = cv2.calcHist([rainbow],channels=[2],mask=None,histSize=[256],ranges=[0,256])

plt.plot(histMaskValuesRed)
plt.show()

plt.plot(histValuesRed)
plt.show()

# 0 for grayscale
gorilla = cv2.imread('Assets/gorilla.jpg',0) 
showGray(gorilla)

histValueGorilla = cv2.calcHist([gorilla],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(histValueGorilla)
plt.show()

# Equalization
equ = cv2.equalizeHist(gorilla)
showGray(equ)

histValueEqu = cv2.calcHist([equ],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(histValueEqu)
plt.show()

colorGorilla = cv2.imread('Assets/gorilla.jpg')
show(colorGorilla)

hsvVerisonGorilla = cv2.cvtColor(colorGorilla,cv2.COLOR_BGR2HSV)

# Value channel of hsvVerisonGorilla is the brightness
hsvVerisonGorilla[:,:,2] = cv2.equalizeHist(hsvVerisonGorilla[:,:,2])
show(cv2.cvtColor(hsvVerisonGorilla,cv2.COLOR_HSV2RGB))