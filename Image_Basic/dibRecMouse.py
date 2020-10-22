import cv2
import numpy as np

# VARIABLES

# TRue while mouse button Down 
drawing = False
ix = -1
iy = -1

# FUNCTION

def drawRectangle(event,x,y,flags,params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy),(x,y),(255,0,0),-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
        cv2.rectangle(img, (ix,iy),(x,y),(255,0,0),-1)

# Show image whit openCV

# Black
img = np.zeros((512,512,3),np.int8)

cv2.namedWindow(winname='myDrawing')
cv2.setMouseCallback('myDrawing',drawRectangle)

while True:
    cv2.imshow('myDrawing',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()