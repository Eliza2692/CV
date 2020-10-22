import cv2
import numpy as np 

def loadImg():
    blank_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text="NENA", org = (50,300), fontFace=font, fontScale=5, color = (255,255,255),thickness=20)
    return blank_img

img = loadImg()

cv2.imwrite('img.jpg', img)

kernel = np.ones((5,5), dtype = np.uint8)

result = cv2.erode(img,kernel,iterations=5)

cv2.imwrite('img2.jpg', result)

print(kernel)