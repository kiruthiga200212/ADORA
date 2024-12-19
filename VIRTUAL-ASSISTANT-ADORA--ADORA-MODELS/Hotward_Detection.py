import os
import speech_recognition as sr

def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You Said:{query}")
        except:
            return "none"
        return query.lower()

while True:
    wake_up = take_command().lower()

    print("Recognized Command:", wake_up)

    if 'wake up' in wake_up:
        script_path = ('c:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/Adora.py')
        os.startfile(script_path)
    else:
        print("Nothing...")
