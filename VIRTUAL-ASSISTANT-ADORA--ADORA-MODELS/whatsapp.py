import webbrowser as web
import time
import keyboard

def whatsapp_Message(number, message):
    numb = '+91' + str(number)
    open_chat = 'https://web.whatsapp.com/send?photo=' + numb + "&text=" + message
    web.open(open_chat)
    time.sleep(10)
    keyboard.press('enter')

def Whatsapp_Grp(group_id, message):
    open_chat = 'https:/web.whatsapp.com/accept?code' + group_id
    web.open(open_chat)
    time.sleep(10)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')
