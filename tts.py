import pyttsx

class textToSpeech:

    def __init__(self,text):
        self.text=text

    def say(self):
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-40)
        engine.say(self.text)
        engine.runAndWait()
        pass
