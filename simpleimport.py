__author__ = 'JinSeok Choi'

import math

def simplePrint():
   print ("this is simplePrint function...")

def newLine():
    print()

def threeNewLines():
    newLine()
    newLine()
    newLine()

def newstring(msg):
    print (msg)

def countdown(n):
    if n == 0:
        print ("Blastoff")
    else:
        print (n)
        countdown(n-1)

def area(r):
    temp = math.pi * r**2
    return temp



