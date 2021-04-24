# Voice recognition (speech-to-text)

import speech_recognition as engine

recognizer = engine.Recognizer()

def recognition_init(istherenoise=False):
    #some logic that will change recognition func with arguments it will get
    pass

def recognition ():
    with engine.Microphone() as mic:
        audio = recognizer.listen(mic)

        try:
            transcript = recognizer.recognize_google(audio)
        except Exception:
            return "Error: Imposible to recognize."
    return transcript