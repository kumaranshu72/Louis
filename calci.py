from tts import textToSpeech
from stt import SpeechToText


class calculator:
    def evaluate(self):
        obj=SpeechToText('./sound/file.wav')
        obj.record()
        var=obj.speech_to_text();

        equation=var.replace("x","*");

        ans=eval(equation);
        #print(ans);

        spe=textToSpeech("the calculated value is equal to "+ans)
        spe.say();


