#TODO 1 : EXTRACT THE TEXT FROM PDF FILE
#libraries
import PyPDF2
from gtts import gTTS
import os


def extract_text_of(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text


syllabus = extract_text_of("syllabus.pdf")
print(syllabus)
#TODO 2 : CONVERT THE EXTRACTED TEXT INTO AUDIO FILE USING gTTS
#TODO 3: READ OR SAVE THE AUDIO FILE
