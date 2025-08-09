# Library Imports
import ctypes
import os
import sys
import time
from PyQt6.QtWidgets import QApplication
import settings
# Self-imports
from api_calls import Api_Calls
from file_funcs import File_Processing
from settings import User_Settings

app = QApplication(sys.argv)

User_Settings.config_check()
monitor_res = str(User_Settings.get_screen_info().width) + 'x' + str(User_Settings.get_screen_info().height)


source = Api_Calls.call_wallhaven_api(resolution=monitor_res,
                                      query=settings.User_Settings.retrieve_user_settings()[2], )
File_Processing.image_resize(source)

absolute = os.path.abspath(
    f'C:/Users/Corentin/Pictures/Wallpapers/{source[0]}/resized_file/{source[1]}')  # TODO:Create adaptative path

time.sleep(1)

ctypes.windll.user32.SystemParametersInfoW(
    # This changes Windows's wallpaper, the 4th argument has to be 3 to update and lock wallpaper beyond reboot
    20,
    0,
    absolute,
    3
)
