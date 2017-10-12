"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: uiTL.py
__Description__: Display the tl live display

"""
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy,\
    QLabel, QBoxLayout
from signals import eventSignals
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class UITLMain(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        
        #set frame
        self.setParent(parent)
        self.resize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3,parent.height()/2)
        self.setStyleSheet("background-color:black")

        self.drawTL()
        
        self.show()
        
    def drawTL(self):
        
        self.layoutSchedule = QHBoxLayout(self)
        self.layoutSchedule.setAlignment(Qt.AlignBottom)
        self.layoutSchedule.setSpacing(0)
        self.layoutSchedule.setContentsMargins(0, 0, 0, 0)
        
        self.scheduleLeft = TLSchedule('left',self)
        self.scheduleRight = TLSchedule('right',self)
        
        self.layoutSchedule.addWidget(self.scheduleLeft)
        self.layoutSchedule.addWidget(self.scheduleRight)
        
        self.scheduleLeft.show()
        self.scheduleRight.show()

        self.setLayout(self.layoutSchedule)
    
   
'''
Display the schedule
''' 
class TLSchedule(QFrame):
    
    def __init__(self,side,parent):
        super().__init__()
        
        self.side = side
        self.setParent(parent)
        self.resize(parent.width()/2,parent.height()/2)
        self.setMinimumSize(parent.width()/2,parent.height()/2)
        self.setMaximumSize(parent.width()/2,parent.height()/2)
        
        self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        self.drawWindow()
        
        self.setStyleSheet("background-color:red")
        self.setAutoFillBackground(True)
        
        #init connector
        eventSignals.tl.connect(self.updateSchedule)
        
    '''
    Draw the schedule window
    '''
    def drawWindow(self):
        
        self.layoutSchedule = QVBoxLayout(self)
        self.title = QLabel("Renens")
        self.boxArray = []
        self.station = QLabel('Get Info',self)
        
        self.layoutSchedule.addWidget(self.station)
        for i in range(0,4):
            box = self.createBox()
            self.boxArray.append(box)
            self.layoutSchedule.addWidget(box)
            
        self.setLayout(self.layoutSchedule)
    
    '''
    Create a schedule box
    '''
    def createBox(self):
        box = QFrame()
        box.resize(self.width(),self.height()/4)
        box.setStyleSheet("background-color:green")
        font = QFont("Times new roman",25)
        
        layoutBox = QHBoxLayout(box)
        layoutBox.setAlignment(Qt.AlignCenter)
        
        textlign = QLabel("Get Info",box)
        textlign.setObjectName("ligne")
        #textlign.setAlignment(Qt.AlignLeft)
        textlign.setFont(font)
        textlign.setStyleSheet("background-color:black;color:white")
        
        texttemps = QLabel("",box)
        texttemps.setObjectName("time")
        #texttemps.setAlignment(Qt.AlignRight)
        texttemps.setFont(font)
        texttemps.setStyleSheet("background-color:black;color:white")
        
        layoutBox.addWidget(textlign)
        layoutBox.addWidget(texttemps)
        
        #layoutBox.setAlignment(textlign, Qt.AlignLeft)
        #layoutBox.setAlignment(texttemps, Qt.AlignRight)
        
        box.setLayout(layoutBox)
        
        return box
        
    '''
    Update the schedul info
    '''
    def updateSchedule(self,side,params):
        if(self.side in side):
            
            ligne = params[0]
            destination = params[2]
            stop = params[1]
            self.station.setText(stop+"->"+destination)
            for i in range(0,4):
                self.boxArray[i].findChild(QLabel,'ligne').setText(ligne)
                self.boxArray[i].findChild(QLabel,'time').setText(params[i+3])