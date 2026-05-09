import modules.gl as gl
import json
import pygame

C_RED = (255, 0, 0)
C_GREEN = (0, 255, 51)
C_YELLOW = (255, 255, 0)
C_BLUE = (0, 0, 100)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_LIGHT_GRAY = (211, 211, 211)
C_DARK_GRAY = (100, 100, 100)
C_GRAY = (128, 128, 128)
C_PURPLE = (128, 0, 128)
C_DARK_PURPLE = (48, 25, 52)

EN_EN = 0
RU_RU = 1
US_EN = 2
RU_KY = 3 # калмыцкий язык

VERSION = 0.1
VERSION_STR = str(VERSION)

# json settings
json_resolution_width = 1920
json_resolution_height = 1017
opt_resolution = (json_resolution_width, json_resolution_height)
opt_fullscreen = False
opt_graphic_starcount = 250

mw = pygame.display.set_mode(opt_resolution, pygame.SCALED | pygame.RESIZABLE)

# menu
titleText = gl.Text("Space Battles", "resourses/fonts/spaceagecyrillic_regular.ttf", 50, C_WHITE, 25, 25, mw)
versionText = gl.Text(f"Version: {VERSION_STR}", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 25, 980, mw)
btnSingleplayer = gl.Button(mw, 25, 250, 350, 30, C_DARK_PURPLE, "Играть с ботами", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 250)
btnMultiplayer = gl.Button(mw, 25, 300, 350, 30, C_DARK_PURPLE, "Играть на сервере", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 300)
btnOptions = gl.Button(mw, 25, 400, 350, 30, C_DARK_PURPLE, "Настройки", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 400)
btnExit = gl.Button(mw, 25, 450, 350, 30, C_DARK_PURPLE, "Выйти", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 450)

# menu on escape
btnExitMenu = None