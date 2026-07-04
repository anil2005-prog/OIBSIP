from datetime import datetime
from tts_engine import speak

def tell_date():
    today = datetime.now().strftime("%d %B %Y")
    print(today)
    speak(f"Today is {today}")