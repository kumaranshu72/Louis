import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
engine.say('Good morning Anshu')
engine.runAndWait()
