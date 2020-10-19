# gaming_setupv2
Turn on game and spotify

## Setup: Spotify App
Before running the program, you need to create an app using [spotify's api](https://developer.spotify.com/dashboard/applications) dashboard. Login using your spotify premium account and follow the instructions to create the app. Once the app is created, you need to grab three things:
* Client ID
* Client Secret
* Redirect URI

The redirect uri can we any website you choose, such as google.com or spotify.com. This is set by going to Edit Setting and putting in the destination under Redirect URIs. You will take these three and create environment variables. When you run either setup.py (only if you ask to it to find your device id) or main.py, you will be prompted on your browser to allow your app to access your spotify. After hitting allow, you will also see a terminal message asking you what uri you were directed to. Copy the url from the search bar into the termal at the prompt.

## Setup: Environment Variables
On your windows computer follow this [guide](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/) to set up environment variables. In short:
1. Start typing environment into your start search bar (lower left) till you see "Edit the system environment variables"
2. On the bottom of the new window, click on "Environment Variables..."
3. Under user variables, or the top half, click New. You want to do this three times to input the information you copied previously (variable name : variable value)
  - SPOTIPY_CLIENT_ID : Your client ID from your app
  - SPOTIPY_CLIENT_SECRET : Your client secret from your app
  - SPOTIPY_REDIRECT_URI : The redirect URI you set for your app
 
 Be sure to hit ok after each variable, and finally hit ok on the window containing all the environment variables. Now we can move on to installation.
 
 ## PIP install
 In this project is a requirements.txt in this project. It contains the needed pip installs for the the program to run. Pip should be installed if you have python. In your terminal put:
 
```bash
pip install -r path\to\requirements.txt
```

## Setup.py
When everything else is setup, this program will allow you to put the needed information for the program to run. Throught the terminal it will prompt you for the following information:
- .exe name of your game
- File path of the game
- File path for spotify
- Playlist uri
- Device ID

Your playlist uri can be found on spotify by right clicking on the playlist, share, then copy Spotify URI. If you do not know the the device id, enter "n" when prompted and have your desired device open before hitting enter "n". Copy the id for your device and continue to follow the prompts on the terminal. A file named "program_info_file"  will be created in order that holds all this information for the future. Whenever you want to change any settings, run setup.py again.

## Main.py
Once everything above is completed, simply running main.py will open your game, spotify, and start your playlist. By grabbing  the needed values from "program_info_file", it checks if the game and spotify is running. If not then then, it will open them. In the background, the program will keep trying to find the device you activated. Once it does, it will start the playlist and the program will end.
