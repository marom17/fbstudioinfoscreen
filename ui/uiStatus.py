# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 13.10.2017
__Name__: uiStatus.py
__Description__: Display the studio status

"""
from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from signals import eventSignals

class UIStatus(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setMinimumSize(parent.width()/2, parent.width()/2)
        self.setMaximumSize(parent.width()/2, parent.width()/2)
        self.setStyleSheet("background-color:orange")
        
        self.font = QFont('Times new roman',50)
        self.status = QLabel('Get Info',self)
        self.status.resize(self.width(),self.height())
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setFont(self.font)
        
        eventSignals.status.connect(self.updateStatus)
    
    '''
    Update the status of the antenna
    '''
    def updateStatus(self,params):
        if(len(params) == 0):
            self.setStyleSheet("background-color:yellow")
            self.status.setText('Error')
         
        else:   
            self.status.setText(params[0])
            if(not params[1]):
                self.setStyleSheet("background-color:lime")
            else:
                self.setStyleSheet("background-color:red")
        