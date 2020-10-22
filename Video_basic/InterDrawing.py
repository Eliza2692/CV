import cv2


#GLobals variables
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
topRight_clicked = False

#Call back function rectangle
def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2, topLeft_clicked, topRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        if topLeft_clicked == True and topRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            topRight_clicked = False
        
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True

        elif topRight_clicked == False:
            pt2(x,y)
            topRight_clicked =True



#conect to the call back
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)

while True :

    ret, frame = cap.read()

    #drawing on the framing global variabes
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
    
    if topLeft_clicked and topRight_clicked:
        cv2.rectangle(frame, pt1, pt2, color=(0,0,255),thickness=3)
    
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows