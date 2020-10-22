import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print (width,height)

Writer =  cv2.VideoWriter('myvideo.avi', cv2.VideoWriter_fourcc(*'XVID'),20,(width,height))


while True:

    ret, frame = cap.read()

    Writer.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

Writer.release()
cap.release()
cv2.destroyAllWindows()  
print (width,height)