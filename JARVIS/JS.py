import pyttsx3
import speech_recognition as sr
from func.wish import wishMe
from func.wish import intro
from data.list import openThings
from func.listen import takeCommand
from func.speak import speak
from llm.gemini import auto

def main():
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            # wishMe()
            # intro()
            while True:
                query = takeCommand().lower()
                openThings(query)
                if "go to sleep" in query:
                    text = "Okay Sir, You can call me anytime"
                    print(f"JARVIS: {text}")
                    speak(text)
                    return  # Exit the function, breaking both loops
                elif "hello" in query:
                    text = "Hello sir, How are you?"
                    speak(text)
                else:
                    auto(query)

if __name__ == "__main__":
    main()
