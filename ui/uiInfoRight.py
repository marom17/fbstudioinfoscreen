# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 13.10.2017
__Name__: uiInfoRight.py
__Description__: Display the studio status and the UV Meter

"""
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from uiStatus import UIStatus

class UIInfoRight(QFrame):
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
        
        self.layoutInfo = QHBoxLayout(self)
        
        self.drawInfoRight()
        
        self.setLayout(self.layoutInfo)
        
        self.show()
        
    '''
    Draw the frame
    '''
    def drawInfoRight(self):
        
        self.uiStatus = UIStatus(self)
        
        self.layoutInfo.addWidget(self.uiStatus)
        
        self.layoutInfo.setAlignment(self.uiStatus, Qt.AlignLeft)

        