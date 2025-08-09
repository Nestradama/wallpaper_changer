import glob
import os

from PIL import Image


class File_Processing:
    def __init__(self):
        pass

    @staticmethod
    def find_latest_file(websource): #Used to assign wallpaper, undependant from filename
        list_of_files = glob.glob(f'C:/Users/Corentin/Pictures/Wallpapers/{websource[0]}/original_file/*')
        latest_file = max(list_of_files, key=os.path.getctime)
        return str(latest_file)

    @staticmethod
    def image_resize(websource): #Used by default, useful for source with random res (Nasa)
        try:
            print("I'm here")
            img = Image.open(File_Processing.find_latest_file(websource))
            new_img = img.resize((1920, 1080))
            os.makedirs(f'C:/Users/Corentin/Pictures/Wallpapers/{websource[0]}/resized_file', exist_ok=True)
            new_img.save(f'C:/Users/Corentin/Pictures/Wallpapers/{websource[0]}/resized_file/{websource[1]}',
                         format='PNG')

        except Exception as e:
            print(e)
