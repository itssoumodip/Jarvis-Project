import pyttsx3
import speech_recognition as sr
import os
import subprocess
from func.listen import takeCommand
from func.speak import speak
import webbrowser
import datetime

def openThings(query):    
    sites = [
                ["YouTube", "https://www.youtube.com"],
                ["Facebook", "https://www.facebook.com"],
                ["Google", "https://www.google.com"],
                ["Twitter", "https://www.twitter.com"],
                ["LinkedIn", "https://www.linkedin.com"],
                ["Instagram", "https://www.instagram.com"],
                ["Reddit", "https://www.reddit.com"],
                ["Wikipedia", "https://www.wikipedia.org"],
                ["Amazon", "https://www.amazon.com"],
                ["Netflix", "https://www.netflix.com"],
                ["GitHub", "https://www.github.com"],
                ["Stack Overflow", "https://stackoverflow.com"]
            ]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            text = f"Opening {site[0]} Sir..."
            print(f"JARVIS: {text}")
            speak(text)
            webbrowser.open(site[1])
    
    if "music".lower() in query.lower():
        text = "Playing your favorite music Sir"
        print(f"JARVIS: {text}")
        speak(text)
        musicPath = "JARVIS/fav_music.mp3"
        os.system(f"start {musicPath}")   

    if "the time" in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")   
        print(f"JARVIS: {strfTime}")
        speak(f"The time is {strfTime}")
   
    # if "getting over it" in query.lower():
    #     exe_path = r"C:\Users\Soumodip Das\Downloads\Getting Over It with Bennett Foddy\Getting Over It\Getting Over It\GettingOverIt.exe"
    #     subprocess.run([exe_path], shell=True)
    
