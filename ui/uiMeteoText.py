"""
__Author__: Romain Maillard
__Date__: 16.10.2017
__Name__: uiMeteoText.py
__Description__: Display the meteo textual prediction

"""
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from signals import eventSignals
from PyQt5.QtGui import QFont

class UIMeteoText(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setMinimumSize(parent.width(), 2*parent.height()/3)
        self.setStyleSheet("background-color:#d6d6c2")
        
        self.layout = QVBoxLayout(self)
        
        self.drawMeteo()
        
        self.setLayout(self.layout)
        
        eventSignals.meteoText.connect(self.updateMeteoText)
        
    '''
    Draw the frames
    '''
    def drawMeteo(self):
        font = QFont("Times new romand",15)
        
        self.title1 = QLabel('',self)
        self.text1 = QLabel('',self)
        
        self.title1.setFont(font)
        self.text1.setFont(font)
        
        self.title1.setStyleSheet("font-weight: bold;")
        
        self.title1.setMaximumWidth(self.width())
        self.text1.setMaximumWidth(self.width())
        
        self.text1.setWordWrap(True)
        
        self.layout.addWidget(self.title1)
        self.layout.addWidget(self.text1)
        
    
    '''
    Update the textual prediction
    '''
    def updateMeteoText(self,params):
        if(len(params) != 0):
            self.title1.setText(params[0])
            self.text1.setText(params[1])