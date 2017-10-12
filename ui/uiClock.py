"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiClock.py
__Description__: Display the time

"""

from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QGridLayout
from signals import eventSignals
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt

class UIClock(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        self.setParent(parent)
        self.resize(parent.width()/2,parent.height()/2)
        self.setMinimumSize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:black")
        self.setAutoFillBackground(True)
        
        id = QFontDatabase.addApplicationFont("ressources/QuiverItal Regular.ttf")
        family = QFontDatabase.applicationFontFamilies(id)[0]
        
        self.font = QFont(family,45)
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setAlignment(Qt.AlignTop)
        
        self.drawTop()
        self.drawBottom()
        
        eventSignals.time.connect(self.updateTime)
        
        self.setLayout(self.gridLayout)
        self.show()
        
    '''
    Draw the 
    '''
    def drawTop(self):
        self.date = QLabel('',self)
        self.date.setFont(self.font)
        self.date.setStyleSheet("color:red")
        self.gridLayout.addWidget(self.date,0,0)
        self.gridLayout.setAlignment(self.date,Qt.AlignCenter)
    
    
    def drawBottom(self):
        self.time = QLabel('',self)
        self.time.setFont(self.font)
        self.time.setStyleSheet("color:red")
        self.gridLayout.addWidget(self.time,1,0)
        self.gridLayout.setAlignment(self.time,Qt.AlignCenter)
        
        
    '''
    Update the time
    '''
    def updateTime(self,date,time):
        self.date.setText(date)
        self.time.setText(time)
        