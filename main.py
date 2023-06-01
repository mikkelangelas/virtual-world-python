from PyQt6.QtWidgets import *
from GUI.MainWindow import MainWindow
import sys

virtualWorld = QApplication(sys.argv)
window = MainWindow()
window.show()
virtualWorld.exec()
