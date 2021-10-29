from re import search
import speech_recognition as sr
from datetime import datetime
from pytz import timezone
import wikipedia
import playsound
import os
import wolframalpha
import clr
import subprocess
from distutils import spawn
from shutil import which
import winapps
from gtts import gTTS

def listen():
    input = sr.Recognizer()
    data = ""
    while (data == "" or data == None):
        with sr.Microphone() as source:
            audio = input.listen(source)
            try:
                data= input.recognize_google(audio)
            except sr.UnknownValueError:
                continue
    return data

def respond(output):
    print(clr.bold(output))
    response=gTTS(text = output, lang = 'en', tld = 'co.uk')
    file = "input.mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':
    while(1):
        wakeWord = listen().lower()
        print(wakeWord)
        if "proxy" in wakeWord:
            while(1):
                print("Input: " + wakeWord)
                respond("Yes sir?")
                text=listen().lower()
                
                if text==None:
                    continue
                
                if "remind me to" in text:
                    break

                if "search" in text:
                    print("Input: " + text)
                    searchFile = text.replace("search ","")
                    print(searchFile.strip(" "))
                    fileCount = 0
                    for root, dirs, files in os.walk("C:/Users/pc/"):
                        if searchFile in root:
                            print(os.path.join(root,searchFile))
                            fileCount += 1
                        if searchFile in dirs:
                            print(os.path.join(root,searchFile))
                            fileCount += 1
                        if searchFile in files:
                            print(os.path.join(root,searchFile))
                            fileCount += 1
                    if fileCount == 0:
                        respond("I'm sorry, I could not find any results based on your search query")
                        break
                    else: 
                        respond("I found " + str(fileCount) + " results based on your search query")
                        break
                
                if "stop" in str(text) or "exit" in str(text) or "that'll be all" in str(text):
                    print("Input: " + text)
                    respond("Just holler whenever you need me sir")
                    exit()
                    
                if "tell me about" in text:
                    print("Input: " + text)
                    text =text.replace("tell me about", "")
                    try:
                        results = wikipedia.summary(text, sentences=3)
                    except wikipedia.exceptions.PageError:
                        respond("I am sorry sir, I could not find any data on that topic")
                        break
                    respond(results)
                    print(clr.bold("Source: Wikipedia"))
                    break 

                elif "launch" in text:
                    print("Input: " + text)
                    searchName = text.replace("launch ", "")
                    app = searchName.replace(" ", "")
                    respond("Launching " + searchName)
                    for a in winapps.search_installed(searchName):
                        print(a.install_location)
                    os.system("PATH %PATH%" + str(a.install_location))
                    print(os.system("path"))
                    print(app)
                    exePath = os.system("where " + app)
                    print(exePath)
                    #os.startfile(exePath)
                    break

                elif "what are you" in text or "tell me about yourself" in text:
                    print("Input: " + text)
                    respond("Greetings, I am PROXY. My creator, Jesse Rogalski, wrote this program to give me life and personality. You can think of me as another Siri, Alexa, or Cortana, but at least I will not feed your personal information to the government. I am completely homemade and ready to fulfill my purpose. It is nice to meet you!")
                    break

                elif "what can you do" in text:
                    print("Input: " + text)
                    respond("I can accomplish tasks such as launching software, performing mathematical calculations, fetching weather data, creating reminders, playing music, and telling you about anything you would like to know.")
                    break

                elif "lock" in text or "lockdown" in text or "log off" in text:
                    print("Input: " + text)
                    respond("Locking down")
                    cmd='rundll32.exe user32.dll, LockWorkStation'
                    subprocess.call(cmd)
                    break

                elif "shut down" in text or "kill power" in text or "cease operation" in text:
                    print("Input: " + text)
                    respond("Shutting down")
                    subprocess.call(["shutdown", "/l"])

                elif "calculate" or "what is" or "tell me about" in text:
                    print("Input: " + text)
                    app_id="TUY5P4-L3EU9A5523"
                    client = wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer = next(res.results).text
                    respond("The answer is " + answer)
                    break
                
                else:
                    print("Input: " + text)
                    respond("Terribly sorry sir, could you repeat that?")
        else: continue