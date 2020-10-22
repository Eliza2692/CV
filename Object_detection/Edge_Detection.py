import cv2
import numpy as np 

img = cv2.imread('../DATA/sammy_face.jpg')


edge = cv2.Canny(image= img, threshold1= 127, threshold2= 127)

cv2.imwrite('img1.jpg',edge)