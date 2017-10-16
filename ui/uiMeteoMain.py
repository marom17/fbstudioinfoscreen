# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 16.10.2017
__Name__: uiMeteoMain.py
__Description__: Display the meteo information

"""
from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from signals import eventSignals
from uiMeteoText import UIMeteoText
from uiMeteoForecast import UIMeteoForecast

class UIMeteoMain(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        
        self.setParent(parent)
        self.resize(parent.width()/2,parent.height()/2)
        self.setMinimumSize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:black")
        self.setAutoFillBackground(True)
        
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.drawMeteo()
        
        self.setLayout(self.layout)
        
        self.show()
        
    '''
    Draw the meteo frame
    '''
    def drawMeteo(self):
        self.meteoforecast = UIMeteoForecast(self)
        self.meteoprediction = UIMeteoText(self)
        
        self.layout.addWidget(self.meteoforecast)
        self.layout.addWidget(self.meteoprediction)
        
        