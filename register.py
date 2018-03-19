from VoiceIt import *
import getpass
import sys
import stt
import tts
import time
import os
import json

myVoiceIt = VoiceIt("e0bb5797dcd944e49e6145ec58ffaf59")
userName = "anshu"
pswd = "anshu500"

print("WELCOME TO LOUIS")
userName=raw_input("Enter Your userName : ")
response = myVoiceIt.getUser(userName, "d0CHipUXOk")
var = True
ind1=response.find("ResponseCode")
ind1+=15
ind2=response.find('"',ind1)
if response[ind1:ind2]=='UNF':
    var=False
while var:
    print("UserName Already Exists.Try Something else")
    userName=raw_input("Enter Your userName : ")
    response = myVoiceIt.getUser(userName, "d0CHipUXOk")
    var = True
    ind1=response.find("ResponseCode")
    ind1+=15
    ind2=response.find('"',ind1)
    if response[ind1:ind2]=='UNF':
        var=False


while True:
    pswd = getpass.getpass('Enter Password:')
    pswd_cnf = getpass.getpass('Confirm Password:')
    if(pswd==pswd_cnf):
        break
    else:
        print("Password Missmatch Try Again")

response = myVoiceIt.createUser(userName, pswd)
ind1=response.find("ResponseCode")
ind1+=15
ind2=response.find('"',ind1)
if response[ind1:ind2]=='SUC':
    print("User Created Successfully")
else:
    print("Something Went wrong! Please try after sometime")
    sys.exit()

i=0
while True:
    if i==3:
        break
    tts.textToSpeech("Please Speak Zoos are filled with small and large animals after the beep").say()
    time.sleep(0.5)
    os.system("echo '\a'")
    time.sleep(0.2)
    stt.SpeechToText('./sound/file.wav').record(5)
    os.system("echo '\a'")
    response = myVoiceIt.createEnrollment(userName, pswd, "./sound/file.wav", "en-US")
    print(response)
    ind1=response.find("ResponseCode")
    ind1+=15
    ind2=response.find('"',ind1)
    if response[ind1:ind2]=='SUC':
        i+=1

data={}
data['userName']=userName
data['password']=pswd
data['isRegistered']=True
with open('./data/sim.json', 'w') as outfile:
    json.dump(data, outfile)
os.system("sudo cp ~/Desktop/blinux/Myscript.desktop ~/.config/autostart/")
print("Registration Successfully! System will restart in 10 seconds")
time.sleep(10)
os.system("reboot")
