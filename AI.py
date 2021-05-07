import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import playsound
import os
import wolframalpha
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
            respond("I'm not sure what you mean sir")
    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)

if __name__=='__main__':
    respond("Good evening Mr. Rogalski")
          
    while(1):
        respond("How can I help you?")
        text=listen().lower()
        
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "goodbye" in str(text) or "that will be all" in str(text):
            respond("Just holler whenever you need me sir")
            break
            
        if 'wikipedia' in text or "show me" in text or "tell me about" in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        
        elif 'search' in text or "look up" in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
        
        elif "calculate" or "what is" in text: 
            question=listen()
            app_id="Mention your API Key"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            respond("The answer is " + answer)
            
        elif 'open Google Chrome' in text:
            webbrowser.open_new_tab(requests.get('https://www.google.com'))
            respond("Really? You needed me for that?")
            
        elif 'youtube' in text: 
            driver = webdriver.Chrome(r"Mention your webdriver location") 
            driver.implicitly_wait(1) 
            driver.maximize_window()
            respond("Opening in youtube") 
            indx = text.split().index('youtube') 
            query = text.split()[indx + 1:] 
            driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))              
                
        elif "open my current project" in text: 
            respond("Right away sir") 
            os.startfile("C:/Users/pc/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        elif "launch Discord" in text: 
            respond("Opening Discord") 
            os.startfile("C:/Users/pc/AppData/Local/Discord/app-1.0.9001/Discord.exe")
        
        else:
           respond("Terribly sorry sir, could you repeat that?")