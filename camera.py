#!/usr/bin/python
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys 

class MainWindow(QMainWindow): 

  print("Simple camera V0.1")
  
  def __init__(self): 
    super().__init__() 
    self.setGeometry(1207, 650, 100, 100) 
    self.setStyleSheet("background : #000;") 
    self.available_cameras = QCameraInfo.availableCameras() 
    self.viewfinder = QCameraViewfinder() 
    self.viewfinder.show() 
    self.setCentralWidget(self.viewfinder) 
    self.select_camera(0) 
    camera_selector = QComboBox() 
    self.show() 

  def select_camera(self, i): 
    self.camera = QCamera(self.available_cameras[i]) 
    self.camera.setViewfinder(self.viewfinder) 
    self.camera.start() 

if __name__ == "__main__" : 
  App = QApplication(sys.argv) 
  window = MainWindow()   
  sys.exit(App.exec()) 
