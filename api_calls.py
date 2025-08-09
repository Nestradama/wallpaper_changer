import datetime
import os
import requests
import settings


class Api_Calls:
    def __init__(self):
        pass

    @staticmethod
    def call_nasa_api():
        nasa_api_key = settings.User_Settings.retrieve_user_settings()[0]
        url = 'https://api.nasa.gov/planetary/apod?api_key='
        og_file = f'original_file/nasa_potd_{datetime.today().strftime('%Y_%m_%d')}.jpg'
        rzd_file = f'resized_file/nasa_potd_{datetime.today().strftime('%Y_%m_%d')}.jpg'

        os.makedirs('nasa/original_file', exist_ok=True)
        api_call = requests.get(url + nasa_api_key)
        data = api_call.json()

        print(data)

        response = requests.get(data['hdurl'])
        filename = og_file.replace('original_file/', '')

        try:
            with open(f'nasa/{og_file}', 'wb') as handler:
                handler.write(response.content)
                handler.close()
        except Exception as e:
            print(e)
        return 'nasa', filename

    @staticmethod
    def call_wallhaven_api(resolution, sorting='random', query='space'):
        wallhaven_api_key = settings.User_Settings.retrieve_user_settings()[1]
        query= settings.User_Settings.retrieve_user_settings()[2]
        print(wallhaven_api_key)
        url = f'https://wallhaven.cc/api/v1/search?apikey={wallhaven_api_key}&q={query}&resolutions={resolution}&sorting={sorting}&seed=Ehdi58'
        os.makedirs('C:/Users/Corentin/Pictures/Wallpapers/wallhaven/original_file/', exist_ok=True)
        api_call = requests.get(url)
        data = api_call.json()
        print("Data", data)
        url = data['data'][0]['path']
        filename = url.replace('https://w.wallhaven.cc/full/', '')
        filename = filename.replace('/', '-')
        response = requests.get(data['data'][0]['path'])

        with open(f'C:/Users/Corentin/Pictures/Wallpapers/wallhaven/original_file/{filename}', 'wb') as handler:
            handler.write(response.content)

        return ['wallhaven', filename]
