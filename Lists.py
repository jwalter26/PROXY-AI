from Driver import respond
import os

async def createList(text):
    txtArr = text.split()
    listName = txtArr[len(txtArr)]
    newList = open(listName + ".txt", "rw")

async def deleteList(list):
    os.remove(list)

async def addToList(text, list):
    txtArr = text.split()
    if txtArr[2] in list:
        respond("This item already exists in " + list)

async def removeFromList(text, list):
    return