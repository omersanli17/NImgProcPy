#You only have one task here. Create a program that reads in a live stream from a camera on your computer 
# (or if you don't have a camera, just open up a video file, in Assets folder iPhone X Trailer - Apple.mp4 ). 
# Then whenever you click the left mouse button down, create a blue circle around where you've clicked.
# Check out the video for an example of what the final project should look like**

import cv2
import numpy as np
import os
import time

# Read the video
video_path = "Assets/iPhone X Trailer - Apple.mp4"
cap = cv2.VideoCapture(video_path)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

def draw_circle(event,x,y,flags,param):
    global center, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False

    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

center = (0,0)
clicked = False

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', draw_circle)

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        if clicked:
            cv2.circle(frame, center=center, radius=50, color=(255,0,0), thickness=5)
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

