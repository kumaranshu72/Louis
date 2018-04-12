import webbrowser
import time
import os
import subprocess
import tts
import stt
from pynput.keyboard import Key, Controller

class sm:
    def sear():
        keyboard = Controller()

        p=p = subprocess.Popen(["google-chrome", "http://www.google.com"])
        time.sleep(3)

        while True:
           tts.textToSpeech("Speak your search query after the beep").say()
           time.sleep(0.5)
           os.system("echo '\a'")
           time.sleep(0.2)
           with keyboard.pressed(Key.ctrl):
              with keyboard.pressed(Key.shift):
        	     keyboard.press('.')
        	     keyboard.release('.')
           #keyboard.press_and_release('ctrl+shift+.')
           time.sleep(15)
           tts.textToSpeech("Do you want to search another query").say()
           time.sleep(0.2)
           os.system("echo '\a'")
           time.sleep(0.2)
           stt.SpeechToText('./Desktop/major/sound/ask.wav').record(3)
           os.system("echo '\a'")
           ask=stt.SpeechToText('./Desktop/major/sound/ask.wav').speech_to_text()
           if ask=="no":
              break

        p.kill()
        #os.system('taskkill /f /im chrome.exe')
        #os.system("pkill "+browserExe) in browser
