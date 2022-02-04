from Driver import respond
import csv

from System import featureInProgress

async def about():
    respond("Greetings, I am PROXY. My creator, Jesse Rogalski, wrote this program to give me life and personality. You can think of me as another Siri, Alexa, or Cortana, but at least I will not feed your personal information to the government. I am completely homemade and ready to fulfill my purpose. It is nice to meet you!")

async def features():
    respond("I can accomplish tasks such as launching software, performing mathematical calculations, fetching weather data, creating reminders, playing music, and telling you about anything you would like to know.")

async def ProxyDoesNotKnow():
    respond("Terribly sorry sir, could you repeat that?")

async def motivateMe():
    featureInProgress()
    return
    respond()

async def launchBriefing():
    return