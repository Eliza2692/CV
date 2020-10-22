import cv2
import numpy as np 

flat_chess = cv2.imread('../DATA/flat_chessboard.png')
real_chess = cv2.imread('../DATA/real_chessboard.jpg')

# Harris Corner

gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_RGB2GRAY)
gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_RGB2GRAY)

gray = np.float32(gray_flat_chess)
gray_real = np.float32(gray_real_chess)

dst = cv2.cornerHarris(src= gray, blockSize= 2, ksize= 3, k= 0.04)
dst_real = cv2.cornerHarris(src= gray_real, blockSize= 2, ksize= 3, k= 0.04)

dst = cv2.dilate(dst, None)
dst_real = cv2.dilate(dst_real, None)

flat_chess[dst > 0.01 * dst.max()] = [0, 0, 255]
real_chess[dst_real > 0.01 * dst_real.max()] = [0, 0, 255]

cv2.imwrite('flat.jpg', flat_chess)
cv2.imwrite('real.jpg', real_chess)
cv2.imwrite('flat_gray.jpg', gray_flat_chess)
cv2.imwrite('real_gray.jpg',gray_real_chess)

# Corner methodos 2

flat_chess = cv2.imread('../DATA/flat_chessboard.png')
real_chess = cv2.imread('../DATA/real_chessboard.jpg')

gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_RGB2GRAY)
gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_RGB2GRAY)

corner = cv2.goodFeaturesToTrack(gray_flat_chess, 64, 0.01, 10)
corner = np.int0(corner)

for i in corner:
    x, y = i.ravel()
    cv2.circle(flat_chess, (x,y), 3, (0, 0, 255), -1)

corner_real = cv2.goodFeaturesToTrack(gray_real_chess, 100, 0.01, 10)
corner_real = np.int0(corner_real)

for i in corner_real:
    x, y = i.ravel()
    cv2.circle(real_chess, (x,y), 3, (0, 0, 255), -1)

cv2.imwrite('flat2.jpg', flat_chess)
cv2.imwrite('real2.jpg', real_chess)
cv2.imwrite('flat2_gray.jpg', gray_flat_chess)
cv2.imwrite('real2_gray.jpg',gray_real_chess)