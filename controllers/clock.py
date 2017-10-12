"""
__Author__: Romain Maillard
__Date__: 12.10.2017
__Name__: clock.py
__Description__: Update the time

"""
from PyQt5.QtCore import QThread

class MyClass(QThread):
    '''
    classdocs
    '''


    def __init__(self, params):
        super().__init__()
        