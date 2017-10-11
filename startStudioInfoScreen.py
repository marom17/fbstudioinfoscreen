"""
__Author__: Romain Maillard
__Date__: 11.10.2017
__Name__: startStudioInfoScreen.py
__Description__: Start the studio info screen

"""
from PyQt5.QtWidgets import QApplication, QWidget
import sys
import config
from controller import MainController


app = QApplication(sys.argv)

print("Start Info Display")

ui = QWidget()
controller = MainController()
controller.start()
ui.show()
app.exec_()
controller.stop()
controller.wait()

print("Stop Info Display")