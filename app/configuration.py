import sys
import os.path
from configparser import ConfigParser
config = ConfigParser()
config.read("settings.ini")

assert list(config.keys()) == ['DEFAULT', 'mpd', 'download_dirs', 'debug', 'http', 'threadpool', 'deezer', 'youtubedl'], f"Validating settings.ini failed. Check {__file__}"

if not config['mpd']['music_dir_root'].startswith(config['download_dirs']['base']):
    print("base download dir must be a subdirectory of the mpd music_dir_root")
    sys.exit(1)

if not os.path.exists(config['youtubedl']['command']):
    print(f"youtube-dl not found at {config['youtubedl']['command']}")
    sys.exit(1)
