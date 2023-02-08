from typing_extensions import Self
import speech_recognition as sr
import random
import requests
import datetime
import pyttsx3
import pyautogui
import os
import sys
import time
from time import sleep  
import webbrowser
import requests
import pywhatkit
import psutil, pyttsx3, math 
import wikipedia
import json
#user interface
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
import time
from imageio import imopen
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

#button
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#computational intelligence
import wolframalpha
app_id="GQ8PHQ-V7R6WA3EKU"
app = wolframalpha.Client(app_id)

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

GREETINGS = ['hello ', 'DYPIAN', 'wake up', 'you there DYPIAN', 'time to work DYPIAN', 'hey DYPIAN',
             'ok DYPIAN', 'are you there']
GREETINGS_RES = ['always there for you sir', 'i am ready sir',
                 'your wish my command', 'how can i help you sir?', 'i am online and ready sir']


def speak(audio):
    Assistant.say(audio)
    print(f":{audio}")
    Assistant.runAndWait()

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning SIR !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon SIR !")   

    else:
        speak("Good Evening SIR !")  

    speak("I am D.Y.P.I.A.N. the student A.I. assistant! Sir. Please tell me how may I help you")


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("Give me command sir ")
        print("Listening.......")
        command.pause_threshold = 1
        audio = command.listen(source,0,5)

        try:
            #speak("Please wait sir")
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"
        query =str(query)
        return query.lower()



def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   print("%s %s" % (s, size_name[i]))
   return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory}  is being used and battery level is at {battery_percent} percent"
    print("System status is :")
    print(final_res) 
    speak(final_res)

def loc(place):
    webbrowser.open("http://www.google.com/maps/place/" + place + "")
    

def my_location():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    print(city, state,country)
    speak(city)
    speak(state)
    speak(country)

def tell_me_about(topic):
    try:
        
        res = wikipedia.summary(topic, sentences=3)

        return res 
    except Exception as e:
        print(e)
        return False


def get_news():
    url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'


def command():
    speak("Sir , please give me command")
    while True:
        query = takecommand()
        #Normal conversastion
        if 'hello' in query:
            speak("Hello sir,I am D y pian the student assistant .")
            speak("your Personal AI Assistant")
            speak("How may I Help you?")
        
        elif 'how are you' in query:
            speak("I am fine sir!")
            speak("Whats about you?")
        
        
            
        elif 'fine'  in query or 'nice'  in query :
            speak("Ok sir , great")
            speak("Whats can i do for you?")
        
        elif query  in GREETINGS  :
                speak(random.choice(GREETINGS_RES))
        
        #Information about project
        elif 'project' in query:
            speak("OK Sir")
            speak("Project name is A I assistant for DPU students")
            speak("Team members are Vaibhav ,krishna ,Ayush and Dhiraj")
            speak("""Features of Our project is that Our A I Assistant offers voice commands,voice searching, 
                  and voice-activated device control, letting you complete a number of tasks . 
                  It is designed to give you conversational interactions to solve your queries and 
                  doubt regarding college issues .""")
        
        # Automation of different function
        elif 'google search' in query:
            speak('this is I found for your search')
            query=query.replace('DYPIAN'," ")
            query=query.replace ('google search'," ")
            pywhatkit.search(query)
            speak('done sir')
        
        elif 'youtube search ' in query:
            query=query.replace('DYPIAN'," ")
            query=query.replace ('youtube search'," ")
            web = 'https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            speak("done sir!")
        
        elif 'open stack overflow' in query or 'stack overflow' in query:
            speak("ok sir i will open the stack over flow website")
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open vs code' in query or 'vs code' in query:
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")
        
        elif 'open dev c plus plus  ' in query or 'dev editor' in query:
            codePath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")

        elif 'open python idle' in query or 'python editor' in query:
            codePath = "C:\\Python39\\pythonw.exe"
            os.startfile(codePath)
            speak("done sir,now start coding ")

        elif "open pbl report" in query or 'pbl report' in query:
         os.startfile("C:\\FOURTH SEMSTER\\PBL\\PBL_F.pptx")
        
        elif "buzzing" in query or "news" in query or "headlines" in query:
                news_res = get_news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    print(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')
       

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        # windows shortcut keys 
        elif "switch the window" in query or "switch window" in query  :
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(0.5)
                pyautogui.keyUp("alt")
        
        elif  "close window" in query  :
                speak("Okay sir, Closing the window")
                pyautogui.keyDown("Ctrl")
                pyautogui.press("W")
                time.sleep(0.5)
                pyautogui.keyUp("Ctrl")

        elif "increase volume" in query  :
                speak("Okay sir, increasing the volume")
                pyautogui.keyDown('volumeup')
                time.sleep(1.0)
                pyautogui.keyUp('volumeup')
        
        elif "Shut up" in query  :
                speak("Okay sir, I am switching to mute mode ")
                pyautogui.hotkey('volumemute')
               

        elif "shrink" in query:
                speak("Okay sir, minimizing the window")
                pyautogui.keyDown("win")
                pyautogui.press("m")
                pyautogui.keyUp("win")
                
        elif "restore" in query:
                speak("Okay sir, restoring the window")
                pyautogui.keyDown("win")
                pyautogui.keyDown("shift")
                pyautogui.press("m")
                pyautogui.keyUp("win")
                pyautogui.keyUp("shift")
       
        elif "lock" in query:
                speak("Okay sir, locking the pc")
                pyautogui.hotkey('win', 'r') 
                pyautogui.typewrite("cmd\n") 
                sleep(0.500)       
                pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation\n")

        elif "menu" in query:
                speak("Okay sir, this is start menu")
                pyautogui.hotkey("win")

        #computational intelligence using wolfram alpha
        elif "calculate" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
            
        elif "what is" in query or "who is" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)

        elif "which is" in query or "which" in query:
                question = query
                answer = computational_intelligence(question)
                speak(answer)
        elif "where is" in query:
              place = query.split('where is ', 1)[1]
              loc(place)
       
    #college information
        elif "erp" in query or 'erp portal' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://campus.dpuerp.in/Secured/DashBoardStudent.aspx")
       
        elif "Admission" in query or 'Admission process' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/ugadmissions.aspx")

        elif "college" in query or 'Profile' in query or 'college profile' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/college-profile.aspx")

        elif "computer engineering" in query or 'computer branch' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/computer-engineering.aspx")

        elif "Academics" in query :
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/Acadmic-Calender.aspx")

        elif " Training and placement" in query :
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/from-the-desk-of-tpo.aspx")

        elif " Computer engineering placements " in query or 'placement' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/placements.aspx")

        elif "University rankers" in query or 'Toppers' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/university-rankers.aspx")

        elif "mission" in query or 'vision' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/vision-mission.aspx")

        elif "Computer engineering faculty" in query or 'faculty ' in query or ' staff ' in query:
            speak("ok sir ,this is found for your query")
            webbrowser.open("https://engg.dypvp.edu.in/computer-engineering-faculty-and-staff.aspx")
        
        
        
        
        
        # system exit
        elif "goodbye" in query or "offline" in query or "bye" in query or "exit" in query:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()
        
        elif 'pause' in query:
            speak("Ok sir")
            break

        elif 'shutdown' in query:
           speak("Do you wish to shutdown your computer ? (yes shut down / no): ")
  
           if 'Yes shutdown' in query:
              os.system("shutdown /s /t 1")
           else:
               break
        
        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
        
        elif "system status" in query:
                system_stats()

        elif "my location" in query:
            speak("Your current locationis :")
            my_location()        

        else:
            speak("Command not found, Please speak again !")
            print("command not found")

#user interface functions
def dpu():
    speak("ok sir i will open the dpu website")
    webbrowser.open("https://engg.dypvp.edu.in/")



FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        #self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.setGeometry(0,0,1920,1080)
        self.setWindowFlags(flags)
        
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))
#ui button keys
        

        self.pushButton1 = QtWidgets.QPushButton(self)
        self.pushButton1.setText("Dpu_website")
        self.pushButton1.setFont(QFont('Arial', 30))
        self.pushButton1.setStyleSheet("color:white")
        self.pushButton1.setGeometry(QtCore.QRect(50,600,375,80))
        self.pushButton1.clicked.connect(Dpu_clicked)
        self.pushButton1.setStyleSheet('QPushButton { color: white;}')
        
        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setText("Run")
        self.pushButton2.setFont(QFont('Arial', 30))
        self.pushButton2.setStyleSheet("color:white")
        self.pushButton2.setGeometry(QtCore.QRect(250,200,200,80))
        self.pushButton2.clicked.connect(Run_clicked)
        

        self.pushButton3 = QtWidgets.QPushButton(self)
        self.pushButton3.setText("Stop")
        self.pushButton3.setFont(QFont('Arial', 30))
        self.pushButton3.setStyleSheet("color:white")
        self.pushButton3.setGeometry(QtCore.QRect(50,400,375,80))
        self.pushButton3.clicked.connect(Stop_clicked)

        
        
 
        self.setStyleSheet("background-image : url(./lib/tus.png); border : 2px solid blue")

def Run_clicked():
   command()

def Stop_clicked():
   exit()

def Dpu_clicked():
    dpu()

#convert_size(1)
#system_stats()
wishMe()

app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())