
from AdoraUi import Ui_AdoraUi
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
import Main
import os
import webbrowser as web
import sys

class Mainthread(QThread):

    def __init__(self):
        super(Mainthread, self).__init__()

    def run(self):
      Main.Task_Execution()

startExe = Mainthread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_AdoraUi()
        self.gui.setupUi(self)

        self.gui.PushButton_Start.clicked.connect(self.startTask)
        self.gui.PushButton_Exit.clicked.connect(self.close)
        self.gui.pushButton_Chrome.clicked.connect(self.chrome_app)
        self.gui.PushButton_Whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.pushButton_YouTube.clicked.connect(self.yt_app)

    def chrome_app(self):
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("C:\\Users\\keert\\OneDrive\\Desktop\\FINAL-PROJECT\\label1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/adora.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/label3.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/wave.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("C:/Users/keert/OneDrive/Desktop/FINAL-PROJECT/VIRTUAL-ASSISTANT-ADORA--ADORA-MODELS/books/7VTb.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        startExe.start()


GuiApp = QApplication(sys.argv)
adora_gui = Gui_Start()
adora_gui.show()
exit(GuiApp.exec_())