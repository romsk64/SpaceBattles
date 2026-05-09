import subprocess
import pygame
import modules.menu as menu
import modules.options as options

pygame.init()

if __name__ == "__main__":
    while menu.menuCycle_:
        menu.cycle()