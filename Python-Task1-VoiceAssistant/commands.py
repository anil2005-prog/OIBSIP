from tts_engine import speak

from time_service import tell_time
from date_service import tell_date
from browser_service import (
    open_google,
    open_youtube,
    google_search
)
from weather import weather
from calculator import calculate
from music import play_music
from email_service import send_email
from reminder import set_reminder


def process_command(command):

    print("process_command() called with:", command)

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        tell_time()

    # Date
    elif "date" in command:
        tell_date()

    # Open Google
    elif "open google" in command:
        open_google()

    # Open YouTube
    elif "open youtube" in command:
        open_youtube()

    # Google Search
    elif command.startswith("search"):
        query = command.replace("search", "").strip()

        if query:
            google_search(query)
        else:
            speak("What do you want me to search?")

    # Weather
    elif "weather" in command:
        weather()

    # Calculator
    elif "calculate" in command:
        calculate()

    # Play Music
    elif "play music" in command:
        play_music()

    # Send Email
    elif "send email" in command:
        send_email()

    # Reminder
    elif "reminder" in command:
        set_reminder()

    # Exit
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        exit()

    # Unknown Command
    else:
        speak("Sorry, I don't understand that command.")