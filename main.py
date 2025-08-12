# Library Imports
import os
import sys
import time

from PyQt6.QtWidgets import QApplication

# Self-imports
from api_functions import Api_Calls
from os_functions import File_Processing, OS_Interaction
from settings import User_Settings


def main():
    app = QApplication(sys.argv)  # Ensures that GUI can run anytime
    User_Settings.config_check()
    config = User_Settings.retrieve_user_settings()

    api_to_call = config['API_SETTINGS']['source'].lower()
    func_name = f'call_{api_to_call}_api'
    func = getattr(Api_Calls, func_name, None)

    if func and callable(func): #Dynamic function call to ensure the right api is called
        source, filename = func(resolution=config['API_SETTINGS']['resolution'],
                                query=config['API_SETTINGS']['query'])
    else:
        raise Exception("Invalid API source")



    File_Processing.image_resize(source, filename)

    user_pic_folder = OS_Interaction.get_picture_path()
    filepath = os.path.abspath(
        f'{user_pic_folder}/Wallpapers/{source}/resized_file/{filename}')  # finds path regardless of user modifications

    time.sleep(1)

    OS_Interaction.set_wallpaper(filepath)


main()
