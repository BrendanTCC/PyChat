#!/usr/bin/python3
import time
import os
import sys

responsesGreat = ["great","awesome","rad","super cool","amazing"]
responsesBad = ["bad","terrible","horrible","craptacular"]
responsesGood = ["good","ok","okay","tiring","average","not great"]
responsesGroovy = ["groovy","wild","freaky","trippy"]

def intro():
    print("DISCLAIMER: this program has bugs. By using this program, you agree that if this program f**ks up your computer somehow, it's your own damned fault for not heeding the warning.")
    print(" ")
    print("Brendan's weird lil Python chat program thing v0.1.8 ALPHA")
    print("(c) 2019 Brendan J. Webb")
    print("")
    time.sleep(.100)
    os.system('cls||clear')
    print("one moment...")
    time.sleep(5)
    os.system('cls||clear')

def outro():
    time.sleep(1)
    print("EOF")
    time.sleep(3)

def name(label):
    n = input(label)
    if n.lower() == "brendan":
        day("Hello, boss!\nHow's your day been, boss? ", n)
    elif n.lower() == "cat":
        sys.exit("cat rules the school! slate")
    else:
        day("Hello, " + n.title() + ", how's your day been? ", n)

def day(label, n):
    d = input(label)
    if d.lower() in responsesGreat:
        print(d.title() + "? Oh golly," , n.title() + "! That's amazing! Have a great day, " , n.title() + "!")
        time.sleep(1)
        print("EOF")
        time.sleep(3)
    elif d.lower() in responsesBad:
        print(d.title() + "? " + d.title() + "?! I wish i could help you bud, but I'm only a program.")
    elif d.lower() in responsesGood:
        print("So your day isn't amazing, " + n.title() + "? I wish I could help you with that, but I'm only a program.")
    elif d.lower() in responsesGroovy:
        print("Far out, " + n.title())
    else:
        print("Wanker.")

intro()
name("Hello, what's your name? ")
outro()
