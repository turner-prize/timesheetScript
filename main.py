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

def GetProjects():
    #fetches unique list of projects to choose from, and sorts into alphabeticl order
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("Select distinct project from log")
    MyProjects = [i[0] for i in c.fetchall()]
    MyProjects.sort()
    conn.commit()
    conn.close()
    return MyProjects

def InsertProjects(sqlDate,sqlProject,sqlTimeLength):
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("INSERT INTO log VALUES (?,?,?)", (sqlDate,sqlProject,sqlTimeLength))
    conn.commit()
    conn.close()

def run():
    if not os.path.isfile('log.db'):
        CreateTable()
    ProjectNumbers = int(input("""How many projects have you worked on today?\n
                                Include internal work like learning or MBD projects) """))

    for i in range(ProjectNumbers):
        projectList = GetProjects()

        print("Choose from previous projects, or enter new project \n")

        for idNo,project in enumerate(projectList):
            print (f"{idNo}: {project}")

        xProject = input(f"\nEnter number or new project: ")
        
        try: 
            xProject = int(xProject)
            xProject = projectList[xProject]
        except:
            pass

        TimeLength = input("How long did you spend? ")
        if not i == (ProjectNumbers -1):
            print("\n---Next Project---\n")
        
        InsertProjects(datetime.datetime.now(),xProject.strip(),TimeLength)

if __name__ == "__main__":
    run()