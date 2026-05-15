import json
import modules.romconst as romconst

def load_language():
    if romconst.opt_language == romconst.RU_RU:
        try:
            with open("resourses/langs/ru_ru.json", 'r', encoding = "utf-8") as f:
                lang_dict = json.load(f)
        except FileNotFoundError:
            print("No file \"resourses/langs/ru_ru.json\" in current directory!")
            exit(1)
    elif romconst.opt_language == romconst.EN_US:
        try:
            with open("resourses/langs/en_us.json", 'r', encoding = "utf-8") as f:
                lang_dict = json.load(f)
        except FileNotFoundError:
            print("No file \"resourses/langs/en_en.json\n in current directory!")
            exit(1)
    
    return lang_dict

def load_options():
    try:
        with open("user/options.json", 'r', encoding = "utf-8") as f:
            options_dict = json.load(f)
    except FileNotFoundError:
        print("No file \"user/options.json\" in current directory!")
        exit(1)
    return options_dict