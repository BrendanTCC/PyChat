import time
import os
print("DISCLAIMER: this program has bugs. By using this program, you agree that if this program f**ks up your computer somehow, it's your own damned fault for not heeding the warning.")
print(" ")
print("Brendan's weird lil Python chat program thing v0.1.8 ALPHA")
print("(c) 2019 Brendan J. Webb")
print("")
time.sleep(.100)
os.system("cls")    
print("one moment...")
time.sleep(5)
os.system("cls")
print("Hello, what's your name?")
n = input()
if n == "Brendan":
    print("Hello, boss!")
    print("How's your day been, boss?")
else:

    
    print("Hello, " + n + ", how's your day been?")

d = input()
if d == "great":
        print(d + "? Oh golly," , n + "! That's amazing! Have a great day, " , n + "!")
        time.sleep(1)
        print("EOF")
        time.sleep(3)
else:
    if d == "bad":
        print(d + "? " + d + "?! I wish i could help you bud, but I'm only a program.")
    else:
        if d == "good" or "Good" or "GOOD" or "tiring":
            print("So your day isn't amazing, " + n + "? I wish I could help you with that, but I'm only a program.")

    time.sleep(1)
    print("EOF")
    time.sleep(3)

