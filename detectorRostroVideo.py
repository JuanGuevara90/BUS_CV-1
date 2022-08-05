import cv2                # Importar librería de open cv
import numpy as np        # Importar librería de numpy como un alias de np
import time               # Importar librería de tiempo
from Registro_pasajeros import main

main()
cap = cv2.VideoCapture(0)     #Captura la imagen con la cámara

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
count=0

while True:              # Ciclo repetitivo hasta que la condición se vuelva verdadero
    try:
        ret,frame = cap.read()  # Bucle infinito hastan llegar a la instrucción brake
        #imAux = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Se define una nueva variable gray (marco)
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        cropped = frame.copy()
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            count=count+1     
            cropped = frame[y:y+h, x:x+w]
            #cv2.imshow('CORTE1',cropped)
        cv2.imshow('frame',frame)         # Muestra una ventana
        cv2.imshow('GRISS',gray)          #Muentra ventana en gris
        time.sleep(0.25)       # 
        k= cv2.waitKey(1)
        if k== 27 or count >=40:
           
            if count == 40:     
                print ("Límite alcanzado")
            break
    except:
        print("error")

        

    print(count)
cap.release()         # Libera la imagen
cv2.destroyAllWindows()  # Cierra todas las ventanas del imshow