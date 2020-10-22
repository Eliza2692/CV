import cv2
import numpy as np 


# importar imagenes

nadia = cv2.imread("../DATA/Nadia_Murad.jpg",0)
denis = cv2.imread("../DATA/Denis_Mukwege.jpg",0)
sovay = cv2.imread("../DATA/solvay_conference.jpg",0)

cv2.imwrite("1.jpg",nadia)
cv2.imwrite("2.jpg",denis)
cv2.imwrite("3.jpg",sovay)

face_cascade = cv2.CascadeClassifier("../DATA/haarcascade_frontalface_default.xml")

def detect_face(img):

    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img,)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)

    return face_img

result = detect_face(denis)

cv2.imwrite("fi.jpg",result)