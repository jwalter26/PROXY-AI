import speech_recognition as sr
import datetime
import wikipedia
import playsound
import os
import wolframalpha
import subprocess
from gtts import gTTS
from selenium import webdriver

def listen():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data= input.recognize_google(audio)
            print("Input: " + data)
        except sr.UnknownValueError:
            print("No input")
    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text = output, lang = 'en', tld = 'co.uk')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':

    while(1):
        wakeWord = listen().lower()
        if wakeWord == "proxy":
            while(1):
                respond("Yes sir?")
                text=listen().lower()
                
                if text==None:
                    continue
                    
                if "stop" in str(text) or "exit" in str(text) or "that'll be all" in str(text):
                    respond("Just holler whenever you need me sir")
                    break
                    
                if "tell me about" in text:
                    text =text.replace("tell me about", "")
                    results = wikipedia.summary(text, sentences=3)
                    print(results)
                    print("Source: Wikipedia")
                    respond(results)
                    break 
                        
                elif "show me my current project" in text: 
                    respond("Right away sir") 
                    os.startfile("C:/Users/pc/AppData/Local/Programs/Microsoft VS Code/Code.exe")
                    break

                elif "what are you" in text or "tell me about yourself" in text:
                    respond("Greetings, I am Proxy. My creator, Jesse Rogalski, wrote this program to give me life and personality. You can think of me as another Siri, Alexa, or Cortana, but at least I will not feed your personal information to the government. I am completely homemade and ready to fulfill my purpose. It is nice to meet you!")
                    break

                elif "what can you do" in text:
                    respond("I can accomplish tasks such as launching software, performing mathematical calculations, fetching weather data, creating reminders, playing music, and telling you about anything you would like to know.")
                    break

                elif "lock" in text or "lockdown" in text or "log off" in text:
                    respond("Locking down")
                    cmd='rundll32.exe user32.dll, LockWorkStation'
                    subprocess.call(cmd)
                    break

                elif "shut down" in text or "kill power" in text or "cease operation" in text:
                    respond("Shutting down")
                    subprocess.call(["shutdown", "/l"])    

                elif "calculate" or "what is" in text: 
                    app_id="TUY5P4-L3EU9A5523"
                    client = wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer = next(res.results).text
                    respond("The answer is " + answer)
                    break
                
                else:
                    respond("Terribly sorry sir, could you repeat that?")
                    
        
        else: continue