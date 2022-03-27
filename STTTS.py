#setup
import os
from gtts import gTTS
from playsound import playsound
import sys
import speech_recognition as sr 
path_to_tts = os.path.join(sys.path[0], 'tts.mp3')

#voice recognission
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source: #sets input device to your mic
        audio = r.listen(source) #listens 
        said = ''
        try:
            said = r.recognize_google(audio) #uses Google to recognise your voice
            print(said)
        except Exception as e:
            print('null')
    return said

#tts
def say(text):
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save(path_to_tts)
    playsound(path_to_tts)
    os.remove(path_to_tts)

#loop
while True:
    checker = get_audio()
    if checker != '':
        say(checker)