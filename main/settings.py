import json
# import pygame
# from pygame._sdl2 import Window
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from romconst import *

opt_language = RU_RU
settings = QApplication([])
mw = QWidget()
mw.resize(500, 600)
mw.setWindowTitle("Настройки")
mw.setStyleSheet("background-color: gray;")

# vbox = QVBoxLayout()
setting1 = QLabel("Hi")

# vbox.addWidget(setting1, alignment = Qt.AlignLeft)

# mw.setLayout(vbox)
mw.show()
settings.exec_()