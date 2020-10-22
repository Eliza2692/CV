import cv2
import numpy as np


img = cv2.imread('../DATA/sudoku.jpg',0)

sobelx = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


cv2.imwrite('img.jpg', img)

cv2.imwrite('sobel.jpg', sobelx)