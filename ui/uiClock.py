# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiClock.py
__Description__: Display the time

"""

from PyQt5.QtWidgets import QFrame, QWidget, QLabel, QGridLayout, QHBoxLayout,\
    QSpacerItem, QWidgetAction
from signals import eventSignals
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
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
        
        self.font = QFont(family,50)
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setAlignment(Qt.AlignTop)
        
        self.drawTop()
        self.drawBottom()
        self.drawMeteo()
        
        eventSignals.time.connect(self.updateTime)
        eventSignals.meteoCondition.connect(self.updateMeteo)
        
        self.setLayout(self.gridLayout)
        self.show()
        
    '''
    Draw the 
    '''
    def drawTop(self):
        self.date = QLabel('',self)
        self.date.setFont(self.font)
        self.date.setStyleSheet("color:red")
        self.date.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.date,0,0)
        self.gridLayout.setAlignment(self.date,Qt.AlignCenter)
    
    '''
    Draw the bottom clock
    '''
    def drawBottom(self):
        self.time = QLabel('',self)
        self.time.setFont(self.font)
        self.time.setStyleSheet("color:red")
        self.time.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.time,1,0)
        self.gridLayout.setAlignment(self.time,Qt.AlignCenter)
        
        
    '''
    Draw the meteo condition
    '''
    def drawMeteo(self):
        box = QFrame(self)
        hbox = QHBoxLayout(self)
        font = QFont("Times new romand",30)
        hbox.setAlignment(Qt.AlignCenter)
        for i in range(0,3):
            label = QLabel(self)
            label.setStyleSheet("color:red;")
            label.setFont(font)
            label.setAlignment(Qt.AlignCenter)
            hbox.addWidget(label)
        
        box.setLayout(hbox)
        
        self.gridLayout.addWidget(box,2,0)
        
    '''
    Update the time
    '''
    def updateTime(self,date,time):
        self.date.setText(date)
        self.time.setText(time)
        
    '''
    Update the meteo condition
    '''
    def updateMeteo(self,params):
        if(len(params) != 0):
            box = self.gridLayout.itemAtPosition(2,0).widget()
            box.layout().itemAt(0).widget().setText(params[0])
            try:
                box.layout().itemAt(1).widget().setPixmap(QPixmap("ressources/meteopics/"+params[1]+".gif"))
            except:
                print("Image error")
            box.layout().itemAt(2).widget().setText(str(params[2])+"°C")
        