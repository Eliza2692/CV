import cv2
import numpy as np 

flat_chess = cv2.imread('../DATA/flat_chessboard.png')

found, corners = cv2.findChessboardCorners(flat_chess, (7, 7))

cv2.drawChessboardCorners(flat_chess, (7, 7), corners, found)

cv2.imwrite('flat.jpg', flat_chess)