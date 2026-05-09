import json
import modules.romconst as romconst

def load_language():
    if romconst.opt_language == romconst.RU_RU:
        with open("resourses/langs/ru_ru.json", 'r', encoding = "utf-8") as f:
            lang_dict = json.load(f)
    elif romconst.opt_language == romconst.EN_US:
        with open("resourses/langs/en_us.json", 'r', encoding = "utf-8") as f:
            lang_dict = json.load(f)
    
    return lang_dict

def load_settings():
    pass