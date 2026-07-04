from tts_engine import speak

def process_command(command):
    print("process_command() called with:", command)

    if "hello" in command:
        print("Greeting detected")

        speak("Hello! How can I help you?")

        print("Finished speaking")   # <-- Add this line

    else:
        speak("Sorry, I don't understand.")