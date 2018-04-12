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
    stt.SpeechToText('~/Desktop/major/sound/filename.wav').record(3)
    os.system("echo '\a'")
    file_name = stt.SpeechToText('~/Desktop/major/sound/filename.wav').speech_to_text().replace(" ", "")
    file_name = file_name+".docx"
    print(file_name)
    if len(readDoc.readFile(file_name).find_all("~/Desktop/major/documents"))<=0:
        print("No such file found")
        tts.textToSpeech("No File Found").say()
    else:
        doc_data = readDoc.readFile("~/Desktop/major/documents/"+file_name).read()
        print(doc_data)
        tts.textToSpeech(doc_data).say()

def writing():
    #writeDoc object
    wr = writeD.writeDoc()
    #taking the title
    tts.textToSpeech("Speak the title of the document").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('~/Desktop/major/sound/docTitle.wav').record(5)
    os.system("echo '\a'")
    doc_title = stt.SpeechToText('~/Desktop/major/sound/docTitle.wav').speech_to_text()
    paragraph = []
    #taking the first paragraph
    while True:
        tts.textToSpeech("Speak the Paragraph").say()
        time.sleep(0.5)
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('~/Desktop/major/sound/docPara.wav').record(15)
        os.system("echo '\a'")
        file_para = stt.SpeechToText('~/Desktop/major/sound/docPara.wav').speech_to_text()
        paragraph.append(file_para)
        tts.textToSpeech("Do you want add more content").say()
        time.sleep(0.2)
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('~/Desktop/major/sound/res.wav').record(3)
        os.system("echo '\a'")
        res=stt.SpeechToText('~/Desktop/major/sound/res.wav').speech_to_text()
        if res=="no":
            break
    time.sleep(0.2)
    tts.textToSpeech("What would you like to name the file").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('~/Desktop/major/sound/docName.wav').record(4)
    os.system("echo '\a'")
    file_Name = stt.SpeechToText('~/Desktop/major/sound/docName.wav').speech_to_text().replace(" ", "")
    file_Name=file_Name+".docx"
    wr.addHeading(doc_title)
    for p in paragraph:
        print(p)
        wr.addParagraph(p)
    wr.saveDoc("~/Desktop/major/documents/"+file_Name)
    tts.textToSpeech("Document saved sucessfully").say()

def browse():
    return "Something 1"

from calci import calculator
def calc():
    c=calculator()
    c.evaluate()
	#calci.calculator.evaluate();



def plmusic():
    return "playing music"

switcher = {
        "read file":reading,
        "write file":writing,
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
        print(cmd)
        perform_command(cmd)

    else:
        print("Something went Wront Try Again")
        tts.textToSpeech("Something went Wrong. Try Again").say()
