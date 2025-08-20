import datetime
import os
import requests

from functions.os_functions import File_Processing
from settings import user_settings
import issue_handler


class Api_Calls:
    def __init__(self):
        self.user_config = user_settings.User_Settings.retrieve_user_settings()

    def call_api(self):
        api_to_call = self.user_config['API_SETTINGS']['source'].lower()
        resolution = self.user_config['API_SETTINGS']['resolution']
        query = self.user_config['API_SETTINGS']['query']
        sorting = issue_handler.api_sorting_set(self.user_config['API_SETTINGS']['sorting'])
        print(sorting)
        purity = issue_handler.api_purity_set(self.user_config['API_SETTINGS']['purity'])
        print(purity)


        func_name = f'call_{api_to_call}_api'
        func = getattr(self, func_name, None)
        try:
            if func and callable(func):
                return func(resolution=resolution, query=query, sorting=sorting, purity=purity)
            else:
                raise Exception("Invalid API source")
        except Exception as e:
            print(e)
            exit()

    @staticmethod
    def call_nasa_api():
        nasa_api_key = user_settings.User_Settings.retrieve_user_settings()[0]
        url = 'https://api.nasa.gov/planetary/apod?api_key='
        og_file = f'original_file/nasa_potd_{datetime.today().strftime('%Y_%m_%d')}.jpg'
        os.makedirs('nasa/original_file', exist_ok=True)
        api_call = requests.get(url + nasa_api_key)
        data = api_call.json()

        response = requests.get(data['hdurl'])
        filename = og_file.replace('original_file/', '')
        if filename.endswith(".gif"):
            File_Processing.gif_convert(f'nasa/{og_file}')
            filename = filename.replace('.gif', '.png')
        else:
            filename = filename.replace('.jpg', '.png')

        try:
            with open(f'nasa/{og_file}', 'wb') as handler:
                handler.write(response.content)
                handler.close()
        except Exception as e:
            print(e)
        return 'nasa', filename

    @staticmethod
    def call_wallhaven_api(resolution, sorting='random', query='space', purity='sfw'):
        try:
            wallhaven_api_key = user_settings.User_Settings.retrieve_user_settings()['API_KEYS']['wallhaven']

            url = f'https://wallhaven.cc/api/v1/search?apikey={wallhaven_api_key}&q={query}&resolutions={resolution}&sorting={sorting}&purity={purity}'
            os.makedirs('C:/Users/Corentin/Pictures/Wallpapers/wallhaven/original_file/', exist_ok=True)
            api_call = requests.get(url)
            data = api_call.json()
            print(data)
            print("request",url)
            total_results = data['meta']['total']
            print(f'Total results: {total_results}')
            if total_results == 0:
                raise IndexError("No results found. Try changing your query")

            url = data['data'][0]['path']

            filename = url.replace('https://w.wallhaven.cc/full/', '')
            filename = filename.replace('/', '-')
            response = requests.get(data['data'][0]['path'])

            with open(f'C:/Users/Corentin/Pictures/Wallpapers/wallhaven/original_file/{filename}', 'wb') as handler:
                handler.write(response.content)

            print(f'File downloaded: {filename}')
            return ['wallhaven', filename]
        except Exception as e:
            issue_handler.no_value_returned_api(e)
