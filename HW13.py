# Read the video on Assets folder name is iPhone X Trailer — Apple.mp4

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

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # WRITE 20 FRAMES PER SECOND TO SEE THE VIDEO HUMAN EYE CAN SEE
        time.sleep(1/60)
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()
cv2.destroyAllWindows()