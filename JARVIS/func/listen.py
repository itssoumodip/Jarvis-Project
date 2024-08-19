import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
# print(voicese[0])
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# it takes Microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4) #stop for sometimes
    
    try:
        print("Understanding...")
        query = r.recognize_google(audio,language="en-in")
        print(f"USER : {query}")
    except Exception as e:
        text = "Sorry, I didn't get that. Please say that again."
        print(f"JARVIS: {text}")
        speak(text)
        return "None"
    return query