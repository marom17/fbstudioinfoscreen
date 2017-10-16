# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 16.10.2017
__Name__: uiMeteoForcast.py
__Description__: Display forcast

"""
from PyQt5.QtWidgets import QFrame, QLabel, QGridLayout
from signals import eventSignals
from PyQt5.QtGui import QFont, QPixmap
import config
from PyQt5.QtCore import Qt

class UIMeteoForecast(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setMinimumSize(parent.width(), parent.height()/3)
        self.setStyleSheet("background-color:#d6d6c2")
        
        self.layout = QGridLayout(self)
        self.layout.setAlignment(Qt.AlignVCenter)
        
        self.drawMeteo()
        
        self.setLayout(self.layout)
        
        eventSignals.meteoForecast.connect(self.updateForecast)
        
    '''
    Draw frame
    '''
    def drawMeteo(self):
        
        wulogo = QPixmap("ressources/meteopics/wulogo.png")
        logoLabel = QLabel('')
        logoLabel.setPixmap(wulogo.scaled(107, 107, Qt.KeepAspectRatio))
        logoLabel.setMaximumSize(107, 107)
        self.layout.addWidget(logoLabel,0,0)
        
        temp = QLabel('min/max (°C)')
        temp.setAlignment(Qt.AlignRight)
        
        wind = QLabel('wind')
        wind.setAlignment(Qt.AlignRight)
        
        hum = QLabel('humidity')
        hum.setAlignment(Qt.AlignRight)
        
        self.layout.addWidget(temp,2,0)
        self.layout.addWidget(wind,3,0)
        self.layout.addWidget(hum,4,0)
        
        for i in range(0,5):
            for y in range(1,5):
                label = QLabel(self)
                label.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(label,i,y)
    
    '''
    Update the meteo
    '''
    def updateForecast(self,params):
        for i in range(1,5):
            try:
                label = self.layout.itemAtPosition(0, i).widget()
                label.setPixmap(QPixmap(config.picfolder+params[i-1][0]+".gif"))
                
                label = self.layout.itemAtPosition(1, i).widget()
                label.setText(params[i-1][1])
                
                label = self.layout.itemAtPosition(2, i).widget()
                label.setText(params[i-1][3]+"/"+params[i-1][2])
                
                label = self.layout.itemAtPosition(3, i).widget()
                label.setText(params[i-1][4])
                
                label = self.layout.itemAtPosition(4, i).widget()
                label.setText(params[i-1][5])
                
            except:
                print("Error params")
        