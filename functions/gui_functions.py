from functions import api_functions as api_func
from functions.os_functions import File_Processing, OS_Interaction
from settings.user_settings import User_Settings


class GUIFunctions:
    def __init__(self):
        pass

    @staticmethod
    def change_wallpaper(query=''):
        print(f'Working in change wallpaper with query: {query}')
        if query == '':
            query = User_Settings.retrieve_user_settings()['API_SETTINGS']['query']
        try:
            User_Settings.changer_user_settings(query)
            print("A")
            source, filename = api_func.Api_Calls().call_api()
            print("B")
            File_Processing.image_resize(source, filename)
            print("C")
            OS_Interaction.set_wallpaper(File_Processing.find_latest_file(source))
            print("D")
        except Exception as e:
            print("Went wrong", e)

    @staticmethod
    def agglomerate_data(settings_dict):
        print(settings_dict)
        updated_data = {
            "wallhaven_api_key": settings_dict['wallhaven_api_key'].text(),
            "query": settings_dict['query'].text(),
            "source": settings_dict['source'].text(),
            "sorting": settings_dict['sorting'].currentText().lower(),
            "resolution": settings_dict['resolution'].text(),
            "purity": settings_dict['purity'].currentText().lower()
        }
        User_Settings.update_settings(updated_data)

