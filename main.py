import tts
import stt
import readDoc
import writeD
import json
import os
import sys
import time
from VoiceIt import *

#open USER data
data = json.load(open('/home/anshu/Desktop/major/data/sim.json'))

if data['isRegistered']=="False":
    print("Please Do the registration first")
    sys.exit()

myVoiceIt = VoiceIt("e0bb5797dcd944e49e6145ec58ffaf59")


def reading():
    tts.textToSpeech("Speak the File Name after the beep").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('/home/anshu/Desktop/major/sound/filename.wav').record(3)
    os.system("echo '\a'")
    file_name = stt.SpeechToText('/home/anshu/Desktop/major/sound/filename.wav').speech_to_text().replace(" ", "")
    file_name = file_name+".docx"
    print(file_name)
    if len(readDoc.readFile(file_name).find_all("/home/anshu/Desktop/major/documents"))<=0:
        print("No such file found")
        tts.textToSpeech("No File Found").say()
    else:
        doc_data = readDoc.readFile("/home/anshu/Desktop/major/documents/"+file_name).read()
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
    stt.SpeechToText('/home/anshu/Desktop/major/sound/docTitle.wav').record(5)
    os.system("echo '\a'")
    doc_title = stt.SpeechToText('/home/anshu/Desktop/major/sound/docTitle.wav').speech_to_text()
    paragraph = []
    #taking the first paragraph
    while True:
        tts.textToSpeech("Speak the Paragraph").say()
        time.sleep(0.5)
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('/home/anshu/Desktop/major/sound/docPara.wav').record(15)
        os.system("echo '\a'")
        file_para = stt.SpeechToText('/home/anshu/Desktop/major/sound/docPara.wav').speech_to_text()
        paragraph.append(file_para)
        tts.textToSpeech("Do you want add more content").say()
        time.sleep(0.2)
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('/home/anshu/Desktop/major/sound/res.wav').record(3)
        os.system("echo '\a'")
        res=stt.SpeechToText('/home/anshu/Desktop/major/sound/res.wav').speech_to_text()
        if res=="no":
            break
    time.sleep(0.2)
    tts.textToSpeech("What would you like to name the file").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('/home/anshu/Desktop/major/sound/docName.wav').record(4)
    os.system("echo '\a'")
    file_Name = stt.SpeechToText('/home/anshu/Desktop/major/sound/docName.wav').speech_to_text().replace(" ", "")
    file_Name=file_Name+".docx"
    wr.addHeading(doc_title)
    for p in paragraph:
        print(p)
        wr.addParagraph(p)
    wr.saveDoc("/home/anshu/Desktop/major/documents/"+file_Name)
    tts.textToSpeech("Document saved sucessfully").say()

def browse():
    return "Something 1"

def calc():
    return "calc"

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
#authentication
while(True):
    spch="Hello "+data['userName']+" ! Please Speak:  Zoos are filled with small and large animals after the beep :"
    tts.textToSpeech(spch).say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('/home/anshu/Desktop/major/sound/file.wav').record(5)
    os.system("echo '\a'")
    response = myVoiceIt.authentication(data['userName'], data['password'], "/home/anshu/Desktop/major/sound/file.wav", "en-US")
    ind1=response.find("ResponseCode")
    ind1+=15
    ind2=response.find('"',ind1)
    print(response[ind1:ind2])
    if response[ind1:ind2]=="SUC":
        tts.textToSpeech("Welcome "+data['userName']+"  How may i Help You!").say()
        #waha dalega test.py wala code
        while True:
            key_press = raw_input()
            if key_press == "":
                print("You pressed enter")
                os.system("echo '\a'")
                time.sleep(0.2)
                stt.SpeechToText('/home/anshu/Desktop/major/sound/command.wav').record(3)
                cmd = stt.SpeechToText('/home/anshu/Desktop/major/sound/command.wav').speech_to_text()
                print(cmd)
                perform_command(cmd)

            else:
                print("Something went Wront Try Again")
                tts.textToSpeech("Something went Wrong. Try Again").say()
    else:
        ind1=response.find("Result")
        ind1+=9
        ind2=response.find('"',ind1)
        msg=response[ind1:ind2]
        print(msg)
        tts.textToSpeech(msg).say()
        time.sleep(0.4)
