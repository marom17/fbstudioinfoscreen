"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: mainUI.py
__Description__: Display the main window of the application

"""
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from uiTL import UITLMain

class MainWindow(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ressources/fbld.ico"))
        self.setWindowTitle("FB Studio Info")
        rec = QApplication.desktop().screenGeometry()
        
        self.resize(rec.width(),rec.height())
        
        
        self.drawBottom()
        
        self.show()
        
        
    '''
    Exit the program with escape key
    '''
    def keyPressEvent(self, event):
        
        if(event.key() == Qt.Key_Escape):
            self.close()
       
    '''
    Draw clock, FB Info
    '''
    def drawTop(self):
        pass
    '''
    Draw tl-live, romandie and meteo
    ''' 
    def drawBottom(self):
        self.uitl = UITLMain(self)
        