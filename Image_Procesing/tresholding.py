import cv2
import numpy as np
img = cv2.imread('DATA/rainbow.jpg',0)

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img2 = cv2.imread('DATA/crossword.jpg')

ret2, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)