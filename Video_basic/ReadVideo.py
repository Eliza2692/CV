import cv2
import time

cap = cv2.VideoCapture('myvideo.avi')

if cap.isOpened() == False:
    print("No file")

while cap.isOpened():

    ret, frame  = cap.read()

    if ret == True:

        time.sleep(1/10)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows