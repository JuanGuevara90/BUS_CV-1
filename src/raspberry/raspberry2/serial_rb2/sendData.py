import serial,os
import time 
from os.path import join, dirname
import serial
import os
from dotenv import load_dotenv
from os.path import join, dirname

from socket import *
from socketserver import TCPServer
from time import ctime


def getred():   
    HOST=''
    PORT = 21567
    BUFSIZ= 1024
    ADDR = (HOST, PORT)

    tcpSvrSock =socket(AF_INET, SOCK_STREAM)
    tcpSvrSock.bind(ADDR)
    tcpSvrSock.listen(5)

    while True:
        print ("esperando para conectarse ")
        tcpCliSock, addr = tcpSvrSock.accept()
        print("conectando desde", addr)
        while True:
            data= tcpCliSock.recv(BUFSIZ)
            data = data.decode('utf-8')
            respMsg="[%s] %s" % (ctime(), data)
            tcpCliSock.send(bytes(respMsg, 'utf-8'))
            print(data)
            
            if not data:
                break
            return data 
        tcpCliSock.close

        tcpSvrSock.close()

def sendDatabySerial(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    FRECUENCIA = os.environ.get("FRECUENCIA")
    DISPOSITIVO = os.environ.get("DISPOSITIVO")
    ser=serial.Serial(''+DISPOSITIVO, FRECUENCIA)
    ser.write(msg.encode("utf-8"))
    ser.close()

def sendred(msg):

    HOST='169.254.212.26'
    PORT = 21567
    BUFSIZ= 1024
    ADDR = (HOST, PORT)

    tcpCliSock= socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send(msg)
    print(msg.decode('utf-8'))
    tcpCliSock.close()

def arduino (mnsj):
  arduino = serial.Serial("/dev/ttyACM0", 9600)
  time.sleep(2)
  arduino.write(mnsj.encode("utf-8"))
  arduino.close()