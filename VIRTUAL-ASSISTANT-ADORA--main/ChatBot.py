import random

command_1 = ['hello',
             'wake up',
             'are you there',
             'hey',
             'hi',
             'help me']

reply_1 = ['hello boss', 'welcome back', 'always for you boss',
           'how can i help you',
           'welcome back boss, how can i help you Boss',
           'hi boss, Is there any work for me',
           'hey there, how are you boss',
           'nice meeting you again boss',
           'hope you missed me, how can i help you',
           'hi boss, how are you']

command_2 = ['bye',
             'go and sleep',
             'sleep']

reply_2 = ['bye boss',
           'nice meeting boss']
command_3 = ['how are you', 'what\'s up', 'how\'s it going']
reply_3 = ['I\'m doing well, thank you!', 'Not much, just here to help. How can I assist you?']

# chatterBot function



def chatterBot(Text):

    for word in Text.split():
        if word in command_1:
            return random.choice(reply_1) + "."
        elif word in command_2:
            return random.choice(reply_2) + "."
        elif word in command_3:
            return random.choice(reply_3) + "."

