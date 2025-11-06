import threading as td
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("c:/Users/muham/Eng_files/Python_prac/NeuralNine/Intermediate_Python/text.txt","r") as f:
            text = f.read()
        time.sleep(1)

def printLoop():
    for i in range(30):
        print(text)
        time.sleep(1)

t1 = td.Thread(target=readFile, daemon=True)
t2 = td.Thread(target=printLoop)

t1.start()
t2.start()
