import json
from random import randint
import pygame
from pygame._sdl2 import Window
import rompgl
from romconst import *

# json options
json_resolution_width = 1920
json_resolution_height = 1017
set_resolution = (json_resolution_width, json_resolution_height)
set_fullscreen = False
set_graphic_starcount = 250

pygame.init()

mw = pygame.display.set_mode(set_resolution, pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Space Battles")
Window.from_display_module().maximize()
mw.fill(C_WHITE)
exit_ = False
mainCycle_ = True
starList = [[], []]
for i in range(set_graphic_starcount):
    starList[0].append(None)
    starList[1].append(None)

titleText = rompgl.Text("Space Battles", "resourses/fonts/spaceagecyrillic_regular.ttf", 50, C_WHITE, 25, 25, mw)
# chSingleplayer = rompgl.Button(mw)
# chMultiplayer = rompgl.Button(mw)

def game_drawbg(bg):
    # пока генерация фона, потом сделаю нормальную картинку или нормальный шум по которому будет фон
    global starList
    global set_graphic_starcount

    bg.fill(C_BLACK)

    for i in range(set_graphic_starcount):
        starList[0][i - 1] = randint(0, json_resolution_width) # x
        starList[1][i - 1] = randint(0, json_resolution_height) # y
        pygame.draw.rect(bg, C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))
    pygame.display.update()
def bg_move(bg):
    global starList
    global set_graphic_starcount
    
    bg.fill(C_BLACK)

    for i in range(set_graphic_starcount):
        starList[1][i - 1] -= 1
        pygame.draw.rect(bg, C_WHITE, pygame.rect.Rect(starList[0][i - 1], starList[1][i - 1], 3, 3))

        if starList[1][i - 1] <= -1:
            starList[1][i - 1] += json_resolution_height
        


game_drawbg(mw)
titleText.drawText()

while mainCycle_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit_ = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP2:
                game_drawbg(mw)
                titleText.drawText()
    if exit_:
        break

    bg_move(mw)
    titleText.drawText()
    
    pygame.display.update()