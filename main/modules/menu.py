import json
import subprocess
from random import randint
import pygame
from pygame._sdl2 import Window
import sys
# import rompgl
import main.modules.gl as gl
from main.modules.romconst import *

# json options
json_resolution_width = 1920
json_resolution_height = 1017
opt_resolution = (json_resolution_width, json_resolution_height)
opt_fullscreen = False
opt_graphic_starcount = 250

pygame.init()

mw = pygame.display.set_mode(opt_resolution, pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Space Battles")
Window.from_display_module().maximize()
mw.fill(C_WHITE)
menuCycle_ = True
starList = [[], []]
for i in range(opt_graphic_starcount):
    starList[0].append(None)
    starList[1].append(None)

titleText = gl.Text("Space Battles", "resourses/fonts/spaceagecyrillic_regular.ttf", 50, C_WHITE, 25, 25, mw)
versionText = gl.Text(f"Version: {VERSION_STR}", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 25, 980, mw)
btnSingleplayer = gl.Button(mw, 25, 250, 350, 30, C_DARK_PURPLE, "Играть с ботами", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 30, 250)
btnMultiplayer = gl.Button(mw, 25, 300, 350, 30, C_DARK_PURPLE, "Играть на сервере", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 30, 300)
btnOptions = gl.Button(mw, 25, 400, 350, 30, C_DARK_PURPLE, "Настройки", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 30, 400)
btnExit = gl.Button(mw, 25, 450, 350, 30, C_DARK_PURPLE, "Выйти", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 30, 450)

def game_drawbg(bg):
    # пока генерация фона, потом сделаю нормальную картинку или нормальный шум по которому будет фон
    global starList
    global opt_graphic_starcount

    bg.fill(C_BLACK)

    for i in range(opt_graphic_starcount):
        starList[0][i - 1] = randint(0, json_resolution_width) # x
        starList[1][i - 1] = randint(0, json_resolution_height) # y
        pygame.draw.rect(bg, C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))
    pygame.display.update()
def bg_move(bg):
    global starList
    global opt_graphic_starcount
    
    bg.fill(C_BLACK)

    for i in range(opt_graphic_starcount):
        starList[1][i - 1] -= 1
        pygame.draw.rect(bg, C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))

        if starList[1][i - 1] <= -1:
            starList[1][i - 1] += json_resolution_height

game_drawbg(mw)

def cycle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP2:
                game_drawbg(mw)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if btnSingleplayer.clicking(x, y):
                    pass
                elif btnMultiplayer.clicking(x, y):
                    pass
                elif btnOptions.clicking(x, y):
                    # subprocess.run(["python", "settings.py"])
                    # processErr = subprocess.Popen([sys.executable, "settings.py"], stderr = subprocess.PIPE, text = True).communicate()
                    # if processErr:
                    #     print(f"Errors: {processErr}")
                    pass
                elif btnExit.clicking(x, y):
                    exit(0)

    bg_move(mw)
    titleText.drawText()
    versionText.drawText()
    btnSingleplayer.drawButton(True)
    btnMultiplayer.drawButton(True)
    btnOptions.drawButton(True)
    btnExit.drawButton(True)
    
    pygame.display.update()