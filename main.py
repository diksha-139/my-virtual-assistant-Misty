from email.mime import audio
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pyttsx3 import engine

print('initializing misty')

MASTER = "diksha"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning..." + MASTER)
    elif hour >= 12 and hour < 16:
        speak("good afternoon..." + MASTER)
    else:
        speak("good evening..." + MASTER)

    # speak("i am misty. How may i help you?")


# this function will take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        aud = r.listen(source)

    try:
        print('recognizing...')
        query1 = r.recognize_google(aud)

        print("user said: {}".format(query1))

    except Exception as e:
        print("say that again please...")
        query1 = None
    return query1


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('teacherinwhitehat@gmail.com', 'teacher@whitehat')
    server.sendmail("diksha.verma139@gmail.com", to, content)
    server.close()


# Main program starts here
def main():
    speak("Initialising misty...")

    wishMe()
    speak("what you want me to do?...")
    query1 = takeCommand()

    # Logic for executing basic tasks as per the query
    if 'wikipedia' in query1.lower():
        speak("searching wikipedia...")
        query1 = query1.replace("wikipedia", " ")
        results = wikipedia.summary(query1, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query1.lower():
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query1.lower():
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'open w3schools' in query1.lower():
        url = 'https://www.w3schools.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'open camera' in query1.lower():
        photos_dir = 'C:\\Users\\Lenovo\\Pictures\\Camera Roll'
        photos = os.listdir(photos_dir)
        print(photos)
        os.startfile(os.path.join(photos_dir, photos[0]))


    elif 'open github' in query1.lower():
        url = 'https://www.github.com/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        webbrowser.get(chrome_path).open(url)

    elif 'the time' in query1.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("{} the time is {}".format(MASTER, strTime))


    elif 'open zoom' in query1.lower():
        zoom_dir = 'C:\\Users\\Lenovo\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
        os.startfile(zoom_dir)

    elif 'email to diksha' in query1.lower():
        try:
            speak("what should i send?...")
            content = takeCommand()
            to = "diksha.verma139@gmail.com"
            sendEmail(to, content)
            speak("email has been sent successfully")

        except Exception as e:
            print(e)


main()
