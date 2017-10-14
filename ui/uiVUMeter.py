# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 14.10.2017
__Name__: uiVUMeter.py
__Description__: Display a VU meter

"""
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QWidget
from PyQt5.QtCore import Qt

class UIVuMeter(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        
        self.setParent(parent)
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setAlignment(Qt.AlignCenter)
        
        self.styleSheetArray = {}
        self.styleSheetArray["red"] = "background-color:red"
        self.styleSheetArray["yellow"] = "background-color:yellow"
        self.styleSheetArray["lime"] = "background-color:lime"
        self.styleSheetArray["noRed"] = "background-color:#4d0000"
        self.styleSheetArray["noYellow"] = "background-color:#4d4d00"
        self.styleSheetArray["noLime"] = "background-color:#003300"
        
        self.dbTab = ["+8","+6","+4","+2","0","-2","-4","-8","-12","-16","-20","-28","-40","-60"]
        
        self.drawVuMeter()
        
        self.setLayout(self.gridLayout)
        
    '''
    Draw the vu meter
    '''
    def drawVuMeter(self):
        self.drawNumber(0)
        self.drawLed(1)
        self.drawLed(2)
        self.drawNumber(3)
    
    '''
    Draw the numbers
    '''
    def drawNumber(self,column):    
        i=0
        for db in self.dbTab:
            label = QLabel(db,self)
            label.setAlignment(Qt.AlignRight)
            label.setStyleSheet("color:white")
            self.gridLayout.addWidget(label,i,column)
            i = i+1
            
    def drawLed(self,column):
        for i in range(0,len(self.dbTab)):
            led = QWidget(self)
            led.setMinimumSize(20, 5)
            if(i<2):
                led.setStyleSheet(self.styleSheetArray["noRed"])
            elif(i<4):
                led.setStyleSheet(self.styleSheetArray["noYellow"])
            else:
                led.setStyleSheet(self.styleSheetArray["noLime"])
            
            self.gridLayout.addWidget(led,i,column)