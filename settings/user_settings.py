##Will handle anything related to the settings files
import configparser
from screeninfo import get_monitors

config = configparser.ConfigParser()


class User_Settings:
    def __init__(self):
        pass

    @staticmethod
    def changer_user_settings(query):  # Used when a user wants to change the wallpaper query
        config.read('config.ini')
        config.set("API_SETTINGS", "query", query)
        config.write(open('config.ini', 'w'))

    @staticmethod
    def set_user_settings(keytype, key, query='space', window_instance=None):
        monitor_res = str(User_Settings.get_screen_info().width) + 'x' + str(User_Settings.get_screen_info().height)
        try:
            config.read('config.ini')
            if not config.has_section("API_KEYS"):
                print("No section1")
                config.add_section("API_KEYS")
                config.set("API_KEYS", keytype, key)
                config.write(open('config.ini', 'w'))
            else:
                print("No section2")
                config.set("API_KEYS", keytype, key)
                config.write(open('config.ini', 'w'))

            if not config.has_section("API_SETTINGS"):
                print("No section3")
                config.add_section("API_SETTINGS")
                config.write(open('config.ini', 'w'))
            else:
                print("No section4")
                config.set("API_SETTINGS", "query", query)
                config.set("PROGRAM_VALUES", "first_launch", "False")
                config.set("API_SETTINGS", "sorting", "random")
                config.set("API_SETTINGS", "resolution", monitor_res)
                config.set("API_SETTINGS", "source", keytype)
                config.set("API_SETTINGS", "purity", "sfw")
                config.write(open('config.ini', 'w'))
        except Exception as e:

            print("Settings have failed", e)
            exit()


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
    def check_first_launch():  # Check if first launch to initialize sections with setup_values
        config.read('config.ini')

        if config.has_section("PROGRAM_VALUES") and config.has_option("PROGRAM_VALUES", "first_launch"):
            firstlaunch = config.get("PROGRAM_VALUES", "first_launch")
            if firstlaunch == "False":
                print("Not first launch")
                return False

            else:
                config.set("PROGRAM_VALUES", "first_launch", "False")
                User_Settings.setup_values()
                config.write(open('../config.ini', 'w'))
                return True
        else:
            print("This shouldnt show")
            User_Settings.setup_values()
            return True

    @staticmethod
    def get_screen_info():
        for monitor in get_monitors():
            if monitor.is_primary:  # check if it's the main screen
                return monitor
        return None  # no primary monitor found

    @staticmethod
    def update_settings(updated_data):
        config.read('config.ini')

        for key, value in updated_data.items():
            found = False
            for section in config.sections():
                if key in config[section]:
                    config.set(section, key, value)
                    print(f"Updated {key} to {value}")
                    found = True
            if not found:
                print(f"Key {key} not found in config file")

        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            print("Updated config file")
