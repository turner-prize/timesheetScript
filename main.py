import sqlite3
import datetime

ProjectNumbers = input("How many projects have you worked on today? (Include internal work like learning or MBD projects)")

if type(ProjectNumbers) != int:
    print ("need an integer lark")


for i in ProjectNumbers:
    Project = input("Enter Client/Project 1: ")
    TimeLength = input("How long did you spend?")