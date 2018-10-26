import sqlite3
import datetime

ProjectNumbers = int(input("How many projects have you worked on today? (Include internal work like learning or MBD projects)"))

for i in range(ProjectNumbers):
    Project = input(f"Enter Client/Project {i}: ")
    TimeLength = input("How long did you spend?")
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO log VALUES (?,?,?)", (datetime.datetime.now(),Project,TimeLength))
    conn.commit()
    conn.close()