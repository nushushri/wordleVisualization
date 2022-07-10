import csv
import sqlite3

crosscsv = open("wordle1.csv", 'w', newline='')
crossCon = sqlite3.connect('wordleTimes.db')
crossConCursor = crossCon.cursor()
allRows = crossConCursor.execute("SELECT * FROM times")
csvWriter = csv.writer(crosscsv, delimiter=",")
csvWriter.writerows(allRows)
crosscsv.close()
crossCon.close()
