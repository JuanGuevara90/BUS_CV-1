import cv2
import numpy as np

cap = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
    ret,frame = cap.read()
    #imAux = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    cropped = frame.copy()
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cropped = frame[y:y+h, x:x+w]
        #cv2.imshow('CORTE1',cropped)
    cv2.imshow('frame',frame)
    cv2.imshow('GRISS',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()