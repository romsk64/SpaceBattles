import subprocess
import pygame
import main.modules.menu as menu
import main.modules.options as options

pygame.init()

if __name__ == "__main__":
    while menu.menuCycle_:
        menu.cycle()