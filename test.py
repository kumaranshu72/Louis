import tts
import stt
import readDoc
import writeD
import json
import os
import time
from VoiceIt import *

def reading():
    tts.textToSpeech("Speak the File Name after the beep").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('./sound/filename.wav').record(3)
    os.system("echo '\a'")
    file_name = stt.SpeechToText('./sound/filename.wav').speech_to_text().replace(" ", "")
    file_name = file_name+".docx"
    if len(readDoc.readFile(file_name).find_all("./documents"))<=0:
        print("No such file found")
        tts.textToSpeech("No File Found").say()
    else:
        doc_data = readDoc.readFile("./documents/"+file_name).read()
        print(doc_data)
        tts.textToSpeech(doc_data).say()

def writing():
    return "one"

def browse():
    return "Something 1"

def calc():
    return "calc"

def plmusic():
    return "playing music"

switcher = {
        "read document":reading,
        "write document":writing,
        "browse internet":browse,
        "calculate":calc,
        "play music":plmusic
    }

def perform_command(argument):
    func = switcher.get(argument, "Invalid Command")
    if(func != "Invalid Command"):
        return func()
    else:
        tts.textToSpeech("Invalid Command").say()
#print(perform_command("read document"))

while True:
    key_press = raw_input()
    if key_press == "":
        print("You pressed enter")
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('./sound/command.wav').record(3)
        cmd = stt.SpeechToText('./sound/command.wav').speech_to_text()
        perform_command(cmd)

    else:
        print("Something went Wront Try Again")
        tts.textToSpeech("Something went Wrong. Try Again").say()
    pass
