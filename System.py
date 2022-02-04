from Driver import respond
import os
import winapps
from distutils import spawn
from shutil import which
import subprocess
from re import search

async def findFiles(text):
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
        return
    else: 
        respond("I found " + str(fileCount) + " results based on your search query")
        return

async def launchApp(text):
    featureInProgress()
    return
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

async def lockPC():
    respond("Locking down")
    cmd='rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)

async def shutDown():
    respond("Shutting down")
    subprocess.call(["shutdown", "/l"])

async def killProxy():
    respond("Until we meet again")
    exit()

async def featureInProgress():
    respond("Sorry, this feature is not ready for use. Check back at a later release.")
