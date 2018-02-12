import pyaudio
import wave
import speech_recognition as sr

class SpeechToText:

    def __init__(self,filename):
        self.filename=filename

    def speech_to_text(self):
        r = sr.Recognizer()
        with sr.WavFile(self.filename) as source:
            audio = r.record(source)

        try:
            return r.recognize_google(audio)
        except LookupError:
            return "Could not understand audio"

    def record(self):
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = self.filename

        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        print "recording..."
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print "Please Wait"


        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

obj=SpeechToText('file.wav')
obj.record()
print(obj.speech_to_text())
