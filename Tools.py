from Driver import respond
import wikipedia
import clr
import wolframalpha
from datetime import datetime
from pytz import timezone
import sched
import time

from System import featureInProgress

async def research(text):
    #text = text.replace("tell me about", "")
    try:
        results = wikipedia.summary(text, sentences=3)
    except wikipedia.exceptions.PageError:
        respond("I am sorry sir, I could not find any data on that topic")
        return
    respond(results)
    print(clr.bold("Source: Wikipedia"))

async def doMath(text):
    app_id="TUY5P4-L3EU9A5523"
    client = wolframalpha.Client(app_id)
    res = client.query(text)
    answer = next(res.results).text
    respond("The answer is " + answer)

async def reminders(text):
    featureInProgress()
    return
    remindTimer = sched.scheduler(time.time,time.sleep)