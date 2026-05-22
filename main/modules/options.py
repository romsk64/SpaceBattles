import json
import pygame
from pygame._sdl2 import Window
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
import modules.romconst as romconst
import modules.menu as menu

# optionsCycle_ = True

# json_resolution_width = 1920
# json_resolution_height = 1017
# opt_resolution = (json_resolution_width, json_resolution_height)
# opt_fullscreen = False
# opt_graphic_starcount = 250

pygame.init()
new_options_dict = dict()

def optionsWindowInit():
    global optionsCycle_

    optionsCycle_ = True
    pygame.display.set_caption("Options")
    # Window.from_display_module().maximize()
    # romconst.mw.fill(romconst.C_DARK_GRAY)

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
    global new_options_dict

    new_options_dict = romconst.json_options_dict

def options():
    for event in pygame.event.get():
        global optionsCycle_

        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                romconst.toMenu = True
                romconst.toOptions = False
                optionsCycle_ = False
            if event.key == pygame.K_KP_PLUS:
                romconst.new_options_dict = new_options_dict
    
    menu.bg_move(romconst.mw)

    pygame.display.update()