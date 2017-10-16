"""
__Author__: Romain Maillard
__Date__: 16.10.2017
__Name__: uiMeteoForcast.py
__Description__: Display forcast

"""
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from signals import eventSignals
from PyQt5.QtGui import QFont

class UIMeteoForcast(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setMinimumSize(parent.width(), parent.height()/3)
        self.setStyleSheet("background-color:#d6d6c2")
        
        self.layout = QVBoxLayout(self)
        
        self.drawMeteo()
        
        self.setLayout(self.layout)
        
        eventSignals.meteoForecast.connect(self.updateForcast)
        
    '''
    Draw frame
    '''
    def drawMeteo(self):
        pass
    
    '''
    Update the meteo
    '''
    def updateForcast(self,params):
       print(params)
        