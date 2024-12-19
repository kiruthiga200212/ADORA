import os
import pyttsx3
import speech_recognition as sr
import pygame

def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"Your command: {query}")
            return query.lower()

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return "none"
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")
            return "none"

def Task_Execution():
    Music()

def Music():
    Speak("Tell me the name of the song")
    music_name = take_command()
    print("Received music name:", music_name)

    # Check for specific songs or keywords in the command
    if 'perfect' in music_name:
        play_music("C:/Users/keert/Downloads/Perfect.mp3")
    elif 'blank space' in music_name:
        play_music('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/songs/Taylor_Swift_-_Blank_space_Taylors_version_-Hippopcharts.com.mp3')
    elif 'vathi raid' in music_name:
        play_music('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/songs/Vaathi-Raid-MassTamilan.io.mp3')
    elif 'shape of you' in music_name:
        play_music('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/songs/Shape-Of-You-Ed-Shereen-Piano-Version-Ringtone-dmr.mp3')
    else:
        Speak("Song not found locally. Playing on YouTube.")
        # You can add the code here to play on YouTube using pywhatkit

    Speak("Your song has been started. Enjoy, ma'am")

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path.replace('\\', '/'))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Call the Task_Execution function to start the process
Task_Execution()
