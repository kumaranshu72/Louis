import docx
import pyttsx

def readFile(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def readText(filename):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-40)
    engine.say(readFile(filename))
    engine.runAndWait()


readText('readme.docx')
