import sys, time
#import RPi.GPIO as GPIO
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
from raspberry.controlador import controladorDatos

global d1, d2
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        filename="/Users/Jessica/Desktop/BUS_CV/src/raspberry/vista/interfaz.ui"
        uic.loadUi(filename, self)

        self.agregar()
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton') # Find the button
        #self.button.clicked.connect(self.ButtonApagar)
                      
        #Show the app
        self.show()

    def agregar(self):
        datospantalla=controladorDatos()
        d1=(datospantalla[1])
        d2=(datospantalla[2])
        lblpi=d1
        lblps=d2
        self.label_9.setText(""+str(lblpi))
        self.label_10.setText(""+str(lblps))

        #Estado del bus
        dato=d1     
        if dato>=0 and dato<5:
            self.label_8.setStyleSheet("background-color: rgb(0, 170, 0);")
        if dato>=5 and dato<10:
            self.label_8.setStyleSheet("background-color:  rgb(255, 100, 28)")
        if dato>=10 and dato<=15:
            self.label_8.setStyleSheet("background-color: rgb(255, 24, 3);")
        


    """def ShutdownButton(self):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8,GPIO IN, pull_up_down=GPIO.PUD_UP)
    def ButtonApagar():
        while True:
            if GPIO.input(8)==False:
                print("La raspberry Pi se apagará")
                subprocess.call(['sudo','shutdown','now'])"""

    #def OnButton(self):
        
            

#Initialize the app
app = QApplication(sys.argv)
window = UI()
app.exec_()