import ctypes
import glob
import os
from ctypes import wintypes
from PIL import Image
from time import sleep


class File_Processing:
    def __init__(self):
        pass

    @staticmethod
    def old_file_deletion(websource):  # TODO: Implement this in settings
        list_of_files = glob.glob(f'C:/Users/Corentin/Pictures/Wallpapers/{websource}/original_file/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        for file in list_of_files:
            if file != latest_file:
                os.remove(file)

    @staticmethod
    def find_latest_file(websource):  # Used to assign wallpaper, independent from filename
        list_of_files = glob.glob(f'C:/Users/Corentin/Pictures/Wallpapers/{websource}/original_file/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
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

    @staticmethod
    def gif_convert(filepath):
        gif_file = Image.open(filepath)
        gif_file.save(filepath.replace('.gif', '.png'), format='PNG')


class OS_Interaction:
    def __init__(self):
        pass

    @staticmethod
    def get_picture_path():
        buffer = ctypes.create_unicode_buffer(wintypes.MAX_PATH)

        ctypes.windll.shell32.SHGetFolderPathW(None, 0x27, None, 0, buffer)  # 0x27 = Picture Folder
        return buffer.value

    @staticmethod
    def get_full_path(source, filename, resized):
        user_pic_folder = OS_Interaction.get_picture_path()
        if resized:
            full_path = f'{user_pic_folder}/Wallpapers/{source}/resized_file/{filename}'
            return full_path
        else:
            full_path = f'{user_pic_folder}/Wallpapers/{source}/original_file/{filename}'
            return full_path

    @staticmethod
    def set_wallpaper(filepath):
        print("I got here")
        sleep(1)
        ctypes.windll.user32.SystemParametersInfoW(
            # This changes Windows's wallpaper, the 4th argument has to be 3 to update and lock wallpaper beyond reboot
            20,
            0,
            filepath,
            3
        )
        print("I changed the wallpaper")
