import json
import pygame
from pygame._sdl2 import Window
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from main.modules.romconst import *

opt_language = RU_RU
exit_to_menu_ = False
mainCycle_ = True

json_resolution_width = 1920
json_resolution_height = 1017
opt_resolution = (json_resolution_width, json_resolution_height)
opt_fullscreen = False
opt_graphic_starcount = 250

pygame.init()

mw = pygame.display.set_mode(opt_resolution, pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Options")
Window.from_display_module().maximize()
mw.fill(C_DARK_GRAY)

# settings = QApplication([])
# mw = QWidget()
# mw.resize(500, 600)
# mw.setWindowTitle("Настройки")
# mw.setStyleSheet("background-color: gray;")

# # vbox = QVBoxLayout()
# setting1 = QLabel("Hi")

# # vbox.addWidget(setting1, alignment = Qt.AlignLeft)

# # mw.setLayout(vbox)
# mw.show()
# settings.exec_()

def saving():
    pass

while mainCycle_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_to_menu_ = True
    if exit_to_menu_:
        pass

    pygame.display.update()