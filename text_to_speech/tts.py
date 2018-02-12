import pyttsx

class speechToText:
    
    def __init__(self,text):
        self.text=text

    def say(self):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-40)
        engine.say(self.text)
        engine.runAndWait()
        pass

obj=speechToText("Good Morning! This is a demo text");
obj.say()
