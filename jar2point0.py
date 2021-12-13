
import pyttsx3
import datetime
import speech_recognition as sr

import wikipedia
import webbrowser
import os
import smtplib 
import text_reader as tx

# generate random integer values
from random import seed
from random import randint
# seed random number generator

def ran(b):
    seed(1)
    return randint(0, b)

def sendGmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(tx.fnr('User'), tx.fnr('password'))
    server.sendmail(tx.fnr('User'), to, content)
    server.close()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant Ma'am. Please tell me how may i help you?")

def sendEmail():
    try:
        speak("To whom should i send email?")
                
        var = input("Enter name (audio input not avaliable for this Sorry): ")
        speak("What should I say?")
        content = takeCommand()
        to = tx.fnr(var)    
        sendGmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry my friend. I am not able to send this email")    


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return query

def play_music():
    music_dir = 'C:\\Users\\Aryan Pande\\Music\\songs'
    songs = os.listdir(music_dir)
    #print(len(songs))
    # print(songs)
    rn=ran(len(songs))
    os.startfile(os.path.join(music_dir, songs[rn]))

def callopen(query):
    if 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open chess.com' in query:
         webbrowser.open("chess.com")

    elif 'open insta' in query:
        webbrowser.open("instagram.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open google' in query:
        webbrowser.open("google.com")
    elif'open vs code' in query:
        codepath = "C:\\Users\\Aryan Pande\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

def callwiki(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia")
    print( results)#optional
    speak(results)

if __name__ == "__main__":
    # print("working")
    wishme()
    # print(tx.fnr())
    go = True
    while go:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  
            
            callwiki(query)

        elif 'open' in query:
            callopen(query)
           
        elif'play music' in query:
            play_music()

        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send email' in query:
            sendEmail()
        
        elif'stop' in query:
            break
        

 
