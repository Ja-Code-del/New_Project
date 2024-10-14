#EXTRACT THE TEXT FROM PDF FILE
#libraries
import PyPDF2
from docx import Document
from gtts import gTTS
import os
import shutil


#Use this function to create another button to convert texts to doc file too
def conv_to_docx(text):
    document = Document()
    document.add_paragraph(text)
    document.save("new.docx")


def extract_text_of(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        conv_to_docx(text)
    return text


#CONVERT THE EXTRACTED TEXT INTO AUDIO FILE USING gTTS
#first divide it into chunk
def split_text(text, max_length=5000):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


#READ OR SAVE THE AUDIO FILE
def text_to_speech(text, language='fr'):
    chunks = split_text(text)
    destination_folder = 'Outputs'
    for i, chunk in enumerate(chunks):
        tts = gTTS(text=chunk, lang=language, slow=False)
        filename = f"output_part_{i + 1}.mp3"
        tts.save(filename)
        shutil.move(filename, os.path.join(destination_folder, filename))
        print(f"Your file has been save into {destination_folder} folder")
        os.system(f"afplay {filename}")
