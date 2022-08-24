import serial
import os
from dotenv import load_dotenv
from os.path import join, dirname

def sendDatabySerial(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    FRECUENCIA = os.environ.get("FRECUENCIA")
    DISPOSITIVO = os.environ.get("DISPOSITIVO")
    ser=serial.Serial(''+DISPOSITIVO, FRECUENCIA, timeout=1)
    ser.write(b''+msg)
    ser.close()