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
from PyQt5.QtGui import QFont, QPixmap

class UITLMain(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        
        #set frame
        self.setParent(parent)
        self.resize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:black")

        self.drawTL()
        
        self.show()
        
    def drawTL(self):
        
        self.drawTop()
        self.drawBottom()
        
        #self.setLayout(self.layoutTop)
        self.setLayout(self.layoutSchedule)
    
    '''
    Draw the top frame
    '''
    def drawTop(self):
        topFrame = QFrame(self)
        topFrame.resize(self.width(),self.height()/4)
        topFrame.setMinimumSize(self.width(),self.height()/4)
        topFrame.setMaximumSize(self.width(),self.height()/4+1)
        topFrame.setStyleSheet("background-color:yellow")
        imageLabel = QLabel(topFrame)
        #imageLabel.setMinimumSize(self.width()/2,self.width()/2)
        image = QPixmap("ressources/logotl.svg")
        imageLabel.setPixmap(image)
        imageLabel.show()
        
        #top UI
        layoutTop = QHBoxLayout()
        layoutTop.setAlignment(Qt.AlignVCenter)
        font = QFont("Times new roman",25)
        self.name = QLabel('tl-live',self)
        self.name.setAlignment(Qt.AlignRight)
        self.name.setFont(font)
        self.name.setStyleSheet("color:blue")
        
        layoutTop.addWidget(imageLabel)        
        layoutTop.addWidget(self.name)
        #layoutTop.setAlignment(self.name, Qt.AlignRight)
        layoutTop.setAlignment(self.name, Qt.AlignVCenter)
        
        topFrame.setLayout(layoutTop)
        topFrame.show()
        
    '''
    Draw the schedule frame
    '''
    def drawBottom(self):
        #schedule UI
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
   
'''
Display the schedule
''' 
class TLSchedule(QFrame):
    
    def __init__(self,side,parent):
        super().__init__()
        
        self.side = side
        self.setParent(parent)
        self.resize(parent.width()/2,3*parent.height()/4)
        self.setMinimumSize(parent.width()/2,3*parent.height()/4)
        self.setMaximumSize(parent.width()/2+1,3*parent.height()/4+1)
        
        self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        self.drawWindow()
        
        self.setStyleSheet("background-color:#d6d6c2")
        self.setAutoFillBackground(True)
        
        #init connector
        eventSignals.tl.connect(self.updateSchedule)
        
    '''
    Draw the schedule window
    '''
    def drawWindow(self):
        
        self.layoutSchedule = QVBoxLayout(self)
        self.boxArray = []
        font = QFont("Times new roman",18)
        self.station = QLabel('Get Info',self)
        self.station.setFont(font)
        
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
        box.setStyleSheet("background-color:#f5f5ef")
        box.setFrameShape(QFrame.Box)
        font = QFont("Times new roman",18)
        
        layoutBox = QHBoxLayout(box)
        layoutBox.setAlignment(Qt.AlignVCenter)
        #layoutBox.setContentsMargins(0, 0, 0, 0)
        
        textlign = QLabel("Get Info",box)
        textlign.setObjectName("ligne")
        textlign.setAlignment(Qt.AlignLeft)
        textlign.setFont(font)
        textlign.setStyleSheet("color:black")
        
        texttemps = QLabel("",box)
        texttemps.setObjectName("time")
        texttemps.setAlignment(Qt.AlignRight)
        texttemps.setFont(font)
        texttemps.setStyleSheet("color:balc")
        
        layoutBox.addWidget(textlign)
        layoutBox.addWidget(texttemps)
        
        layoutBox.setAlignment(textlign, Qt.AlignLeft)
        layoutBox.setAlignment(texttemps, Qt.AlignRight)
        
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
            self.station.setText(ligne+"->"+destination)
            for i in range(0,4):
                self.boxArray[i].findChild(QLabel,'ligne').setText(stop)
                self.boxArray[i].findChild(QLabel,'time').setText(params[i+3])