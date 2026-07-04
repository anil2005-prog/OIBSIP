import webbrowser
from tts_engine import speak

def play_music():
    speak("Playing music")
    webbrowser.open("https://music.youtube.com")