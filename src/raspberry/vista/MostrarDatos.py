import serial, time
from raspberry.controlador import controladorDatos

def connection():
    puerto = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 0.2)
    if puerto.isOpen() == False:
        puerto.open()
    puerto.flushInput()
    puerto.flushOutput()
    return puerto


def agregar():
    puerto = connection()
    datospantalla=controladorDatos()
    d1=(datospantalla[1])
    d2=(datospantalla[2])
    lblpi=d1
    lblps=d2
    puerto.write(b't4'+str(lblpi).encode()+b' '+b'\xFF\xFF\xFF')
    puerto.write(b't4'+str(lblps).encode()+b' '+b'\xFF\xFF\xFF')

def estado(d1):
    puerto = connection()
    dato=d1     
    if dato>=0 and dato<5:
       puerto.write(b't4'"background-color: rgb(1664);")