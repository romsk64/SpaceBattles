import json
import pygame
from pygame._sdl2 import Window
import rompgl

# json options
json_resolution_width = 1280
json_resolution_height = 720
opt_resolution = (json_resolution_width, json_resolution_height)
opt_fullscreen = False

pygame.init()

mw = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Space Battles")
Window.from_display_module().maximize()
exit_ = False
mainCycle_ = True

test_text = rompgl.Text("Test", "Arial", 20, (255, 255, 255), 500, 350, mw)
test_text.drawText()
# chSingleplayer = rompgl.Button(mw)
# chMultiplayer = rompgl.Button(mw)

while mainCycle_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit_ = True
            break
    if exit_:
        break
    
    pygame.display.update()