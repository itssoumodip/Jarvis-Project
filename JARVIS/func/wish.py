import pyttsx3
import speech_recognition as sr
import time  # Import the time module
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
# print(voicese[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    now = datetime.datetime.now()
    hour = now.strftime("%I")  # 12-hour format
    minute = now.strftime("%M")
    am_pm = now.strftime("%p")  # AM/PM
    current_time = f"{hour}:{minute} {am_pm}"
    today_date = now.strftime("%A, %B %d, %Y")
    
    # Introduce a short delay before speaking
    time.sleep(0.5)
    
    if int(now.strftime("%H")) >= 0 and int(now.strftime("%H")) < 12:
        text = f"Good Morning!"
        print(f"JARVIS: {text}")
        speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        speak(text)
    elif int(now.strftime("%H")) >= 12 and int(now.strftime("%H")) < 18:
        text = f"Good Afternoon!"
        print(f"JARVIS: {text}")
        speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        speak(text)
    else:
        text = f"Good Evening!"
        print(f"JARVIS: {text}")
        speak(text)
        text = f"Today is {today_date}, and the time is {current_time}."
        print(f"JARVIS: {text}")
        speak(text)
        
def intro():
    time.sleep(0.5) 
    intro_text = "Hello Soumodip,"
    print(f"JARVIS: {intro_text}")
    speak(intro_text)
    intro_text = "I am Jarvis, your personal assistant."
    print(f"JARVIS: {intro_text}")
    speak(intro_text)
    intro_text = "How can I assist you today?"
    print(f"JARVIS: {intro_text}")
    speak(intro_text)


