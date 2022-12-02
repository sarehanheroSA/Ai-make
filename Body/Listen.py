import speech_recognition as sr
 
def Listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,0,8)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio,language='en-in')
            print(f"You said : {data}")
   
        except:
            return ""
        data = str(data)
        return data.lower()
