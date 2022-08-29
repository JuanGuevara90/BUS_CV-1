import serial,os
import time 


from os.path import join, dirname
from dotenv import load_dotenv

def sendDatabySerial(msg):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    FRECUENCIA = os.environ.get("FRECUENCIA")
    DISPOSITIVO = os.environ.get("DISPOSITIVO")
    ser=serial.Serial(''+DISPOSITIVO, FRECUENCIA, timeout=1)
    ser.write(b''+msg)
    ser.close()


def arduino (mnsj):
  arduino = serial.Serial("COM5", 9600)
  time.sleep(2)
  arduino.write(mnsj.encode("utf-8"))
  arduino.close()

def ardrecibe():

  hw_sensor = serial.Serial(port='COM4', baudrate=115200, timeout=1, write_timeout=1)

  if __name__ == '__main__':
    while True:
        hw_sensor.write('getValue'.encode('utf-8'))
        time.sleep(1)
        try:
            raw_string_b = hw_sensor.readline()
            raw_string_s = raw_string_b.decode('utf-8')
            if(raw_string_s.index("}")>=0 and raw_string_s.index("{")==0):
                raw_string_s = raw_string_s[0:raw_string_s.index("}")+1]
                raw_string_j = json.loads(raw_string_s)
                print(raw_string_j)
                print(raw_string_j["Sensor_id"])
                print(raw_string_j["Value"])
                return raw_string_j
            else:
                print("error/ no } found.")
        except:
            print("Exception occurred, somthing wrong...")
  hw_sensor.close()

