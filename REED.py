from this import d
from httplib2 import MalformedHeader
import pyttsx3
import os
from PyPDF2 import PdfReader
#import cv2
import numpy as np
#import pytesseract

#let the program know wher tesseract is
#pytesseract.pytesseract.tesseract_cmd = r""


#Initialize the pyttsx3 with a variable called engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
#img = cv2.imread("")

#cv2.imshow("Img", img)
#cv2.waitKey(0)

reader = PdfReader("importpdfs\Calculus_Made_Easy_Thompson.pdf")
pages = reader.numPages
i = 40
pagegetter = reader.getPage(i)
text = pagegetter.extractText()
for voice in voices:
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.say('The quick brown fox jumped over the lazy dog.')


while i != pages:
    i += 1
    engine.say(text)
    pagegetter
    print(pagegetter)
    print(text)
    engine.runAndWait()
    engine.stop()
    break

    
