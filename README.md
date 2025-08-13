# Wallpaper changer

This little script makes use of API calls to change your wallpaper, this is a small project aimed to people who want to change wallpapers within a given theme.


# How does it work?

You'll have to get yourself an API key from the currently [supported sources](#Supported-APIs), and enter it when prompted to by the script by launching `main.py` 

Don't forget to click save as I didn't implement a failsafe for closing the window yet.

To launch `main.py`, simply right click in the folder, open terminal, and type `python main.py`

(Note: The images will be savec in your Default Picture Folder, yes, even if you modified the path, as long as windows recognize it as such, so remember to empty it from time to time if you don't want to keep the old files)


# Please read this

This project uses APIs to work, I insist, **DO NOT SHARE YOUR API KEYS**, the sources I currently use are limited on number of request, and you will not be charged even if you change multiple times your wallpaper, but they can be rate limited if used too much (Such as your API key being shared with too many people), in the future, I *might* use API have paid plan when you reach a certain number of request per period (Normally unreachable by a single individual), if your API key is shared publicly, you might go over the limit and get charged, so please, **DO NOT SHARE YOUR API KEYS** (If you did, or are scared to, check the next section)

(Note: if in the future I use free sources with paid plans available, I will either put a check with the api to make sure you don't get charged, or put a warning when selecting a source that can potentially charge you)


## You think you made a mistake?

- If you think you made a mistake during the setup such as entering NASA's API Key while you had Wallhaven selected, or entered a wrong query, don't worry.

- If you made a mistake on the API Key, you can either just re-enter it if you didn't click save yet (As this will close the setup), or you can simply delete the file `config.ini` that has been created in the folder

- If you entered a wrong query, whenever you will run `main.py`, it will ask for a query to change your wallpaper to, so don't worry too much about it

- If the script threw an error:
Wallhaven: You probably made a query that didn't return any results, I didn't implement a warning message yet, try with a simple query like "Space", if it still throws an error, please contact me with the Error message
Nasa: Chances are, they are currently using a GIF, it happens sometimes, I didn't implement anything for them yet, it will come soon

- **I SHARED MY API KEY**: Don't panic, just go wherever your found your API key, you should find a button such as "Regenerate", "Refresh", or any synonym, and press yes if there are any prompts asking if you are sure, this will invalidate the previous key, and provide you with a new one 

## What will change in the future
The changes that I plan to make are as follow:

- If API allows, restrictions on tag (To avoid unwanted content, such as Cyberpunk 2077 when you want to have Cyberpunk Aesthetic) ***(High Priority)***
- Add a way to delete older wallpapers files (User Selection, on new, on amount, on time) ***(High Priority)***
- Workaround NASA using GIF sometimes *
- Add a setting button on subsequent `main.py` runs to edit API key(s), source or any other settings
- Add other sources *(If you have requests for sources, contact me)*
- Make the script run on a timer in the background (User selection, can be a one time run or a background run) maybe as a service, maybe as a script *(Maybe user selection as well?)*
- Make the wallpaper change start as soon as the setup is saved *(Low priority)*

*Will be added on the next update


## My 2 cents on how you'll use it
I suggest this to be used with Wallhaven API for a few reasons, first is, Wallhaven can enforce Resolution search, which I use in my project, it allows me to filter out images that do not have the same resolution as your screen, and would therefore stretch when resized to fit your screen. Second thing, you can find wallpapers based on a query, so you can change fairly easily what you want on your background (Space, Castle, Games...)


## Known issues
- Lack of failsafe in case setup window is closed (Temp fix: Delete config.ini and restart `main.py`
- NASA image being stretched depending on the picture, [read this](#-My-2-cents-on-how-you'll-use-it) (Will try to find a workaround at some point)

### Supported APIs
[NASA APOD](https://apod.nasa.gov/apod/astropix.html): To create an API key, simply head to https://api.nasa.gov, you will then receive an **API key in your emails**

[Wallhaven](https://wallhaven.cc): To create an API key, **create an account**, head to **Settings**, and you will find it in the **category "Account"** under "API Key"


#### Disclaimer
I am not a profesionnal *(Yet hopefully)*, I did this for my own use, and thought "Lets make it available for other people who could like it", so if you have any feedback on anything about this project, the features, the code, literally anything, please contact me so I can improve
