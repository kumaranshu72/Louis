import docx

class readFile:

    def __init__(self,filename):
        self.filename=filename
        pass

    def read(self):
        doc = docx.Document(self.filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
