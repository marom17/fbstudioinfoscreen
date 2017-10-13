# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiBroadcast.py
__Description__: Display the next broadcast

"""
from PyQt5.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QLabel
from signals import eventSignals
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class uiBroadcast(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        
        self.numberOfBroadcast = 0
        
        self.setParent(parent)
        self.resize(parent.width(),parent.height()/2)
        self.setMaximumSize(parent.width(),parent.height()/2+1)
        self.setStyleSheet("background-color:#d6d6c2")
        eventSignals.broadcast.connect(self.updateBroadCast)
        
        self.layout = QVBoxLayout(self)
        
        self.drawBroadcast()
        
        self.setLayout(self.layout)
        
        self.show()
        
       
    def drawBroadcast(self):
        
        self.noBroadcast = QLabel("Pas d'émission programmée",self)
        #self.noBroadcast.move(0,self.height()/2-self.noBroadcast.height()/2)
        self.noBroadcast.setAlignment(Qt.AlignCenter)
        self.noBroadcast.setMinimumSize(self.width(),self.height())
        
        font = QFont("Times new roman",25)
        self.noBroadcast.setFont(font)
        
        self.title = QLabel('Prochaines émissions')
        self.font = QFont('Times new romand',15)
        self.title.setFont(self.font)
        
        self.layout.addWidget(self.title)
        self.layout.setAlignment(self.title, Qt.AlignTop)
        
        self.arrayBox = []
        for i in range(0,3):
            self.arrayBox.append(self.createBox())
    '''
    Create the box that have the broadcast info
    '''
    def createBox(self):
        box = QFrame(self)
        #box.setMinimumSize(self.width(), self.height()/3)
        box.setMaximumSize(self.width(), self.height()/3)
        box.setStyleSheet("background-color:yellow")
        box.setAutoFillBackground(True)
        box.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        box.setStyleSheet("background-color:#f5f5ef")
        box.setFrameShape(QFrame.Box)
        
        
        font = QFont("Times new roman",15)
        
        layout = QVBoxLayout(box)
        layout.setContentsMargins(5, 0, 0, 5)
        
        date = QLabel('',box)
        date.setObjectName('date')
        date.setFont(font)
        date.setStyleSheet("font-weight: bold;")
        
        name = QLabel('',box)
        name.setObjectName('name')
        name.setFont(font)
        
        layout.addWidget(date)
        layout.addWidget(name)
        layout.setAlignment(date, Qt.AlignTop)
        layout.setAlignment(name, Qt.AlignBottom)
        
        box.setLayout(layout)
        
        self.layout.addWidget(box)
        #layout.setAlignment(box,Qt.AlignTop)
        box.hide()
        
        return box
    
    '''
    Hide a number of box
    '''
    def hideBox(self,num):
        for i in range(0,num):
            self.arrayBox[self.numberOfBroadcast-i].hide()
    '''
    Show a number of box
    '''
    def showBox(self,num):
        for i in range(0,num):
            self.arrayBox[i].show()
    
    '''
    Update the programmed emission
    ''' 
    def updateBroadCast(self,params):
        
        if(len(params) != 0):
            self.noBroadcast.hide()
            
        for i in range(0,len(params)):
            self.arrayBox[i].findChild(QLabel,'name').setText(params[i][0])
            self.arrayBox[i].findChild(QLabel,'date').setText(params[i][1])
            
        if(len(params) != self.numberOfBroadcast):
            if(len(params) < self.numberOfBroadcast):
                self.hideBox(len(params)-self.numberOfBroadcast)
            else:
                self.showBox(len(params))
        
        self.numberOfBroadcast = len(params)
        if(len(params) == 0):
            self.noBroadcast.show()
        #print(params)