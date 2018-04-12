from tts import textToSpeech
from stt import SpeechToText
import os


class calculator:
    def evaluate(self):
        os.system("echo '\a'")
        time.sleep(0.2)
        obj=SpeechToText('./Desktop/major/sound/file.wav')
        obj.record(5)
        time.sleep(0.2)
        os.system("echo '\a'")
        var=obj.speech_to_text();

        equation=var.replace("x","*");

        ans=eval(equation);
        #print(ans);

        spe=textToSpeech("the calculated value is equal to "+str(ans))
        spe.say();
