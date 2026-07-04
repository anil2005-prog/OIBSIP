from datetime import datetime
from tts_engine import speak

def tell_time():
    current_time = datetime.now().strftime("%I:%M %p")
    print("Current Time:", current_time)
    speak(f"The current time is {current_time}")