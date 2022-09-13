import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
from raspberry.controlador import controladorDatos
from ..utiles.getDateCurrent import getDate_Current
from ..database.conexion import create_connection
global d1, d2
d1=0
d2=0
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("/Users/Jessica/Desktop/BUS_CV/src/raspberry/vista/interfaz.ui", self)
        self.label_9.setText.connect(self.agregar)

        dato=5      
        if dato>=0 and dato<5:
            self.label_8.setStyleSheet("background-color: rgb(0, 170, 0);")
        if dato>=5 and dato<10:
            self.label_8.setStyleSheet("background-color:  rgb(255, 100, 28)")
        if dato>=10 and dato<=15:
            self.label_8.setStyleSheet("background-color: rgb(255, 24, 3);")
                        
        #Show the app
        self.show()

    def agregar(self):
        conn = create_connection()
        dateCurrent = getDate_Current()
        datospantalla=controladorDatos(conn,dateCurrent)
        d1=(datospantalla[1])
        d2=(datospantalla[2])
        lblpi=str(d1)
        lblpi=str(d2)
        self.label_8.setText(lblpi)
        self.label_9.setText(lblpi)
      

#Initialize the app
app = QApplication(sys.argv)
window = UI()
app.exec_()