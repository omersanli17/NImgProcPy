import cv2
import numpy as np
import matplotlib.pyplot as plt

#  ORIGINAL BGR and RGB images
dark_horse = cv2.imread('Assets/horse.jpg')
showHorse = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('Assets/rainbow.jpg')
showRainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('Assets/bricks.jpg')
showBricks = cv2.cvtColor(blue_bricks,cv2.COLOR_BGR2RGB)

def show(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(6,6))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

show(showHorse)
show(showBricks)

# To calculate histograms of arrays of images by using the OpenCV function
#  Channels: [0]: blue, histSize: 256: upper limit, ranges: 0,256
histValues = cv2.calcHist([blue_bricks],channels=[0],mask=None,histSize=[256],ranges=[0,256])

print(histValues)
plt.plot(histValues)
plt.show()

# Same operation for horse 

histValuesOfHorse = cv2.calcHist([dark_horse],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(histValuesOfHorse)
plt.show()

def plotHistogramCustom(imageName,title,histSize=[256],ranges=[0,256]):
    img = cv2.imread('Assets/'+imageName)
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,histSize,ranges)
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.title(title)
    plt.show()

plotHistogramCustom('kerem.jpeg','Kerem Histogram')