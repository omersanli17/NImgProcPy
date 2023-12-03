import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create an black empty image 600x 600,  put text HERSHEY_COMPLEX 'ABCDE' on it

def createImage():
    img = np.zeros(shape=(600,600))
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,text='OMER',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return img


def show(img):
    # It creates a figure object with the specified size. 6,6 means 6 inches by 6 inches
    fig = plt.figure(figsize=(12,10))
    # It adds an Axes to the figure as part of a subplot arrangement. 111 means 1x1 grid, first subplot
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

image = createImage()
show(image)

kernel = np.ones(shape=(5,5),dtype=np.uint8)

# Erosion
result = cv2.erode(image,kernel,iterations=5)
show(result)

# Add background Noise
white_noise = np.random.randint(low=0,high=2,size=(600,600))
show(white_noise)

# 1 to 255, 0 and 255
white_noise = white_noise * 255
show(white_noise)

noise_image = white_noise + image
show(noise_image)

opening = cv2.morphologyEx(noise_image,cv2.MORPH_OPEN,kernel)
show(opening)

# Add black noise, -255 and 0
black_noise = np.random.randint(low=0,high=2,size=(600,600))
black_noise = black_noise * -255
show(black_noise)

# In order to get noise on white negative -255 is added to positive brightnesss of white
black_noise_image = black_noise + image
black_noise_image[black_noise_image == -255] = 0
show(black_noise_image)

closing = cv2.morphologyEx(black_noise_image,cv2.MORPH_CLOSE,kernel)
show(closing) 

# morphological gradient, It is the difference between dilation and erosion of an image.

gradient = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
show(gradient)

# In order to understand erosion, show theoretical GIF file

from SubOperatorSample.GIFLoading import show_loading_gif

if __name__ == "__main__":
    gif_file_name = "Erosion"  # Replace with Dilation to see
    loading_window = show_loading_gif(gif_file_name)

    # Close the loading window after the processing is done
    loading_window.stopAnimation()
    loading_window.close()