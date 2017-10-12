"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiNews.py
__Description__: Display news

"""
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout,\
    QSizePolicy
from signals import eventSignals
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class UINews(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.resize(parent.width()/2,parent.height()/2)
        self.setMinimumSize(parent.width()/3,parent.height()/2)
        self.setMaximumSize(parent.width()/3+1,parent.height()/2+1)
        self.setStyleSheet("background-color:#d6d6c2")
        self.setAutoFillBackground(True)
        
        self.drawNews()
        
        eventSignals.news.connect(self.updateNews)
    
    '''
    Draw the news frame
    '''    
    def drawNews(self):
        self.layoutNews = QVBoxLayout(self)
        self.boxArray = []
        image = QPixmap("ressources/logoRomandie.png")
        logo = QLabel(self)
        logo.setPixmap(image)
        self.layoutNews.addWidget(logo)
        for i in range(0,7):
            box = self.createBox()
            self.boxArray.append(box)
            self.layoutNews.addWidget(box)
            
        self.setLayout(self.layoutNews)
    
    '''
    Create a news box
    '''
    def createBox(self):
        box = QFrame()
        box.resize(self.width(),self.height()/6)
        box.setStyleSheet("background-color:#f5f5ef")
        box.setFrameShape(QFrame.Box)
        font = QFont("Times new roman",15)
        
        layoutBox = QHBoxLayout(box)
        layoutBox.setAlignment(Qt.AlignVCenter)
        layoutBox.setContentsMargins(5, 0, 0, 0)
        
        textTime = QLabel("Get Info",box)
        textTime.setObjectName("time")
        textTime.setAlignment(Qt.AlignLeft)
        textTime.setFont(font)
        textTime.setStyleSheet("color:black")
        textTime.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        textNews = QLabel("",box)
        textNews.setObjectName("news")
        textNews.setAlignment(Qt.AlignLeft)
        textNews.setFont(font)
        textNews.setStyleSheet("color:black")
        
        layoutBox.addWidget(textTime)
        layoutBox.addWidget(textNews)
        
        layoutBox.setAlignment(textTime, Qt.AlignTop)
        layoutBox.setAlignment(textNews, Qt.AlignLeft)
        
        box.setLayout(layoutBox)
        
        return box
    
    '''
    Update the new feed
    '''
    def updateNews(self,params): 
        for i in range(0,7):
            self.boxArray[i].findChild(QLabel,'time').setText(params[i][0])
            self.boxArray[i].findChild(QLabel,'news').setText(params[i][1])