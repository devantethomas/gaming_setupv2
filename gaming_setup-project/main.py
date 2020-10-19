import psutil
import subprocess
import os
import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth

music_name = 'spotify'
music_location, game_name, game_location, playlist_uri, dev_id, = [''] * 5

#load variables from file created in steup
try:
    with open('program_info_file', 'rb') as f:
        music_location, game_name, game_location, playlist_uri, dev_id = pickle.load(f)
except FileNotFoundError:
    print('Please run setup.py to create the file')

# #spotipy code
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')

#see which programs are running
def running_programs(program_name):
    process_list = []
    for p in psutil.process_iter():
        process_list.append(p.name().lower())
    if program_name.lower() in process_list:
        return True
    else:
        return False

#open specified program
def open_program(file_path):
    subprocess.Popen(file_path)

#checks if a program is running, and if not will call function to open
def check_if_open(program_name, file_path):
    if running_programs(program_name):
        pass
    else:
        open_program(file_path)
        return True

#Once device is detected will start the specific playlist
def start_playlist(playlist_uri, dev_id):
    scope = 'user-read-playback-state streaming user-modify-playback-state'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    while True:
        devices = sp.devices().get('devices')
        if devices: #if a device is found
            try:
                for device in devices: #if multiple devices found, checks id of each and starts playlist on matching id
                    if dev_id == device.get('id'): 
                        sp.start_playback(device_id=dev_id, context_uri=playlist_uri)
                        playing = True #if playlists starts break out of outer loop, else loop again till id is found
                    else:
                        playing = False
                if playing:
                    break
            except spotipy.exceptions.SpotifyException:
                continue


check_if_open(game_name, game_location)
check_if_open(music_name, music_location)
start_playlist(playlist_uri, dev_id)








        
        


