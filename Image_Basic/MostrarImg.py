import numpy as np
import matplotlib as plt
import cv2

img = cv2.imread('pic.JPEG')

while True:
    cv2.imshow('pic',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()