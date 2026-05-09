import json
import subprocess
from random import randint
import pygame
from pygame._sdl2 import Window
import sys
# import rompgl
from modules import gl, romconst

# json options
# json_resolution_width = 1920
# json_resolution_height = 1017
# opt_resolution = (json_resolution_width, json_resolution_height)
# opt_fullscreen = False
# opt_graphic_starcount = 250

pygame.init()

def menuWindowInit():
    romconst.mw = pygame.display.set_mode(romconst.opt_resolution, pygame.SCALED | pygame.RESIZABLE)
    pygame.display.set_caption("Space Battles")
    Window.from_display_module().maximize()
    romconst.mw.fill(romconst.C_WHITE)

menuCycle_ = True
starList = [[], []]
for i in range(romconst.opt_graphic_starcount):
    starList[0].append(None)
    starList[1].append(None)

# def menuButtonsInit():
#     romconst.titleText = gl.Text(
#         "Space Battles", "resourses/fonts/spaceagecyrillic_regular.ttf", 50, romconst.C_WHITE, 25, 25, romconst.mw)
#     romconst.versionText = gl.Text(
#         f"Version: {romconst.VERSION_STR}", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, romconst.C_WHITE, 25, 980, romconst.mw)
#     romconst.btnSingleplayer = gl.Button(
#         romconst.mw, 25, 250, 350, 30, romconst.C_DARK_PURPLE, "Играть с ботами", "resourses/fonts/spaceagecyrillic_regular.ttf",
#         24, romconst.C_WHITE, 30, 250)
#     romconst.btnMultiplayer = gl.Button(
#         romconst.mw, 25, 300, 350, 30, romconst.C_DARK_PURPLE, "Играть на сервере", "resourses/fonts/spaceagecyrillic_regular.ttf",
#         24, romconst.C_WHITE, 30, 300)
#     romconst.btnOptions = gl.Button(
#         romconst.mw, 25, 400, 350, 30, romconst.C_DARK_PURPLE, "Настройки", "resourses/fonts/spaceagecyrillic_regular.ttf",
#         24, romconst.C_WHITE, 30, 400)
#     romconst.btnExit = gl.Button(
#         romconst.mw, 25, 450, 350, 30, romconst.C_DARK_PURPLE, "Выйти", "resourses/fonts/spaceagecyrillic_regular.ttf",
#         24, romconst.C_WHITE, 30, 450)

def game_drawbg(bg):
    global starList

    bg.fill(romconst.C_BLACK)

    for i in range(romconst.opt_graphic_starcount):
        starList[0][i - 1] = randint(0, romconst.json_resolution_width) # x
        starList[1][i - 1] = randint(0, romconst.json_resolution_height) # y
        pygame.draw.rect(bg, romconst.C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))
    pygame.display.update()
def bg_move(bg):
    global starList
    
    bg.fill(romconst.C_BLACK)

    for i in range(romconst.opt_graphic_starcount):
        starList[1][i - 1] -= 1
        pygame.draw.rect(bg, romconst.C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))

        if starList[1][i - 1] <= -1:
            starList[1][i - 1] += romconst.json_resolution_height

game_drawbg(romconst.mw)

def cycle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP2:
                game_drawbg(romconst.mw)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if romconst.btnSingleplayer.clicking(x, y):
                    pass
                elif romconst.btnMultiplayer.clicking(x, y):
                    pass
                elif romconst.btnOptions.clicking(x, y):
                    pass
                elif romconst.btnExit.clicking(x, y):
                    exit(0)

    bg_move(romconst.mw)
    romconst.titleText.drawText()
    romconst.versionText.drawText()
    romconst.btnSingleplayer.drawButton(True)
    romconst.btnMultiplayer.drawButton(True)
    romconst.btnOptions.drawButton(True)
    romconst.btnExit.drawButton(True)
    
    pygame.display.update()