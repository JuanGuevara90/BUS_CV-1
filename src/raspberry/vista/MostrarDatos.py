import serial, time
#import RPi.GPIO as GPIO
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
    puerto.write(b'n00.val='+str(lblpi).encode()+b'\xFF\xFF\xFF')
    puerto.write(b'n1.val='+str(lblps).encode()+b'\xFF\xFF\xFF')

def estado(d1):
    puerto = connection()
    dato=d1     
    if dato>=0 and dato<5:
       puerto.write(b"t6.bco=GREEN"+b'\xFF\xFF\xFF')
    if dato>=5 and dato<10:
       puerto.write(b"t6.bco=64512"+b'\xFF\xFF\xFF')
    if dato>=10 and dato<=15:
       puerto.write(b"t6.bco=RED"+b'\xFF\xFF\xFF')
    
"""def ShutdownButton(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8,GPIO IN, pull_up_down=GPIO.PUD_UP)
    def ButtonApagar():
        while True:
            if GPIO.input(8)==False:
                print("La raspberry Pi se apagará")
                subprocess.call(['sudo','shutdown','now'])"""