#!/usr/bin/python3
import time
import os

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
    if n == "Brendan":
        day("Hello, boss!\nHow's your day been, boss? ", n)
    else:
        day("Hello, " + n + ", how's your day been? ", n)

def day(label, n):
    d = input(label)
    if d.lower() == "great":
        print(d + "? Oh golly," , n + "! That's amazing! Have a great day, " , n + "!")
        time.sleep(1)
        print("EOF")
        time.sleep(3)
    elif d.lower() == "bad":
        print(d + "? " + d + "?! I wish i could help you bud, but I'm only a program.")
    elif d.lower() == "good" or d.lower() == "tiring":
        print("So your day isn't amazing, " + n + "? I wish I could help you with that, but I'm only a program.")
    elif d.lower() == "groovy":
        print("Far out, " + n)
    else:
        print("Wanker.")

intro()
name("Hello, what's your name? ")
outro()
