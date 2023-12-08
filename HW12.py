# Connect Camera on Python and OpenCV

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec for Video 
# Windows: DIVX
# MacOS & Linux: XVID

# 20 is the number of frames per second
writer = cv2.VideoWriter('Assets/myvideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()