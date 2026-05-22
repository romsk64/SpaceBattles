import modules.gl as gl
import modules.json_load as json_load
import json
import pygame

C_RED = (255, 0, 0)
C_GREEN = (0, 255, 51)
C_YELLOW = (255, 255, 0)
C_BLUE = (0, 0, 100)
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_LIGHT_GRAY = (211, 211, 211)
C_DARK_GRAY = (100, 100, 100)
C_GRAY = (128, 128, 128)
C_PURPLE = (128, 0, 128)
C_DARK_PURPLE = (48, 25, 52)

EN_US = 0
RU_RU = 1
# RU_KY = 2 # калмыцкий язык

VERSION = 0.1
VERSION_STR = str(VERSION)

# json settings
json_options_dict = json_load.load_options()
json_resolution_width = json_options_dict['resolution_wid']
json_resolution_height = json_options_dict['resolution_hid']
opt_resolution = (json_resolution_width, json_resolution_height)
opt_fullscreen = json_options_dict['fullscreen']
opt_graphic_starcount = json_options_dict['graphic_starcount']
opt_language = json_options_dict['language']

# language
lang_dict = json_load.load_language() # словарь со всеми словами
langName = lang_dict['name']
langNameOptions = lang_dict['nameOptions']
langNameSingleplayer = lang_dict['nameSingleplayer']
langNameMultiplayer = lang_dict['nameMultiplayer']
langBtnSingleplayer = lang_dict['btnSingleplayer']
langBtnMultiplayer = lang_dict['btnMultiplayer']
langBtnOptions = lang_dict['btnOptions']
langBtnExit = lang_dict['btnExit']
langBtnExitMenu = lang_dict['btnExitMenu']
langBtnOptLang = lang_dict['btnOptLang']

# new options
new_options_dict = dict()

# to menu/options/game
toMenu = True
toOptions = False
toGame = False

mw = pygame.display.set_mode(opt_resolution, pygame.SCALED | pygame.RESIZABLE)

# menu
titleText = gl.Text("Space Battles", "resourses/fonts/spaceagecyrillic_regular.ttf", 50, C_WHITE, 25, 25, mw)
versionText = gl.Text(f"Version: {VERSION_STR}", "resourses/fonts/spaceagecyrillic_regular.ttf", 24, C_WHITE, 25, 980, mw)
btnSingleplayer = gl.Button(mw, 25, 250, 350, 30, C_DARK_PURPLE, f"{langBtnSingleplayer}", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 250)
btnMultiplayer = gl.Button(mw, 25, 300, 350, 30, C_DARK_PURPLE, f"{langBtnMultiplayer}", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 300)
btnOptions = gl.Button(mw, 25, 400, 350, 30, C_DARK_PURPLE, f"{langBtnOptions}", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 400)
btnExit = gl.Button(mw, 25, 450, 350, 30, C_DARK_PURPLE, f"{langBtnExit}", "resourses/fonts/spaceagecyrillic_regular.ttf",
        24, C_WHITE, 30, 450)

# menu on escape
btnExitMenu = None

# options
# ...