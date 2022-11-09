
import RPi.GPIO as GPIO

from .serial_rb2.sendData import getred,sendred,sendDatabySerial
from .serial_rb2.sensorica import sensorica #sensorica2
import os
from dotenv import load_dotenv
from os.path import join, dirname


from socket import *
from socketserver import TCPServer
from time import ctime



def controladorSensorSalida():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    TRIGH1 = os.environ.get("TRIGH1")
    ECHO1 = os.environ.get("ECHO1")
  
    distanciaS2=(sensorica(TRIGH1,ECHO1))
    if(distanciaS2):#aqui calibramos al sensor
        n=True
        return n
    GPIO.cleanup()



#rasberry2
def rsb2salida():
    #if(controladorSensorSalida()):
        adicion=True
        if(adicion==True):
            msg=b"restar"
            sendred(msg)
    #sendDatabySerial(getred()) 