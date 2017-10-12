"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: uiNews.py
__Description__: Display news

"""
from PyQt5.QtWidgets import QFrame
from signals import eventSignals

class UINews(QFrame):
    '''
    classdocs
    '''


    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        
        eventSignals.news.connect(self.updateNews)
    
    '''
    Update the new feed
    '''
    def updateNews(self,params): 
        pass