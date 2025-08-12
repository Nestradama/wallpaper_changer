import ctypes
import glob
import os
from ctypes import wintypes
from PIL import Image


class File_Processing:
    def __init__(self):
        pass

    @staticmethod
    def find_latest_file(websource):  # Used to assign wallpaper, independent from filename
        list_of_files = glob.glob(f'C:/Users/Corentin/Pictures/Wallpapers/{websource}/original_file/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return str(latest_file)

    @staticmethod
    def image_resize(websource, file):
        try:
            img = Image.open(File_Processing.find_latest_file(websource))
            new_img = img.resize((1920, 1080))
            os.makedirs(f'C:/Users/Corentin/Pictures/Wallpapers/{websource}/resized_file', exist_ok=True)
            new_img.save(f'C:/Users/Corentin/Pictures/Wallpapers/{websource}/resized_file/{file}',
                         format='PNG')

        except Exception as e:
            print(e)


class OS_Interaction:
    def __init__(self):
        pass

    @staticmethod
    def get_picture_path():
        buffer = ctypes.create_unicode_buffer(wintypes.MAX_PATH)

        ctypes.windll.shell32.SHGetFolderPathW(None, 0x27, None, 0, buffer) #0x27 = Picture Folder
        return buffer.value

    @staticmethod
    def set_wallpaper(filepath):
        ctypes.windll.user32.SystemParametersInfoW(
            # This changes Windows's wallpaper, the 4th argument has to be 3 to update and lock wallpaper beyond reboot
            20,
            0,
            filepath,
            3
        )
