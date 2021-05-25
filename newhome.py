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


def mains():
    def showdatabase():
        global conn, cursor
        conn = sqlite3.connect('D:\pyhelp/HISTORY.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `history` (s_no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Type TEXT, Date TEXT, Query Text)")

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    main = Toplevel()
    main.title("PyGuide Search Engine")
    # window.resizable(0,0)

    image = Image.open('D:\pyhelp\images\pyfinal.jpg')
    image = ImageTk.PhotoImage(image)
    panel = Label(main, image=image)
    panel.pack()


    def Exit():
        result = tkMessageBox.askquestion(
            'PyHelp Search Engine', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            window.destroy()
            exit()

        else:
            tkMessageBox.showinfo(
                'Return', 'You will now return to the application screen')

    def About():
        root2 = Toplevel()
        root2.title('PyHelp Search Engine')
        root2.resizable(0, 0)
        img = Image.open(r'D:\\pyhelp\\images\\about.jpg')
        img = ImageTk.PhotoImage(img)
        panel = Label(root2, image=img)
        panel.pack(side="top", fill="both", expand="yes")
        root2.mainloop()

    def refresh():
        main.destroy()
        mains()

    def Back():
        main.withdraw()
        window.state('normal')

    def history():
        val = SEARCH.get()
        val.lower()
        lt = ['lib', 'err', 'git', 'stk']
        v = val.split(':')
        if v[0] not in lt:
            v1 = None
        else:
            v1 = v[0]
        try:
            v2 = v[1]
        except:
            v2 = v[0]
        v3 = str(datetime.date.today())

        showdatabase()
        cursor.execute("INSERT INTO 'history' (Type,Date,Query) Values (?,?,?)", (v1, v3, v2))
        conn.commit()
        cursor.close()
        conn.close()

    def search_fn():
        history()
        speak('Processing. Please Wait')
        query = SEARCH.get()
        query = query.lower()
        ch = query.split(':')

        if "lib" in ch[0]:
            text = scrolledtext.ScrolledText(main, height=8, width=100, bg='black', fg='white',
                                             font=('Times New Roman', 13), relief='solid', borderwidth=2,
                                             state='normal')
            text.place(x=345, y=226)
            a = ch

            def getdata(url):
                r = requests.get(url)
                return r.text

            x = a[1]
            url = 'https://pypi.org/project/' + x + '/#description'
            htmldata = getdata('https://pypi.org/project/' + x + '/#description')
            soup = BeautifulSoup(htmldata, "html.parser")
            lst = []
            data = ""
            try:
                for j in soup.find('span', id='pip-command'):
                    data += 'PIP COMMAND:'
                    data += str(j)
                data += '\n'
                for clss in soup.find_all('div', class_="project-description"):
                    p = clss.find_all('p')
                    for i in p:
                        data += i.get_text()
                        data += '\n'
            except:
                data = "Not Found!!!!"
            if data == "Not Found!!!!":
                def linkopen():
                    pass

                def sp():
                    speak(data)

                bo = Button(main, text='SPEAK', fg='black', bg='lavender', width=10, font=('arial', 14, 'bold'), bd=1,
                            borderwidth=6, relief='solid', command=sp)
                bo.place(x=1145, y=382)
                lo = Button(main, text="Not Found!!!!", fg='black', bg='lavender', width=67, font=('arial', 14, 'bold'),
                            bd=1, borderwidth=6, relief='solid', command=None)
                lo.place(x=345, y=382)
                text.insert(INSERT, data)
                text.config(state='disabled')
            else:
                def linkopen():
                    webbrowser.open(url)

                def sp():
                    speak(data)

                bo = Button(main, text='SPEAK', fg='black', bg='lavender', width=10, font=('arial', 14, 'bold'), bd=1,
                            borderwidth=6, relief='solid', command=sp)
                bo.place(x=1145, y=382)
                lo = Button(main, text="Open In Official Website", fg='black', bg='lavender', width=67,
                            font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
                lo.place(x=345, y=382)
                text.insert(INSERT, data)
                text.config(state='disabled')
                lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white',
                            bg='black', width=70)
                lab.place(x=345, y=429)
                text = scrolledtext.ScrolledText(main, height=10, width=100, bg='black', font=('Times New Roman', 13),
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
                    text.place(x=345, y=480)

                searchgoogle()


        elif "err" in ch[0]:
            text = scrolledtext.ScrolledText(main, height=8, width=100, bg='black', fg='white',
                                             font=('Times New Roman', 13), relief='solid', borderwidth=2,
                                             state='normal')
            text.place(x=345, y=226)
            a = ch
            x = a[1]
            url = 'https://en.wikipedia.org/wiki/' + x

            lst = []
            data = ""
            try:
                data += wikipedia.summary(x, sentences=2)
            except:
                data = "Not Found!!!!"
            if data == "Not Found!!!!":
                def linkopen():
                    pass

                def sp():
                    speak(data)

                bo = Button(main, text='SPEAK', fg='black', bg='lavender', width=10, font=('arial', 14, 'bold'), bd=1,
                            borderwidth=6, relief='solid', command=sp)
                bo.place(x=1145, y=382)
                lo = Button(main, text="Not Found!!!!", fg='black', bg='lavender', width=67, font=('arial', 14, 'bold'),
                            bd=1, borderwidth=6, relief='solid', command=None)
                lo.place(x=345, y=382)
                text.insert(INSERT, data)
                text.config(state='disabled')
            else:
                def linkopen():
                    webbrowser.open(url)

                def sp():
                    speak(data)

                bo = Button(main, text='SPEAK', fg='black', bg='lavender', width=10, font=('arial', 14, 'bold'), bd=1,
                            borderwidth=6, relief='solid', command=sp)
                bo.place(x=1145, y=382)
                lo = Button(main, text="Open In Official Website", fg='black', bg='lavender', width=67,
                            font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
                lo.place(x=345, y=382)
                text.insert(INSERT, data)
                text.config(state='disabled')
                lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white',
                            bg='black', width=70)
                lab.place(x=345, y=429)
                text = scrolledtext.ScrolledText(main, height=10, width=100, bg='black', font=('Times New Roman', 13),
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
                    text.place(x=345, y=480)

                searchgoogle()

        elif "git" in ch:
            x = ch[1]
            url = 'https://github.com/search?q=' + x

            def linkopen():
                webbrowser.open(url)

            lo = Button(main, text="Open In Github", fg='black', bg='lavender', width=77,
                        font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
            lo.place(x=345, y=225)
            lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white', bg='black',
                        width=72)
            lab.place(x=345, y=270)
            text = scrolledtext.ScrolledText(main, height=19, width=100, bg='black', font=('Times New Roman', 13),
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
                text.place(x=345, y=310)

            searchgoogle()

        elif "stk" in ch:
            x = ch[1]
            url = 'https://stackoverflow.com/nocaptcha?s=' + x

            def linkopen():
                webbrowser.open(url)

            lo = Button(main, text="Open In StackOverFlow", fg='black', bg='lavender', width=77,
                        font=('arial', 14, 'bold'), bd=1, borderwidth=6, relief='solid', command=linkopen)
            lo.place(x=345, y=225)
            lab = Label(main, text='''------More Related links-----''', font=('Agency Fb', 28), fg='white', bg='black',
                        width=72)
            lab.place(x=345, y=270)
            text = scrolledtext.ScrolledText(main, height=19, width=100, bg='black', font=('Times New Roman', 13),
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
                text.place(x=345, y=310)

            searchgoogle()

        elif 'http' in query or 'www.' in query:
            webbrowser.open(query)
        else:
            text = scrolledtext.ScrolledText(main, height=25, width=100, bg='black', font=('Times New Roman', 13),
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
                text.place(x=345, y=228)

            searchgoogle()



    def ShowView():
        # Customising ViewForm

        global viewform
        viewform = Toplevel()
        viewform.title("History")
        width = 550
        height = 500

        viewform.geometry("%dx%d" % (width, height,))
        viewform.resizable(0, 0)
        ViewForm()

    # =====================================================================================================

    def ViewForm():
        # Creating A View Item Window

        global tree
        TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)

        MidViewForm = Frame(viewform, width=600)
        MidViewForm.pack()

        lbl_text = Label(TopViewForm, text="History", font=('impact', 24), width=600, bg="PaleTurquoise")
        lbl_text.pack(fill=X)

        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

        tree = ttk.Treeview(MidViewForm, columns=("S.No.", "Type", "Date", "Query"), selectmode="extended", height=100,
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading('S.No.', text="S.No.", anchor=W)
        tree.heading('Type', text="Type", anchor=W)
        tree.heading('Date', text="Date", anchor=W)
        tree.heading('Query', text="Query", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=100)
        tree.column('#2', stretch=NO, minwidth=0, width=110)
        tree.column('#3', stretch=NO, minwidth=0, width=120)

        tree.pack()
        showhist()

    # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def showhist():
        showdatabase()

        cursor.execute("SELECT * FROM `history` ORDER BY s_no desc")
        fetch = cursor.fetchall()

        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor.close()
        conn.close()

    labtxt = Label(main, text='''Options to customize your search 
    for easy handling-:''', font=('Agency fb', 18, 'bold'), bg='white', fg='black')
    labtxt.place(x=20, y=230)

    labtxt2 = Label(main, text='''• Lib:''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt2.place(x=20, y=300)
    labtxt3 = Label(main, text='''<Your Query>''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt3.place(x=57, y=300)
    labtxt4 = Label(main, text='''   To Search For Any Library''', font=('Agency fb', 15), bg='white', fg='black')
    labtxt4.place(x=15, y=330)

    labtxt5 = Label(main, text='''• Err:''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt5.place(x=180, y=300)
    labtxt6 = Label(main, text='''<Your Query>''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt6.place(x=220, y=300)
    labtxt7 = Label(main, text='''  To Search For Any Error''', font=('Agency fb', 15), bg='white', fg='black')
    labtxt7.place(x=180, y=330)

    labtxt8 = Label(main, text='''• Git:''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt8.place(x=20, y=360)
    labtxt9 = Label(main, text='''<Your Query>''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt9.place(x=57, y=360)
    labtxt10 = Label(main, text='''  To Search On Github''', font=('Agency fb', 15), bg='white', fg='black')
    labtxt10.place(x=15, y=390)

    labtxt11 = Label(main, text='''• Stk''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt11.place(x=180, y=360)
    labtxt12 = Label(main, text='''<Your Query>''', font=('Agency fb', 18), bg='white', fg='black')
    labtxt12.place(x=220, y=360)
    labtxt13 = Label(main, text=''' To Search On StackOverFlow''', font=('Agency fb', 13), bg='white', fg='black')
    labtxt13.place(x=180, y=390)

    labtxt14 = Label(main, text='''----Random Python Facts----''', font=('Agency fb', 23, 'bold'), bg='white',
                     fg='black')
    labtxt14.place(x=40, y=430)

    a = open('D:\\pyhelp\\randinfo.txt', 'r')
    s = a.read()
    s = s.split('•')
    index = randint(0, len(s) - 1)
    text = s[index]
    txt = scrolledtext.ScrolledText(main, font=('arial', 10,), height=6, width=40, borderwidth=4, relief="solid")
    txt.place(x=18, y=480)
    txt.insert(INSERT, text)
    txt.config(state='disabled')
    a.close

    b1 = Button(main, text='HISTORY', width=8, font=('Arial', 12, 'bold'), fg='black', bg='lavender', relief='solid',
                command=ShowView)
    b1.place(x=20, y=610)
    b2 = Button(main, text='ABOUT', width=8, font=('Arial', 12, 'bold'), fg='black', bg='lavender', relief='solid',
                command=About)
    b2.place(x=130, y=610)
    b3 = Button(main, text='EXIT', width=8, font=('Arial', 12, 'bold'), fg='black', bg='lavender', relief='solid',
                command=Exit)
    b3.place(x=240, y=610)

    b4 = Button(main, text='↶', font=('Arial', 17,), fg='black', bg='white', bd=1, borderwidth=3, relief='solid',
                command=Back)
    b4.place(x=440, y=100)
    search = Entry(main, textvariable=SEARCH, font=('arial', 24,), width=34, bg='lavender', borderwidth=5,
                   relief='solid')
    search.place(x=470, y=100)

    try:
        socket.create_connection(('google.com', 80))
        b = Button(main, text="SEARCH", width=15, fg="white", bg='black', font=('Franklin Gothic Book', 15, "bold"),
                   relief='solid', bd=1, borderwidth=4, command=search_fn)
        b.place(x=900, y=100)

    except:
        b = Button(main, text="SEARCH", width=15, fg="white", bg='black', font=('Franklin Gothic Book', 15, "bold"),
                   relief='solid', bd=1, borderwidth=4, command=offline)
        b.place(x=1070, y=100)

    b5 = Button(main, text='↺', font=('Arial', 17,), fg='black', bg='white', bd=1, borderwidth=3, relief='solid',
                command=refresh)
    b5.place(x=1090, y=100)
    if SEARCH.get() != '':
        search_fn()

    main.mainloop()

image=Image.open("D:\pyhelp\images\py4.jpg")
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
option.config(bg='lavender',font=('arial',15),borderwidth=4,relief='solid',width=8)
option.place(x=1100,y=75)


showbtn = Button(window,fg='lavender',bg="black",borderwidth=5,relief='groove',text='🔎',width=2,font=('arial',13,'bold'),command=show)
showbtn.place(x=1065,y=77)


search = Entry(window,textvariable=SEARCH,font=('arial',30,),width= 40,bg='lavender',borderwidth=6,relief='groove')  #flat, groove, raised, ridge, solid, or sunken
search.place(x=250,y=500)

try:
    socket.create_connection(('google.com',80))
    b = Button(window,text="SEARCH 🔎",width=15,fg="lavender",bg='black',font=('Franklin Gothic Book',18,"bold"),relief='solid',bd=1,borderwidth=4,command=mains)
    b.place(x=930,y=501)

except:
    b = Button(window, text="SEARCH 🔎", width=15, fg="lavender", bg='black', font=('Franklin Gothic Book', 18, "bold"),
               relief='solid', bd=1, borderwidth=4, command=offline)
    b.place(x=930, y=501)

window.mainloop()






