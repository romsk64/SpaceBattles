import json
import subprocess
from random import randint
import pygame
from pygame._sdl2 import Window
import sys
from modules import gl, romconst

pygame.init()

def menuWindowInit():
    pygame.display.set_caption(f"{romconst.langName}")
    Window.from_display_module().maximize()
    romconst.mw.fill(romconst.C_WHITE)

menuCycle_ = True
starList = [[], []]
for i in range(romconst.opt_graphic_starcount):
    starList[0].append(None)
    starList[1].append(None)

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
        global menuCycle_
        
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
                    romconst.toOptions = True
                    romconst.toMenu = False
                    menuCycle_ = False
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