# import subprocess
from pygame._sdl2 import Window
import modules.menu as menu
import modules.options as options
import modules.romconst as romconst
import modules.game as game

# pygame.init()

if __name__ == "__main__":
    mainCycle_ = True

    Window.from_display_module().maximize()
    
    while mainCycle_:
        if romconst.toMenu:
            menu.menuWindowInit()
        elif romconst.toOptions:
            options.optionsWindowInit()
        elif romconst.toGame:

        
        if menu.menuCycle_:
            menu.cycle()
        elif options.optionsCycle_:
            options.options()