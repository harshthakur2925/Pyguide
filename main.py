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

main = Toplevel()
main.title("PyGuide Search Engine")
#window.resizable(0,0)

image =Image.open('D:\pyhelp\images\home.jpg')
image =ImageTk.PhotoImage(image)
panel =Label(main,image=image)
panel.pack()


def search_fn():
    query = SEARCH.get()
    query=  query.lower()
    ch = query.split(':')

    if "lib" in ch[0]:
        text = scrolledtext.ScrolledText(main,height=8,width=99,bg='black',fg='white',font=('Times New Roman',13),relief='solid',borderwidth=2,state ='normal')
        text.place(x=236,y=128)
        a = ch
        def getdata(url):
            r = requests.get(url)
            return r.text
        x= a[1]
        url='https://pypi.org/project/'+x+'/#description'
        htmldata =getdata('https://pypi.org/project/'+x+'/#description')
        soup = BeautifulSoup(htmldata,"html.parser")
        lst =[]
        data =""
        try:
            for j in soup.find('span',id='pip-command'):
                data += 'PIP COMMAND:'
                data += str(j)
            data+='\n'
            for clss in soup.find_all('div',class_="project-description"):
                p = clss.find_all('p')
                for i in p:
                    data += i.get_text()
                    data+='\n'
        except:
            data = "Not Found!!!!"
        if data == "Not Found!!!!":
            def linkopen():
                pass
            def sp():
                speak(data)
            bo = Button(main,text='SPEAK',fg='black',bg='sky blue',width =8,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=sp)
            bo.place(x=1036,y=282)
            lo= Button(main,text="Not Found!!!!",fg='black',bg='sky blue',width =65,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=None)
            lo.place(x=236,y=282)
            text.insert(INSERT,data)
            text.config(state= 'disabled')
        else:
            def linkopen():
                webbrowser.open(url)
            def sp():
               speak(data)
            bo = Button(main,text='SPEAK',fg='black',bg='sky blue',width =8,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=sp)
            bo.place(x=1036,y=282)
            lo= Button(main,text="Open In Official Website",fg='black',bg='sky blue',width =65,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=linkopen)
            lo.place(x=236,y=282)
            text.insert(INSERT,data)
            text.config(state= 'disabled')
            lab= Label(main,text='''------More Related links-----''',font=('Agency Fb',28),fg='white',bg='black',width=70)
            lab.place(x=236,y=329)
            text = scrolledtext.ScrolledText(main, height=14, width=99, bg='black', font=('Times New Roman', 13),
                                             relief='solid', borderwidth=2)

            def searchgoogle():
                link = []
                for url in googlesearch.search(query, stop=20):
                    link.append(url)

                def open(links):
                    webbrowser.open(links["text"])

                for i in range(len(link)):
                    t = link[i]
                    button = Button(main, text=t, relief='flat', bg='black', fg='white')
                    button["command"] = lambda t=button: open(t)
                    text.window_create(END, window=button)
                    text.insert(END, "\n")
                text.config(state='disabled')
                text.place(x=236, y=380)
            searchgoogle()


    elif "err" in ch[0]:
        text = scrolledtext.ScrolledText(main,height=8,width=99,bg='black',fg='white',font=('Times New Roman',13),relief='solid',borderwidth=2,state ='normal')
        text.place(x=236,y=128)
        a = ch
        x= a[1]
        url= 'https://en.wikipedia.org/wiki/'+x

        lst =[]
        data =""
        try:
            data+= wikipedia.summary(x, sentences=2)
        except:
            data = "Not Found!!!!"
        if data == "Not Found!!!!":
            def linkopen():
                pass
            def sp():
                speak(data)
            bo = Button(main,text='SPEAK',fg='black',bg='sky blue',width =8,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=sp)
            bo.place(x=1036,y=282)
            lo= Button(main,text="Not Found!!!!",fg='black',bg='sky blue',width =65,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=None)
            lo.place(x=236,y=282)
            text.insert(INSERT,data)
            text.config(state= 'disabled')
        else:
            def linkopen():
                webbrowser.open(url)
            def sp():
               speak(data)
            bo = Button(main,text='SPEAK',fg='black',bg='sky blue',width =8,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=sp)
            bo.place(x=1036,y=282)
            lo= Button(main,text="Open In Official Website",fg='black',bg='sky blue',width =65,font=('arial',14,'bold'),bd=1,borderwidth=6,relief='solid',command=linkopen)
            lo.place(x=236,y=282)
            text.insert(INSERT,data)
            text.config(state= 'disabled')
            lab= Label(main,text='''------More Related links-----''',font=('Agency Fb',28),fg='white',bg='black',width=70)
            lab.place(x=236,y=329)
            text = scrolledtext.ScrolledText(main, height=14, width=99, bg='black', font=('Times New Roman', 13),
                                             relief='solid', borderwidth=2)

            def searchgoogle():
                link = []
                for url in googlesearch.search(query, stop=20):
                    link.append(url)

                def open(links):
                    webbrowser.open(links["text"])

                for i in range(len(link)):
                    t = link[i]
                    button = Button(main, text=t, relief='flat', bg='black', fg='white')
                    button["command"] = lambda t=button: open(t)
                    text.window_create(END, window=button)
                    text.insert(END, "\n")
                text.config(state='disabled')
                text.place(x=236, y=380)
            searchgoogle()

    elif "git" in ch:
        x=ch[1]
        url ='https://github.com/search?q='+x
        def linkopen():
            webbrowser.open(url)

        lo = Button(main, text="Open In Github", fg='black', bg='sky blue', width=75,
                    font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
        lo.place(x=236, y=125)
        lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white', bg='black',
                    width=70)
        lab.place(x=236, y=170)
        text = scrolledtext.ScrolledText(main, height=23, width=99, bg='black', font=('Times New Roman', 13),
                                         relief='solid', borderwidth=2)

        def searchgoogle():
            link = []
            for url in googlesearch.search(query, stop=20):
                link.append(url)

            def open(links):
                webbrowser.open(links["text"])

            for i in range(len(link)):
                t = link[i]
                button = Button(main, text=t, relief='flat', bg='black', fg='white')
                button["command"] = lambda t=button: open(t)
                text.window_create(END, window=button)
                text.insert(END, "\n")
            text.config(state='disabled')
            text.place(x=236, y=210)

        searchgoogle()

    elif "stk" in ch:
        x=ch[1]
        url ='https://stackoverflow.com/nocaptcha?s='+x
        def linkopen():
            webbrowser.open(url)

        lo = Button(main, text="Open In StackOverFlow", fg='black', bg='sky blue', width=75,
                    font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
        lo.place(x=236, y=125)
        lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white', bg='black',
                    width=70)
        lab.place(x=236, y=170)
        text = scrolledtext.ScrolledText(main, height=23, width=99, bg='black', font=('Times New Roman', 13),
                                         relief='solid', borderwidth=2)

        def searchgoogle():
            link = []
            for url in googlesearch.search(query, stop=20):
                link.append(url)

            def open(links):
                webbrowser.open(links["text"])

            for i in range(len(link)):
                t = link[i]
                button = Button(main, text=t, relief='flat', bg='black', fg='white')
                button["command"] = lambda t=button: open(t)
                text.window_create(END, window=button)
                text.insert(END, "\n")
            text.config(state='disabled')
            text.place(x=236, y=210)

        searchgoogle()

    elif 'http' in query or 'www.' in query:
        webbrowser.open(query)
    else:
        text = scrolledtext.ScrolledText(main,height=27,width=99,bg='black',font=('Times New Roman',13),relief='solid',borderwidth=2)
        def searchgoogle():
            link =[]
            for url in googlesearch.search(query,stop=20):
                link.append(url)
            def open(links):
                webbrowser.open(links["text"])
            for i in range(len(link)):
                t = link[i]
                button = Button(main,text=t,relief='flat',bg='black',fg='white')
                button["command"]= lambda t =button:open(t)
                text.window_create(END,window=button)
                text.insert(END,"\n")
            text.config(state= 'disabled')
            text.place(x=236,y=128)
        searchgoogle()


SEARCH= StringVar()

labtxt = Label(main,text = '''Option to customize your 
search for easy handling-:''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt.place(x=7,y=120)
labtxt2 = Label(main,text= '''• Lib:''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt2.place(x=7,y=177)
labtxt3 = Label(main,text= '''<Your Query>''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt3.place(x=67,y=180)
labtxt4 = Label(main,text= '''   To Search For Any Library''',font =('Agency fb',15),bg ='white',fg ='black')
labtxt4.place(x=7,y=210)
labtxt5 = Label(main,text= '''• Err:''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt5.place(x=7,y=237)
labtxt6 = Label(main,text= '''<Your Query>''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt6.place(x=77,y=240)
labtxt7 = Label(main,text= '''  To Search For Any Error''',font =('Agency fb',15),bg ='white',fg ='black')
labtxt7.place(x=7,y=270)
labtxt8 = Label(main,text= '''• Git:''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt8.place(x=7,y=298)
labtxt9 = Label(main,text= '''<Your Query>''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt9.place(x=60,y=300)
labtxt10 = Label(main,text= '''  To Search On Github''',font =('Agency fb',15),bg ='white',fg ='black')
labtxt10.place(x=7,y=330)
labtxt11 = Label(main,text= '''• Stk''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt11.place(x=7,y=356)
labtxt12 = Label(main,text= '''<Your Query>''',font =('Agency fb',18),bg ='white',fg ='black')
labtxt12.place(x=60,y=358)
labtxt13 = Label(main,text= ''' To Search On StackOverFlow''',font =('Agency fb',15),bg ='white',fg ='black')
labtxt13.place(x=7,y=385)

labtxt14 = Label(main,text= '''   ----Random Python Facts----''',font =('Agency fb',15,'bold'),bg ='white',fg ='black')
labtxt14.place(x=7,y=430)

a = open('D:\\pyhelp\\randinfo.txt','r')
s = a.read()
s = s.split('•')
index = randint(0,len(s)-1)
text = s[index]
txt = scrolledtext.ScrolledText(main,font=('Times New Roman',13),height=3,width=22,borderwidth=4,relief="solid")
txt.place(x=6,y=460)
txt.insert(INSERT,text)
txt.config(state='disabled')
a.close

b1 =Button(main,text='HISTORY',width=18,font=('Arial',15,'bold'),fg='black',bg='pale turquoise',relief='solid',command =None)
b1.place(x=6,y=527)
b2 =Button(main,text='ABOUT',width=18,font=('Arial',15,'bold'),fg='black',bg='pale turquoise',relief='solid',command =None)
b2.place(x=6,y=568)
b3 =Button(main,text='EXIT',width=18,font=('Arial',15,'bold'),fg='black',bg='pale turquoise',relief='solid',command =None)
b3.place(x=6,y=609)

b4=Button(main,text='↶',font=('Arial',17,),fg='black',bg='white',bd=1,borderwidth=3,relief='solid',command =None)
b4.place(x=245,y=35)

search = Entry(main,textvariable=SEARCH,font=('arial',24,),width= 34,bg='pale turquoise',borderwidth=5,relief='solid')
search.place(x=275,y=35)

try:
    socket.create_connection(('google.com',80))
    b = Button(main,text="SEARCH",width=15,fg="pale turquoise",bg='black',font=('Franklin Gothic Book',15,"bold"),relief='solid',bd=1,borderwidth=4,command=search_fn)
    b.place(x=899,y=35)

except:
    b = Button(main, text="SEARCH", width=15, fg="pale turquoise", bg='black', font=('Franklin Gothic Book', 15, "bold"),
               relief='solid', bd=1, borderwidth=4, command=None)
    b.place(x=899, y=35)

b5=Button(main,text='↺',font=('Arial',17,),fg='black',bg='white',bd=1,borderwidth=3,relief='solid',command =None)
b5.place(x=1078,y=35)



main.mainloop()