# -*- coding: utf-8 -*-
"""
__Author__: Romain Maillard
__Date__: 17.10.2017
__Name__: music.py
__Description__: Search the last musics of the radio

"""
from PyQt5.QtCore import QThread
from signals import eventSignals

class MusicControl(QThread):
    '''
    classdocs
    '''


    def __init__(self):
        super().__init__()
        self.running = True
        
    def run(self):
        
        while(self.running):
            
            self.msleep(500)
            
    def stop(self):
        self.running = False
        
    '''
    Fetch the music from database
    '''
    def getMusic(self):
        pass