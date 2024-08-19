import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print("hello")
    s=input()
    speaker.Speak(s)