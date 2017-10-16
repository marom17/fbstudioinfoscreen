"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: mainUI.py
__Description__: Display the main window of the application

"""
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout,\
    QGridLayout, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from uiTL import UITLMain
from uiClock import UIClock
from uiNews import UINews
from uiInfoLeft import UIInfoLeft
from uiInfoRight import UIInfoRight
from uiMeteoMain import UIMeteoMain

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
        
        self.drawMainWindow()
        
        self.showFullScreen()
        #self.show()
        
        
    '''
    Exit the program with escape key
    '''
    def keyPressEvent(self, event):
        
        if(event.key() == Qt.Key_Escape):
            self.close()
     
    '''
    Draw the main window
    ''' 
    def drawMainWindow(self):
        self.windowLayout = QFrame(self)
        self.windowLayout.setMinimumSize(self.width(), self.height())
        self.windowLayout.setMaximumSize(self.width(), self.height())
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        
        self.drawTop()
        self.drawBottom()
        
        self.windowLayout.setLayout(self.gridLayout)

    '''
    Draw clock, FB Info
    '''
    def drawTop(self):
        
        self.uiclock = UIClock(self)
        self.uiLeftInfo = UIInfoLeft(self)
        self.uiRightInfo = UIInfoRight(self)
        
        self.gridLayout.addWidget(self.uiclock,0,0)
        self.gridLayout.addWidget(self.uiLeftInfo,0,1)
        self.gridLayout.addWidget(self.uiRightInfo,0,2)
        
    '''
    Draw tl-live, romandie and meteo
    ''' 
    def drawBottom(self):
        
        self.uitl = UITLMain(self)
        self.uinews = UINews(self)
        self.uimeteo = UIMeteoMain(self)
        
        self.gridLayout.addWidget(self.uitl,1,0)
        self.gridLayout.addWidget(self.uinews,1,1)
        self.gridLayout.addWidget(self.uimeteo,1,2)
        #self.gridLayout.setAlignment(self.uitl, Qt.AlignBottom)
        #self.layoutBottom.setAlignment(self.uitl,Qt.AlignBottom)
        
        