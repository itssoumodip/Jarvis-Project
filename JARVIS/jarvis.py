import pyttsx3
import datetime
import speech_recognition as sr
import win32com.client
import time  # Import the time module
import webbrowser
import openai
import os
import subprocess

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = datetime.datetime.now().minute
    current_time = f"{hour}:{minute:02d}"
    today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    
    # Introduce a short delay before speaking
    # time.sleep(0.5)
    
    if hour >= 0 and hour < 12:
        time.sleep(0.5) 
        text = f"Good Morning!"
        print(f"JARVIS: {text}")
        speaker.Speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        speaker.Speak(text)
    elif hour >= 12 and hour < 18:
        time.sleep(0.5) 
        text = f"Good Afternoon!"
        print(f"JARVIS: {text}")
        speaker.Speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        speaker.Speak(text)
    else:
        time.sleep(0.5) 
        text = f"Good Evening!"
        print(f"JARVIS: {text}")
        speaker.Speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        # time.sleep(0.5) 
        speaker.Speak(text)

def intro():
    time.sleep(0.5) 
    intro_text = "Hello Soumodip,"
    print(f"JARVIS: {intro_text}")
    speaker.Speak(intro_text)
    intro_text = "I am Jarvis, your personal assistant."
    print(f"JARVIS: {intro_text}")
    speaker.Speak(intro_text)
    intro_text = "How can I assist you today?"
    print(f"JARVIS: {intro_text}")
    speaker.Speak(intro_text)

def takeCommand():
    # it takes Microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try: 
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"USER: {query}")
        except Exception as e:
            # print(e)
            text = "Sorry, I didn't get that. Please say that again."
            print(f"JARVIS: {text}")
            speaker.Speak(text)
            return "None"
    return query

if __name__ == "__main__":
    wishMe()
    intro()
    while True:
        print("Listening.......")
        query = takeCommand()
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
                speaker.Speak(text)
                webbrowser.open(site[1])

        if "music".lower() in query.lower():
            text = "Playing your favorite music Sir"
            print(f"JARVIS: {text}")
            speaker.Speak(text)
            musicPath = "JARVIS/fav_music.mp3"
            os.system(f"start {musicPath}")   

        if "the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")   
            print(f"JARVIS: {strfTime}")
            speaker.Speak(f"The time is {strfTime}")

        if "getting over it" in query.lower():
            exe_path = r"C:\Users\Soumodip Das\Downloads\Getting Over It with Bennett Foddy\Getting Over It\Getting Over It\GettingOverIt.exe"
            subprocess.run([exe_path], shell=True)
