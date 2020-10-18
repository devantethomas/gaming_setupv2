# gaming_setupv2
Turn on game and spotify

## Setup: Spotify App
Before running the program, you need to create an app using [spotify's api](https://developer.spotify.com/dashboard/applications) dashboard. Login using your spotify premium account and follow the instructions to create the app. Once the app is created, you need to grab three things:
* Client ID
* Client Secret
* Redirect URI

The redirect uri can we any website you choose, such as google.com or spotify.com. This is set by going to Edit Setting and putting in the destination under Redirect URIs. You will take these three and create environment variables

## Setup: Environment Variables
On your windows computer follow this [guide](https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/) to set up environment variables. In short:
1. Start typing environment into your start search bar (lower left) till you see "Edit the system environment variables"
2. On the bottom of the new window, click on "Environment Variables..."
3. Under user variables, or the top half, click New. You want to do this three times to input the information you copied previously (variable name : variable value)
  - SPOTIPY_CLIENT_ID : Your client ID from your app
  - SPOTIPY_CLIENT_SECRET : Your client secret from your app
  - SPOTIPY_REDIRECT_URI : The redirect URI you set for your app
 
 Be sure to hit ok after each variable, and finally hit ok on the window containing all the environment variables. Now we can move on to installation
