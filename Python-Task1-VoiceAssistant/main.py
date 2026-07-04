from tts_engine import speak
from speech_engine import listen
from commands import process_command

def main():
    speak("Voice Assistant Started")

    while True:
        command = listen()

        if command:
            process_command(command)

if __name__ == "__main__":
    main()