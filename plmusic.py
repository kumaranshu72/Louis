import os
import pygame
from sys import exit
import tts
import stt
import time

class mus:
    def pld():
        files = []
        sep="."
        for filename in os.listdir('./Desktop/major/pymusic'):
                filename=filename.split(sep,1)[0]
                files.append(filename)
        #print(files[0])
        #print(files[1])
        tts.textToSpeech("Speak the name of the song you want to play").say()
        time.sleep(0.2)
        os.system("echo '\a'")
        time.sleep(0.2)
        stt.SpeechToText('./Desktop/major/sound/song.wav').record(5)
        os.system("echo '\a'")
        song=stt.SpeechToText('.Desktop/major/sound/song.wav').speech_to_text()

        print(song)
        file_index = files.index(song) if song in files else None
        if file_index == None:
           tts.textToSpeech("Sorry this song is not available").say()
        else:
           pygame.init()
           pygame.display.set_mode((200,100))
           pygame.mixer.music.load('./Desktop/major/pymusic/'+files[file_index]+'.mp3')
           pygame.mixer.music.play(0)
           while True:                                                                 #to close using x button
              for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
