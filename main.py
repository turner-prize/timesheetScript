import sqlite3
import datetime
import os

def CreateTable():
    #creates tables to log info if it doesn't exists. Will be run first time, or if it moves.
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("CREATE TABLE log (date datetime, project varchar(255), timeTaken varchar(255));")
    conn.commit()
    conn.close()

def run():
    if not os.path.isfile('log.db'):
        print("Creating database")
        CreateTable()
    ProjectNumbers = int(input("How many projects have you worked on today? (Include internal work like learning or MBD projects)"))

    for i in range(ProjectNumbers):
        Project = input(f"Enter Client/Project {i}: ")
        TimeLength = input("How long did you spend?")
        conn = sqlite3.connect('log.db')
        c = conn.cursor()
        c.execute("INSERT INTO log VALUES (?,?,?)", (datetime.datetime.now(),Project,TimeLength))
        conn.commit()
        conn.close()


run()


