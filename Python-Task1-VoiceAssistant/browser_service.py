import webbrowser
import urllib.parse
from tts_engine import speak

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")
    
def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
    
def google_search(query):
    query = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={query}")