# musiclib.py

import pywhatkit as kit

def play(song_name):
    try:
        print(f"🎵 Playing: {song_name} on YouTube...")
        kit.playonyt(song_name)
    except Exception as e:
        print("❌ Could not play the song. Error:", e)
