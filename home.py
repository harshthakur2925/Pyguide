from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter.scrolledtext as scrolledtext
from PIL import ImageTk, Image
import sqlite3
from random import randint
from bs4 import BeautifulSoup
import requests
import socket
import datetime
import webbrowser
import pyttsx3
import time
import wikipedia
import subprocess
import googlesearch
import os,sys

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('welcome to pyhelp search engine')

window = Tk()
window.title("PyGuide Search Engine")
#window.resizable(0,0)

image =Image.open('D:\pyhelp\images\pyg3.jpeg')
image =ImageTk.PhotoImage(image)
panel =Label(window,image=image)
panel.pack()

SEARCH =StringVar()
optionvar = StringVar()


def show():
    x=optionvar.get()
    if x== 'Day':
        a = datetime.date.today()
        a = str(a)
        speak(a)
        day = datetime.date.today().strftime((r'%A'))
        speak(day)
    elif x== 'Time':
        t=datetime.datetime.now().strftime(r'%H:%M:%S:')
        t= "sir current time is " + str(t)
        speak(t)
    elif x =='Calculator':
        import calcultor

    elif x== 'Calendar':
        import calndar
    elif x== 'Translator':
        try:
            socket.create_connection(('google.com',80))
            import translator
        except:
            offline()




def offline():
    time.sleep(1)
    speak("No internet")
    subprocess.call("D:\pyhelp\dino.exe")


optionvar.set("---widgets---")

option = OptionMenu(window,optionvar,'---widgets---','Time','Day',"Calculator","Calendar",'Translator')
option.config(bg='pale turquoise',font=('arial',15),borderwidth=4,relief='solid',width=61)
option.place(x=134,y=8)

showbtn = Button(window,fg='black',bg="pale turquoise",borderwidth=5,relief='solid',width=22,text="Show",font=('arial',13,'bold'),command=show)
showbtn.place(x=850,y=10)



search = Entry(window,textvariable=SEARCH,font=('arial',30,),width= 32,bg='pale turquoise',borderwidth=6,relief='solid')
search.place(x=134,y=350)

try:
    socket.create_connection(('google.com',80))
    b = Button(window,text="SEARCH",width=15,fg="black",bg='pale turquoise',font=('Franklin Gothic Book',18,"bold"),relief='solid',bd=1,borderwidth=4,command=None)
    b.place(x=850,y=350)

except:
    b = Button(window, text="SEARCH", width=15, fg="black", bg='pale turquoise', font=('Franklin Gothic Book', 18, "bold"),
               relief='solid', bd=1, borderwidth=4, command=offline)
    b.place(x=850, y=350)

window.mainloop()




