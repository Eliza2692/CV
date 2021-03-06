import cv2 
import numpy as np

blank_img = np.zeros((512,512,3),np.int16)

print(blank_img)

# dibuja rectangulo
cv2.rectangle(blank_img,pt1=(384,10),pt2=(500,150),color=(0,255,0),thickness=10)
cv2.rectangle(blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)
cv2.circle(blank_img,center=(100,100),radius=50,color=(255,0,0), thickness=8)
cv2.circle(blank_img,center=(400,400),radius=50,color=(255,0,0), thickness=-1)
cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(85,170,255),thickness=5)

#texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='Hello',org=(10,500), fontFace=font, fontScale=4, color=(255,255,255),thickness=3)
# poligonos
vertices = np.array([[100,300],[200,200],[400,300],[200,400]],dtype = np.int32)
pts = vertices.reshape(-1,1,2)
cv2.polylines(blank_img,[pts],isClosed=True, color=(255,170,85),thickness=5)

# crea foto
cv2.imwrite('blank.jpg', blank_img)

