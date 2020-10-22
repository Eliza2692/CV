import cv2
import numpy as np

img1 = cv2.imread('pic.JPEG')
img2 = cv2.imread('char.png')

# blending the same size

img3 = cv2.resize(img1,(1200,1200))
img4 = cv2.resize(img2,(1200,1200))

blended = cv2.addWeighted(src1=img3, alpha= 0.5, src2=img4, beta= 0.5, gamma= 0)

#blending diferente size

x_offset = img1.shape[1] - img2.shape[1]
y_offset = img1.shape[0] - img2.shape[0]

rows, cols, chanels = img2.shape

roi = img1[y_offset:,x_offset:,:]

img2_gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

#Create mask

mask_inv = cv2.bitwise_not(img2_gray)

#white background
white_background = np.full(img2.shape,255,dtype=np.uint8)
bk = cv2.bitwise_or(white_background,white_background,mask= mask_inv)

#final
fg = cv2.bitwise_or(img2,img2,mask_inv)
final = cv2.bitwise_or(roi,fg)

# crea foto
cv2.imwrite('final.jpg', final)
cv2.imwrite('bk.jpg', bk)
cv2.imwrite('mask.jpg', mask_inv)
cv2.imwrite('gray2.jpg', img2_gray)
cv2.imwrite('roi.jpg', roi)
cv2.imwrite('img1.jpg', img3)
cv2.imwrite('img2.jpg', img4)
cv2.imwrite('blended.jpg', blended)
