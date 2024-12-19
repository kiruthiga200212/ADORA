import speech_recognition as sr
import pygame
import time

class Car:
    def __init__(self, seatbelt_fastened=False):
        self.seatbelt_fastened = seatbelt_fastened
        pygame.mixer.init()

    def fasten_seatbelt(self):
        self.seatbelt_fastened = True
        print("Seatbelt fastened.")

    def unfasten_seatbelt(self):
        self.seatbelt_fastened = False
        print("Seatbelt unfastened.")

    def check_seatbelt_and_alert(self):
        if self.seatbelt_fastened:
            print("Seatbelt is fastened. Drive safely!")
        else:
            print("Seatbelt not fastened! Alerting...")
            self.play_alert_sound()

    def play_alert_sound(self):
        pygame.mixer.music.load("C:/Users/keert/Downloads/mixkit-alarm-clock-beep-988.wav")  # Ensure you have this file in your working directory
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
            pygame.time.Clock().tick(10)

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for 'seatbelt' command...")
        audio = recognizer.listen(source)

    try:
        speech_input = recognizer.recognize_google(audio)
        print(f"You said: {speech_input}")
        return speech_input.lower()
    except sr.RequestError:
        print("API unavailable")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

    return ""

# Initialize speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initialize the car
my_car = Car()

# Example: To simulate seatbelt being fastened or unfastened, toggle these:
# my_car.fasten_seatbelt()
my_car.unfasten_seatbelt()

# Voice command loop
while True:
    command = recognize_speech_from_mic(recognizer, microphone)
    if "seat belt" in command:
        my_car.check_seatbelt_and_alert()
        break  # Or, remove this line if you want to continuously listen for commands
