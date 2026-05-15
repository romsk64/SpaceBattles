# import subprocess
import pygame
import modules.menu as menu
import modules.options as options
import modules.romconst as romconst
# import modules.lang as lang

pygame.init()

if __name__ == "__main__":
    if romconst.toMenu == True:
        menu.menuWindowInit()
        while menu.menuCycle_:
            menu.cycle()
    elif romconst.toOptions == True:
        options.optionsWindowInit()
        while options.optionsCycle_:
            pass