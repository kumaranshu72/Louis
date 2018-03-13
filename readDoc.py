import docx
import os

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

    def find_all(self,path):
        result = []
        for root, dirs, files in os.walk(path):
            if self.filename in files:
                result.append(os.path.join(root, self.filename))
        return result

#print(len(readFile("readme.docx").find_all("./documents")))
