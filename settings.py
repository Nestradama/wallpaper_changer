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
    def changer_user_settings(query): #Used when user wants to change wallpaper query
        config.read('config.ini')
        config.set("API_SETTINGS", "query", query)
        config.write(open('config.ini', 'w'))

    @staticmethod
    def set_user_settings(keytype, key, query='space', window_instance=None):
        monitor_res = str(User_Settings.get_screen_info().width) + 'x' + str(User_Settings.get_screen_info().height)

        config.read('config.ini')
        if not config.has_section("API_KEYS"):
            config.add_section("API_KEYS")
            config.set("API_KEYS", keytype, key)
            config.write(open('config.ini', 'w'))
        else:
            config.set("API_KEYS", keytype, key)
            config.write(open('config.ini', 'w'))

        if not config.has_section("API_SETTINGS"):
            print("No section")
            config.add_section("API_SETTINGS")
            config.write(open('config.ini', 'w'))
        else:
            config.set("API_SETTINGS", "query", query)
            config.set("PROGRAM_VALUES", "first_launch", "False")
            config.set("API_SETTINGS", "sorting", "random")
            config.set("API_SETTINGS", "resolution", monitor_res)
            config.set("API_SETTINGS", "source", keytype)
            config.write(open('config.ini', 'w'))
            window_instance.close()

    @staticmethod
    def retrieve_user_settings():
        config.read('config.ini')
        config_data = {}
        for section in config.sections():
            config_data[section] = {}
            for key in config[section]:
                config_data[section][key] = config[section][key]
        return config_data

    @staticmethod
    def setup_values():
        try:
            config.read('config.ini')
            config.add_section("PROGRAM_VALUES")
            config.set("PROGRAM_VALUES", "first_launch", "False")
            config.add_section("API_KEYS")
            config.add_section("API_SETTINGS")
            config.write(open('config.ini', 'w'))
            print("Setup complete")
        except Exception as e:
            print(e)

    @staticmethod
    def config_check():  # Check if first launch to initialize sections with setup_values
        config.read('config.ini')

        if config.has_section("PROGRAM_VALUES") and config.has_option("PROGRAM_VALUES", "first_launch"):
            firstlaunch = config.get("PROGRAM_VALUES", "first_launch")
            if firstlaunch == "False":

                gui.GUI.query_selection()
            else:
                config.set("PROGRAM_VALUES", "first_launch", "False")
                User_Settings.setup_values()
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
