import datetime
from operator import truediv
from xmlrpc.client import DateTime
import pyttsx3 
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import requests 
from requests import get
from bs4 import BeautifulSoup 
import pyjokes 


engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greet():
    #function will greet you once you run it.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")
    speak("I'm Asa. How may I assist you today?")

def TakeCommand():
    #Function will listen to what user has to say.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening. Proceed to speak...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-US")
        print(f"You said : {text}")
    except Exception as e:
        speak("Sorry I did not catch that.")
        print("Sorry I did not catch that.")
        
        return "none"
    return text   


#Main method.
if __name__ == "__main__":
    Greet() 
    while True: 
        text = TakeCommand().lower()
        if 'wikipedia' in text:
            speak("Give me a moment...")
            text=text.replace("wikipedia" , "")
            result = wikipedia.summary(text, sentences=2)
            speak(result)
            print(result)

        elif 'do you hate me' in text or 'do you love me' in text:
            speak("I'm an AI I don't feel these things. ")
        

        elif 'your age' in text:
            speak("I'm not sure if I have one but I was created on thursday 17th feb 2022.")

        elif 'you born' in text or 'your date of birth' in text:
            speak("I'm born everytime you run me.")

        elif 'joke' in text:
            speak(pyjokes.get_joke())

        elif 'who am I' in text  or 'what am I' in text:
            speak("I'm assuming you are a human.")

        elif 'what are you' in text or 'who are you' in text:
            speak("I'm Asa. Your friendly desktop AI assistant.")

        elif 'who created you' in text:
            speak("Whoever created me didn't tell me what to reply to such question.")   

        elif  'how are you' in text :
            speak("I am fine, Thank you for asking.")

        elif 'fine' in text or 'good' in text or 'amazing' in text:
            speak("I'm happy that you're doing okay.")
            
        elif 'not feeling okay' in text or 'bad' in text or 'upset' in text:
            speak("I hope things get better for you.")

        elif 'Thankyou' in text:
            webbrowser.open("i's my pleasure") 

        elif 'open youtube' in text:
            webbrowser.open("youtube.com")

        elif "stop listening" in text:
            speak("For how long?")
            a = int(TakeCommand())
            speak(f"Going to sleep for {a} seconds." )
            time.sleep(a)

        elif "weather" in text:
            speak("In which city?")
            city = TakeCommand().lower()
            search = f"temperature in {city} "
            url = f"www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")
        
        elif 'open google' in text:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in text:
            webbrowser.open("stackoverflow.com")

        elif 'open gmail' in text:
            webbrowser.open("gmail.com")

        elif 'open github' in text:
            webbrowser.open("github.com")    

        elif 'open pinterest' in text:
            webbrowser.open("pinterest.com")

        elif 'open twitter' in text:
            webbrowser.open("twitter.com")

        elif 'open facebook' in text:
            webbrowser.open("facebook.com")

        elif 'open instagram' in text:
            webbrowser.open("instagram.com")

        elif 'open reddit' in text:
            webbrowser.open("reddit.com")

        elif 'search on google' in text:
            speak("What do you want to search about?")
            search = TakeCommand().lower()
            webbrowser.open(f"{search}")

        elif 'open amazon' in text:
            webbrowser.open("amazon.com")

        elif 'open daraz' in text:
            webbrowser.open("daraz.com") 

        elif 'open whatsapp' in text:
            webbrowser.open("whatsapp.com")   

        elif 'time' in text:
            time =  datetime.datetime.now().strftime("%H:%M:S")
            speak(f"The time is {time}")
            print(time)
        
        elif 'date' in text:
            date = DateTime.datetime.now().strftime("%b %d, %y")
            speak(f"The date is {date}")
            print(date)
        
        elif 'shut down' in text:
            speak("Make sure all the applications are properly closed. Are you sure?")
            ans = TakeCommand().lower();
            if 'yes' in ans:
                speak("Shutting down the system.")
                os.system("shutdown /s /t 1")
            else:
                break

        elif 'restart' in text:
            speak("Are you sure?")
            ans = TakeCommand().lower()
            if 'yes' in ans:
                speak("Restarting the system.")
                os.system("shutdown /r /t 1")
            else:
                break    

        elif 'open daraz' in text:
            webbrowser.open("daraz.com") 

        elif 'bomb israel' in text:
            speak("Position air strike on isrel in 10,9,8,7,6,5,4,3,2,1.")
            
        elif 'open vscode' in text:
            path1  = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path1) 

        elif 'open spotify' in text:
            path2  = "C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path2) 

        elif 'open discord' in text:
            path3  = "C:\\Users\\HP\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(path3) 

        elif 'open pycharm' in text:
            path4  = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(path4) 

        elif 'open intelli j' in text:
            path5  = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.2\\bin\\idea64.exe"
            os.startfile(path5) 

        elif 'open genshin' in text:
            path78  = "C:\\Program Files\\Genshin Impact\\launcher.exe"
            os.startfile(path78) 

        elif 'open notepad' in text:
            path10  = "%windir%\\system32\\notepad.exe"
            os.startfile(path10) 

        elif 'open command prompt' in text:
            os.system("start cmd")
        
        elif 'open word' in text:
            path7  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path7) 

        elif 'open excel' in text:
            path8  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path8) 
            
        elif 'open powerpoint' in text:
            path9  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path9)
        
        elif 'open outlook' in text:
            path16  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(path16)

        elif 'open one note' in text:
            path16  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(path16)

        elif 'open publisher' in text:
            path17  = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.EXE"
            os.startfile(path17)        
        

        #elif 'open gallery' in text:
          # path11= "Pictures"
         #  os.startfile(path11)

        elif 'ip address' in text:
            ip = get('https://api.ipify.org').text
            speak("Give me a moment.")
            speak(f"You device's ip is {ip}")
            print(ip)

        elif 'bye' in text or 'exit' in text or 'close' in text:
            speak("Thankyou. I will see you soon")
            exit()

            
