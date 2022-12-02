import pyttsx3

def Speak(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty('rate',168)
    engine.say(x)
    engine.runAndWait()