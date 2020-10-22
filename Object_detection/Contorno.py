import cv2
import numpy as np 

img = cv2.imread('../DATA/internal_external.png')

image, contorno, hierachy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

external_contorno = np.zeros(image.shape)

for i in range(len(contorno)):
    # external
    if hierachy[0][i][3] == -1:
        cv2.drawContours(external_contorno, contorno, i, 255, -1)
    

cv2.imwrite('img.jpg',img)