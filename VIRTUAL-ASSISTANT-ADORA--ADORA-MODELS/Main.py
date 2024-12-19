'''I need a assistant that would help me to do all things with a single command'''
# import keyboard
import smtplib
from my_email import send_email
from numpy import number
import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
import pywhatkit
from bs4 import BeautifulSoup
import os
import wikipedia
from googletrans import Translator
import pyautogui
import requests
import PyPDF2
from gtts import gTTS
import datetime
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import ChatBot 
from whatsapp import whatsapp_Message,Whatsapp_Grp

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def Speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return ("Morning")
    elif hour >= 12 and hour < 16:
        return ("Afternoon")
    elif hour >= 16 and hour < 19:
        return ("evening")
    else:
        return ("night")
    
def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour >= 3 and hour < 18:
        print("have a good day sir")
        Speak("have a good day sir")
    else:
        print("Goodnight sir")
        Speak("Goodnight sir")
        print("Offline")
        exit(0)


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
        except:
            return "none"
        return query.lower()
    
def seatbelt_alert():
    playsound("C:/Users/keert/Downloads/mixkit-alarm-clock-beep-988.wav")


def Task_Execution():

    def Music():

        Speak(f"Tell me the name of the song")
        music_name = take_command()
        
        if 'Perfect' in music_name:
                os.startfile('C:/Users/keert/Downloads/Perfect.mp3')
        elif 'Blank Space' in music_name:
                os.startfile('C:/Users/keert/Downloads/blank-space.mp3')
        elif 'vathi raid' in music_name:
                os.startfile('C:/Users/keert/Downloads/Vaathi-Raid-MassTamilan.io.mp3')
        elif 'Shape of you' in music_name:
                os.startfile('C:/Users/keert/Downloads/Shape-Of-You.mp3')
        else:
                Speak("Song not found locally. Playing on YouTube.")
                pywhatkit.playonyt(music_name)
                Speak("playing song,enjoy your music ma'am ")
    
    def OpenApps(query):
        Speak("Ok mam wait a second")

        if 'code' in query:
            os.startfile('"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Microsoft Edge.lnk"')

        elif 'excel' in query:
            os.startfile('"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel.lnk"')

        elif 'gitHub' in query:
            os.startfile('https://github.com/')

        elif 'chrome' in query:
            os.startfile('"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome.lnk"')
            
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/place/Dwaraka+Doss+Goverdhan+Doss+Vaishnav+College/@13.0741295,80.2134855,15z/data=!4m6!3m5!1s0x3a5266a2b44ea549:0x24732a5af8f16afd!8m2!3d13.0741295!4d80.2134855!16zL20vMDNkZ2Ni?entry=ttu')
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'telegram' in query:
            webbrowser.open('https://www.telegram.com')

        Speak("Your command has been completed")

    def SpeedTest(query):
        import speedtest
        Speak("Checking speed...")
        st = speedtest.Speedtest()
        downloading = st.download()
        correctDown = int(downloading / 800000)
        uploading = st.upload()
        correctUpload = int(uploading / 800000)

        Speak(f"The Downloading speed is {correctDown} mbps and the uploading speed is {correctUpload} mbps")
        print(f"The Downloading speed is {correctDown} mbps and the uploading speed is {correctUpload} mbps")


        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUpload} mbp s")
        elif 'downloading' in query:
            Speak(f"The Downloading speed is {correctDown} mbp s")
        else:
            Speak(f"The Downloading speed is {correctDown} and the uploading spped is {correctUpload} mbp s")
            

    def Temp():
        search = "temperature in chennai"
        url = "https://www.google.com/search?q=temperature+in+chennai&rlz=1C1OPNX_enIN1096IN1099&oq=temperature+in+chenn&gs_lcrp=EgZjaHJvbWUqDAgAECMYJxiABBiKBTIMCAAQIxgnGIAEGIoFMgYIARBFGDkyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgASoAgCwAgA&sourceid=chrome&ie=UTF-8"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The temperature outside is {temperature}")

    def Reader():
        Speak("Tell me the name of the book")

        name = take_command()

        if 'grammar' in name:
            os.startfile('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/englishgrammarbook.pdf')
            book = open('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/englishgrammarbook.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page i have to start reading?")
            numPage = int(input("enter the page number"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, i have to read?")
            lang = take_command()

            if 'english' in lang:
                transl = Translator()
                textMal = transl.translate(text, 'en')
                textm = textMal.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    Speak(text)
            else:
                Speak(text)

        elif 'novels' in name:
            os.startfile('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Asura.pdf')
            book = open('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Asura.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page i have to start reading?")
            numPage = int(input("enter the page number"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, i have to read?")
            lang = take_command()

            if 'Tamil' in lang.lower():
                transl = Translator()
                textMal = transl.translate(text, 'ta')
                textm = textMal.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    Speak(text)
            else:
                Speak(text)

        elif 'operating system' in name:
            os.startfile('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Operating System.pdf')
            book = open('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Operating System.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of pages in this book are {pages}")
            Speak("From which page i have to start reading?")
            numPage = int(input("enter the page number"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In which language, i have to read?")
            lang = take_command()

            if 'english' in lang:
                transl = Translator()
                textMal = transl.translate(text, 'en')
                textm = textMal.text
                speech = gTTS(text=textm)

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    Speak(text)
            else:
                Speak(text)

    def CloseApps(query):
        Speak("Ok sir wait a second")

        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'telegram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'notion' in query:
            os.system("TASKKILL /F /im Notion.exe")
        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")
        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'git' in query:
            os.system("TASKKILL /F /im git-bash.exe")

        Speak("Your command has been successfully completed")

    def YoutubeAuto():
        Speak("What's your command")
    comm = take_command()

    if 'stop' in comm:
        keyboard.press('space bar')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'silent please' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    elif 'film mode' in comm:
        keyboard.press('t')

    elif 'move to the previous' in comm:
        keyboard.press('shift')
        keyboard.press('p')
        keyboard.release('shift')

    elif 'move to the next' in comm:
        keyboard.press('shift')
        keyboard.press('n')
        keyboard.release('shift')  

    Speak("Done sir")

    def TakeMalayalam():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing....")
                query = command.recognize_google(audio, language='ml')
                print(f"You Said:{query}")
            except:
                return "none"
            return query.lower()

    def Tran():
        Speak("Tell me the line")
        line = TakeMalayalam()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak("The translation for this line is " + Text)

    def ChromeAuto():
        Speak("Chrome Automation started")
        command = take_command()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def Dict():
        Speak("activated dictionary")
        Speak("Tell me the word")
        probl = take_command()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("meaning of", "")
            result = Diction.meaning(probl)
            Speak(f"The meaning for {probl} is {result}")
            print(f"The meaning for {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("synonym of", "")
            result = Diction.synonym(probl)
            Speak(f"The synonym for {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("adora", "")
            probl = probl.replace("of", "")
            probl = probl.replace("antonym of", "")
            result = Diction.antonym(probl)
            Speak(f"The antonym for {probl} is {result}")

        Speak("Exited Dictionary")
        print("Exited Dictionary")


    def screenshot():
        Speak("Ok boss, what should i name that file")
        path = take_command()
        path1name = path + ".png"
        path1 = "C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/screenshot/" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/screenshot")
        Speak("Here is your screenshot")


    while True:
        query = take_command()

        if 'hello' in query:
            Speak("Hello boss," " iam adora")
            Speak("Your personal virtual assistant")
            Speak("How may i help you")
        
        elif 'how are you' in query:
            Speak("i am fine mam")
            Speak("whats about you")

        elif 'you need a break' in query:
            Speak("Ok ma'am," "You can call me anytime")
            break

        elif 'i am worried' in query:
            Speak("Go and take a short break you will feel better")

        elif 'ok see you' in query:
            Speak("Ok bye see you soon")
            break

        elif 'name of hod' in query:
            Speak("DR.p.suganya department of computer science ")
            
        elif 'stupid' in query:
            Speak("sorry if am worng")
            break

        elif 'am give up' in query:
            Speak("no you can...Fight for it boss")
            
        elif 'bye' in query:
            Speak("Ok sir, Bye")
            break

        elif 'who is this' in query:
            Speak("Hello boss, I am Adora. Your personal virtual assistant. How may I help you?")

        elif 'who is your developer' in query:
            Speak("kiruthiga rajagopal developed me in march 2024, for their final year project,from DG VAISHNAV college")

        elif 'send email' in query:
            send_email("Test Subject", "This is a test email message.", "yuvidiya12@gmail.com")
            Speak("Email sent successfully.")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            Speak(f"the time is:{strTime}")
            print(strTime)
            

        elif 'youtube search' in query:
            Speak("Ok sir, This is what I found for your search")
            query = query.replace('adora', "")
            query = query.replace("youtube search", "")
            query = query.replace('paly', "")
            web = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak("Done sir")

        elif 'google search' in query:
            Speak("This is what I found for you")
            query = query.replace('adora', "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            Speak('Done ')

        elif 'website' in query:
            Speak("Ok sir, launching..")
            query = query.replace('adora', "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched ")

        elif 'launch' in query:
            Speak("Tell me the name of the website")
            name = take_command()
            query = query.replace('adora', "")
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done mam")

        elif 'facebook' in query:
            Speak("Ok ma'am")
            webbrowser.open("https://www.facebook.com")
            Speak("Done ma'am")

        elif 'music' in query:
            Music()

        elif 'wikipedia search' in query:
            Speak("Searching Wikipedia")
            query = query.replace("adora", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"According to Wikipedia :{wiki}")    

        elif 'whatsapp message' in query:
            query = query.replace("adora", "")
            query = query.replace("send to", "")
            query = query.replace("whatsapp message", "")
            query = query.replace("to", "")
            name = query

            if 'mani thatha' in name:
                number = "+91 9952020057"
                Speak(f"What's the message for {name}")
                message = take_command()
                whatsapp_Message(number, message)
                Speak("Ok boss, sending WhatsApp message")
                Speak("if you press enter, your message sucessfully send")

            elif 'yuve' in name:
                number = "+91 8925649684"
                Speak(f"What's the message for {name}")
                message = take_command()
                whatsapp_Message(number, message)
                Speak("Ok boss, sending WhatsApp message")
                Speak("if you press enter, your message sucessfully send")

            elif 'mental hospital' in name:
                number = "+91 6382204006"
                Speak(f"What's the message for {name}")
                message = take_command()
                whatsapp_Message(number, message)
                Speak("Ok boss, sending WhatsApp message")
                Speak("if you press enter, your message sucessfully send")

            elif 'group ' in name:
                group_id = "F304hUHq4yk3hWSU9aJ6WK"
                Speak(f"What's the message for {name}")
                message = take_command()
                Whatsapp_Grp(group_id, message)
                Speak("Ok boss, sending WhatsApp message")
                Speak("if you press enter, your message sucessfully send")

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps(query)

        elif 'open instagram' in query:
            OpenApps(query)

        elif 'open maps' in query:
            OpenApps(query)

        elif 'open code' in query:
            OpenApps(query)

        elif 'open youtube' in query:
            OpenApps(query)

        elif 'open excel' in query:
            OpenApps(query)

        elif 'open chrome' in query:
            OpenApps(query)

        elif 'close chrome' in query:
            CloseApps(query)

        elif 'close notion' in query:
            CloseApps(query)

        elif 'close facebook' in query:
            CloseApps(query)

        elif 'close instagram' in query:
            CloseApps(query)

        elif 'close telegram' in query:
            CloseApps(query)

        elif 'close maps' in query:
            CloseApps(query)

        elif 'close code' in query:
            CloseApps(query)

        elif 'close git' in query:
            CloseApps(query)

        elif 'close youtube' in query:
            CloseApps(query)

        # Youtube automation
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')
            
        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'move to the next' in query:
            keyboard.press('shift + p')

        elif 'move to the previous' in query:
            keyboard.press('shift + n')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'chrome automation' in query:
            ChromeAuto()
            

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
            
        elif 'repeat my words' in query:
            Speak("speak sir")
            jj = take_command()
            Speak(f"you said: {jj}")

        elif 'my location' in query:
            Speak("ok sir, wait a second")
            webbrowser.open('https://www.google.com/maps/place/Dwaraka+Doss+Goverdhan+Doss+Vaishnav+College/@13.0741295,80.2134855,15z/data=!4m6!3m5!1s0x3a5266a2b44ea549:0x24732a5af8f16afd!8m2!3d13.0741295!4d80.2134855!16zL20vMDNkZ2Ni?entry=ttu')
        
        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter the time")
            time = input(": enter the time:")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up boss")
                    playsound("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/Alarm.mp3")
                    Speak("boss alarm closed")
                elif now > time:
                    break
        
        elif 'translator' in query:
                    Tran()

        elif 'remember ' in query:
                    rememberMsg = query.replace("remember that", "")
                    rememberMsg = rememberMsg.replace("adora", "")
                    Speak(f"You tell me to remind you that: "+rememberMsg)
                    remember = open('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Data.txt', 'w')
                    remember.write(rememberMsg)
                    remember.close()

        elif 'what do you remember' in query:
                    remember = open('C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/Data.txt', 'r')
                    Speak("You tell me that:" +remember.read())

        elif 'google scrap' in query:
                    import wikipedia as googleScrap
                    query = query.replace('adora',"")
                    query = query.replace("google scrap", "")
                    query = query.replace("google", "")
                    Speak("This is what I found on the web")
                    pywhatkit.search(query)

    

        if 'temperature' in query:
                Temp()

        elif 'read a book' in query:
            Reader()

        elif 'downloading speed' in query:
            SpeedTest(query)

        elif 'uploading speed' in query:
            SpeedTest(query)

        elif 'internet speed' in query:
            SpeedTest(query)


        elif 'seat belt status' in query:
            seatbelt_alert()
            Speak("please fasten your seatbelt for safety")
        

        elif 'how to' in query:
            Speak("Getting data from the internet")
            op = query.replace("adora", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            
        elif 'video downloader' in query:
            from pytube import YouTube
            import pytube.cli as pytube

            Speak("Enter the url")
            url = input("Enter the url")

            yt = YouTube(url)
            videos = yt.streams.all()

            for video in videos:
                print(video)

            num = input("Enter the number")
            vid = videos[int(num)]
            vid.download()
            Speak("Downloaded")
            
        elif 'quit' in query:
            Speak("Ok bye see you soon")
            break

        elif 'chat' in query:
            reply = ChatBot.chatterBot(query)
            if reply == "none":
                Speak("Sorry, I didn't understand that. Can you please repeat?")
            else:
                Speak(reply)

        


        
if __name__ == '__main__':
        Task_Execution()
       
