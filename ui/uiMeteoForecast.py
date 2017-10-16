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
        
        self.drawMeteo()
        
        self.setLayout(self.layout)
        
        eventSignals.meteoForecast.connect(self.updateForecast)
        
    '''
    Draw frame
    '''
    def drawMeteo(self):
        pic1 = QLabel(self)
        pic2 = QLabel(self)
        pic3 = QLabel(self)
        
        day1 = QLabel(self)
        day2 = QLabel(self)
        day3 = QLabel(self)
        
        temp1 = QLabel(self)
        temp2 = QLabel(self)
        temp3 = QLabel(self)

        
        self.layout.addWidget(pic1,0,0)
        self.layout.addWidget(pic2,1,0)
        self.layout.addWidget(pic3,2,0)
        
        self.layout.addWidget(day1,0,1)
        self.layout.addWidget(day2,1,1)
        self.layout.addWidget(day3,2,1)
        
        self.layout.addWidget(temp1,0,2)
        self.layout.addWidget(temp2,1,2)
        self.layout.addWidget(temp3,2,2)
    
    '''
    Update the meteo
    '''
    def updateForecast(self,params):
        for i in range(0,3):
            try:
                label = self.layout.itemAtPosition(0, i).widget()
                label.setPixmap(QPixmap(config.picfolder+params[i][0]+".gif"))
                
                label = self.layout.itemAtPosition(1, i).widget()
                label.setText(params[i][1])            
                
                label = self.layout.itemAtPosition(2, i).widget()
                label.setText(params[i][2]+"/"+params[i][3])
            except:
                print("Error params")
        