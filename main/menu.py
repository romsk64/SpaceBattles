import pygame
import rompgl

pygame.init()

mw = pygame.display.set_mode((1250, 720))
mainCycle_ = True

while mainCycle_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mainCycle_ = False
            break
    
    # if exit_:
    #     break
    
    pygame.display.update()