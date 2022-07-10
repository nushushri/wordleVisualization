import os
import json
import re
from datetime import date 
import sqlite3

# regex expression to identify a message with Wordle message
wordleRegexp = re.compile(r'Wordle [0-9]* [0-9]/6')
# dictionary mapping month numbers to names
dateMonthDict = {1:'Jan', 2:'Feb', 3:'March', 4:'April', 5: 'May',6:'June',7:'July', 8:'Aug', 9:'Sept',10:'Oct', 11:'Nov', 12:'Dec'}

# function that returns whether a message is a Wordle message or not
def isWordleTime(message):
    return(re.match(wordleRegexp, message))

# getting the number of guesses from the wordle message, where "X" counts as 7
def getGuesses(time):
    pos1 = time.find("/")
    guesses = time[pos1-1:pos1]
    if(guesses == "X"):
        guesses = 7
    return guesses

# taking date inputs and returning the month name
def convertToMonth(dateParam):
    return dateMonthDict[dateParam.month]

anoushkaDict = {} # to store my times of each day
friendDict = {} # to store my friend's times of each day
messageFileOpened = open("messages/friend1Messages.json", "r")
messageFile = json.load(messageFileOpened)

# go through each message, adding (date, wordle guess #) as a key-value pair into the correct person's dictionary
for message in messageFile["messages"]:
    if(message.get("content", None)):
        if(isWordleTime(message["content"])):
            if(message["sender_name"] == "Anoushka Shrivastava"):
                anoushkaDict[date.fromtimestamp(message["timestamp_ms"]/1000)] = getGuesses(message["content"])
            else:
                friendDict[date.fromtimestamp(message["timestamp_ms"]/1000)] = getGuesses(message["content"])

crosswordConnection = sqlite3.connect('wordleTimes.db')
crosswordCursor = crosswordConnection.cursor()
crosswordCursor.execute('''CREATE TABLE times(month text, date text, name1Guesses int, name2Guesses int)''')

# when dates exist in both dictionaries, add our times into the database table
counter = 0
for key in anoushkaDict:
    if(friendDict.get(key, None)):
        name1Guesses =  anoushkaDict[key]
        name2Guesses = friendDict[key]
        crosswordCursor.execute("INSERT INTO times(month, date, name1Guesses, name2Guesses) VALUES (?, ?, ?, ?)", (convertToMonth(key), str(key), name1Guesses, name2Guesses))
        crosswordConnection.commit()
        counter += 1

crosswordConnection.close()
messageFileOpened.close()


