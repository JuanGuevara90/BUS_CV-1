
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

img = cv2.imread("2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3,5)
count = 0
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    count = count+1
cv2.putText(img, str(count),(0,200), cv2.FONT_ITALIC, 2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('img',img)
cv2.imwrite('test3.jpg', img)
print("Success")
print(count)
cv2.waitKey()