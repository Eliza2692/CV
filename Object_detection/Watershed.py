import cv2
import numpy as np 

sep_coins = cv2.imread('../DATA/pennies.jpg')

sep_blur = cv2.medianBlur(sep_coins,25)

gray_sep_coins = cv2.cvtColor(sep_blur,cv2.COLOR_RGB2GRAY)

ret, sep_thresh = cv2.threshold(gray_sep_coins,160,255,cv2.THRESH_BINARY_INV)

image, contours , hierachy = cv2.findContours(sep_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):

    if hierachy [0][i][3] == 1:

        cv2.drawContours(sep_coins,contours,i,(255,0,0),10)

cv2.imwrite('coins.jpg', sep_coins)
cv2.imwrite('grayblurtresh.jpg', sep_thresh)