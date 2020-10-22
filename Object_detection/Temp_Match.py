import cv2
import numpy as np 

full = cv2.imread('../DATA/sammy.jpg')
face = cv2.imread('../DATA/sammy_face.jpg')

cv2.imwrite('sammy.jpg',full)
cv2.imwrite('sammyFace.jpg',face)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:

    #create a copy
    full_copy = full.copy()

    method = eval(m)

    res = cv2.matchTemplate(full_copy,face,method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    heigh, width, chanels = face.shape

    bottom_right = (top_left[0] + width, top_left[1] + heigh)

    cv2.rectangle(full_copy, top_left, bottom_right, (255, 0, 0), 10)
    
    cv2.imwrite(str(m[-6:])+'.jpg',full_copy)