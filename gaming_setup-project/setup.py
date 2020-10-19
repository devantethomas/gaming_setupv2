import pickle
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

#add playlist uri

def print_devices():
    scope = ('user-read-playback-state')
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    devices = sp.devices().get('devices')
    for device in devices:
        name = device.get('name')
        dev_id = device.get('id') 
        print(f'{name} : {dev_id}')


welcome_msg = 'Hello, if you need help with finding the required information, please refer to the read me for more detailed instructions!'



music_location = input('\nEnter file path for spotify: ')

game_name = input('Enter the .exe name of game: ')
game_location = input('Enter the file path for the desired game: ')

playlist_uri = input('Enter the playlist uri copied from spotify: ')


while True:
    try:
        print('\nIf you do not know your device id, have application or website open.')
        know_id = input('\nDo you know your device id?(Y/N): ').lower()
        if know_id == 'y':
            device_id = input('Enter device id: ')
            break
        elif know_id == 'n':
            print('Current devices, copy the left value of the device you want')
            print_devices()
            continue
        else:
            raise ValueError
    except ValueError:
        print('\nInput y if you know the device id, or n if you do not know. Try again!')
        continue

program_info = [music_location, game_name, game_location, playlist_uri, device_id]
with open('program_info_file', 'wb') as f:
    pickle.dump(program_info, f)






