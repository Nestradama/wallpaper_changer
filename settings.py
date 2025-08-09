##Will handle anything related to the settings files
import configparser

from datashader import first

import gui
from screeninfo import get_monitors

config = configparser.ConfigParser()


class User_Settings:
    def __init__(self):
        pass

    @staticmethod
    def changer_user_settings(query):
        config.read('config.ini')
        config.set("API_SETTINGS", "query", query)
        config.write(open('config.ini', 'w'))


    @staticmethod
    def set_user_settings(keytype, key, query='space'):
        config.read('config.ini')
        if not config.has_section("API_KEYS"):
            config.add_section("API_KEYS")
            config.set("API_KEYS", keytype, key)
            config.write(open('config.ini', 'w'))
        else:
            config.set("API_KEYS", keytype, key)
            config.write(open('config.ini', 'w'))

        if not config.has_section("API_SETTINGS"):
            config.add_section("API_SETTINGS")
            config.set("API_SETTINGS", "query", query)
            config.write(open('config.ini', 'w'))
        else:
            config.set("API_SETTINGS", "query", query)
            config.write(open('config.ini', 'w'))

    @staticmethod
    def retrieve_user_settings():
        config.read('config.ini')
        return config.get("API_KEYS", "NASA"), config.get("API_KEYS", "WALLHAVEN"), config.get("API_SETTINGS", "query")

    @staticmethod
    def setup_values():
        try:
            config.read('config.ini')
            config.add_section("PROGRAM_VALUES")
            config.set("PROGRAM_VALUES", "first_launch", "False")
            config.write(open('config.ini', 'w'))
        except Exception as e:
            print(e)

    @staticmethod
    def config_check():  # Check for first launch to initialize sections with setup_values
        config.read('config.ini')

        if config.has_section("PROGRAM_VALUES") and config.has_option("PROGRAM_VALUES", "first_launch"):
            firstlaunch = config.get("PROGRAM_VALUES", "first_launch")
            if firstlaunch == "False":

                gui.GUI.query_selection()
            else:
                config.set("PROGRAM_VALUES", "first_launch", "False")
                config.write(open('config.ini', 'w'))
                gui.Program_Setup.is_first_launch()
        else:
            User_Settings.setup_values()
            gui.Program_Setup.is_first_launch()

    @staticmethod
    def get_screen_info():
        for monitor in get_monitors():
            if monitor.is_primary:  # check if it's the main screen
                return monitor
        return None  # no primary monitor found
