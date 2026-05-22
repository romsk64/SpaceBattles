import pygame
import modules.gl as gl
import modules.romconst as romconst

pygame.init()

def gameWindowInit():
    global gameCycle_

    gameCycle_ = True
    pygame.display.set_caption(f"{romconst.langName}: {romconst.langNameSingleplayer}")

def game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)