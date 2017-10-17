# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 17.10.2017
__Name__: uiMusic.py
__Description__: Display the last musics

"""
from PyQt5.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QLabel
from signals import eventSignals
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class uiMusic(QFrame):
    '''
    classdocs
    '''


    def __init__(self,parent):
        super().__init__()
        
        self.setParent(parent)
        self.resize(parent.width(),parent.height()/2)
        self.setMaximumSize(parent.width(),parent.height()/2+1)
        self.setStyleSheet("background-color:#d6d6c2")
        eventSignals.music.connect(self.updateMusic)
        
        self.layout = QVBoxLayout(self)
        
        self.drawMusic()
        
        self.setLayout(self.layout)
        
        self.show()
        
       
    def drawMusic(self):
        font = QFont('Times new roman',25)
        title = QLabel('Derniers titres',self)   
        title.setStyleSheet("font-weight: bold;")   
        title.setFont(font)
        self.layout.addWidget(title)  
        
        for i in range(0,5):
            label = QLabel('Artiste titre',self)
            label.setFont(font)
            self.layout.addWidget(label)
            
    
    
    '''
    Update the programmed emission
    ''' 
    def updateMusic(self,params):
        if(len(params) != 0):
            for i in range(0,5):
                self.layout.itemAt(i+1).widget().setText(params[i])