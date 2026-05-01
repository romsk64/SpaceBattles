import pygame

pygame.init()

mw = pygame.display.set_mode((1250, 720))
mainCycle_ = True

while mainCycle_:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mainCycle_ = False
            break