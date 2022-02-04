from gtts import gTTS
import speech_recognition as sr
import clr
import playsound
import os
from General import *
from Tools import *
from System import *
from Lists import *
import settings

async def listen():
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

async def respond(output):
    print(clr.bold(output))
    response=gTTS(text = output, lang = 'en', tld = 'co.uk')
    file = "input.mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':
    while(1):
        wakeWord = listen().lower()
        if settings.wakeWord in wakeWord:
            while(1):
                print("Input: " + wakeWord)
                respond("Yes " + settings.name + "?")
                text=listen().lower()
                print("Input: " + text)
            
                if text==None:
                    continue
                
                elif "remind me to" in text:
                    reminders()
                    break

                elif "search" in text:
                    findFiles()
                    break 
                
                elif "quit" in text or "exit" in text:
                    killProxy()
                    
                elif "tell me about" in text:
                    research(text)
                    break 

                elif "launch" in text:
                    launchApp()
                    break

                elif "what are you" in text or "tell me about yourself" in text:
                    about()
                    break

                elif "what can you do" in text:
                    features()
                    break

                elif "lock" in text or "lockdown" in text or "log off" in text:
                    lockPC()
                    break

                elif "shut down PC" in text or "kill power" in text:
                    shutDown()
                    break

                elif "calculate" in text or "what is" in text:
                    doMath()
                    break
                
                else:
                    ProxyDoesNotKnow()
                    break
        else: continue