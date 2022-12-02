from Body.Listen import Listen
from Body.Speak import Speak
from Brain.Brain import ReplyBrain
from Brain.QNA import Questionans




def Main():
    while True:
        Data = Listen()
        Data = str(Data)
        if "what is" in Data or "Where is" in Data or "how many" in Data or "who is" in Data:
            Reply = Questionans(Reply)
        
        elif "my location" in Data:
            from Google_Map.Map import map
            map()
        elif "exit " in Data:
            Speak("ok SIR , I am exit now.")   
        else:
            pass
        Reply = ReplyBrain(Data)
        print(Reply)
        Speak(Reply)
        break
Main()
