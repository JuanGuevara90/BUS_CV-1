import serial

def sendDatabySerial():
    serial.Serial('/dev/ttyS1', 19200, timeout=1)
    ser.write(b'hello')
    ser.close()   # write a string