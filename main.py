import tts
import stt
import readDoc
import writeD
import json
import os
import time
from VoiceIt import *

#open USER data
data = json.load(open('./data/sim.json'))
myVoiceIt = VoiceIt("2140c866df40472f84530b6fbd4c5a95")

#authentication
while(True):
    spch="Hello "+data[0]['userName']+" ! Please Speak:  Zoos are filled with small and large animals after the beep :"
    tts.textToSpeech(spch).say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('./sound/file.wav').record(5)
    os.system("echo '\a'")
    response = myVoiceIt.authentication("anshu", "anshu500", "./sound/file.wav", "en-US")
    ind1=response.find("ResponseCode")
    ind1+=15
    ind2=response.find('"',ind1)
    print(response[ind1:ind2])
    if response[ind1:ind2]=="SUC":
        tts.textToSpeech("Welcome "+data[0]['userName']+"  How may i Help You!").say()
        #waha dalega test.py wala code
        break
    else:
        ind1=response.find("Result")
        ind1+=9
        ind2=response.find('"',ind1)
        msg=response[ind1:ind2]
        print(msg)
        tts.textToSpeech(msg).say()
        time.sleep(0.4)
