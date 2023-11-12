import cv2
import numpy as np

from transform import perspective_transform

rect = np.zeros((4, 2), dtype='float32')
rect[0] = (300, 0)
rect[1] = (1280-300, 0)
rect[2] = (0, 720)
rect[3] = (1280, 720)

cap = cv2.VideoCapture(0)

if cap.isOpened():  # try to get the first frame
    rval, frame = cap.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = cap.read()
    frame = perspective_transform(frame, rect)
    print(frame.shape)
    key = cv2.waitKey(20)
    if key == 27:  # exit on ESC
        break

cv2.destroyWindow("preview")
cap.release()
