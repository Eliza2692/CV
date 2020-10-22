import cv2
import numpy as np


img = cv2.imread('../DATA/horse.jpg')
img2 = cv2.imread('../DATA/rainbow.jpg')
img3 = cv2.imread('../DATA/bricks.jpg')


cv2.imwrite('img.jpg', img)
cv2.imwrite('img2.jpg', img2)
cv2.imwrite('img3.jpg', img3)