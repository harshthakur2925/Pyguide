from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from textblob import TextBlob

root = Toplevel()
root.geometry('500x395')
root.title('Translator')
root.resizable(False, False)
root.configure(bg='gray10')
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'esperanto': 'eo',
            'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl',
            'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha',
            'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is',
            'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
            'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky',
            'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk',
            'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
            'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or',
            'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
            'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
            'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
            'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
            'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
            'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def translate():
    word = TextBlob(entry1.get('1.0', END))
    lan = word.detect_language()
    lan_todict = languages.get()
    lan_to = lan_dict[lan_todict]
    word = word.translate(from_lang=lan, to=lan_to)
    entry2.insert(INSERT, word)


def main_exit():
    rr = messagebox.askyesnocancel('Notification', 'Do you want to exit?', parent=root)
    if rr == True:
        root.destroy()


def on_enterentry1(e):
    entry1['bg'] = 'gray'


def on_leaveentry1(e):
    entry1['bg'] = 'white'


def on_enterentry2(e):
    entry2['bg'] = 'gray'


def on_leaveentry2(e):
    entry2['bg'] = 'white'


languages = StringVar()
font_box = Combobox(root, width=30, textvariable=languages, state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(36)
font_box.place(x=200, y=170)

entry1 = scrolledtext.ScrolledText(root, width=30, font=('calibri', 15, 'bold'), height=5)
entry1.place(x=150, y=35)

entry2 = scrolledtext.ScrolledText(root, width=30, font=('calibri', 15, 'bold'), height=5)
entry2.place(x=150, y=200)

label1 = Label(root, text='Enter Text:', font=('calibri', 15, 'bold'), bg='gray10', fg='white')
label1.place(x=15, y=80)

label2 = Label(root, text='Translated:', font=('calibri', 15, 'bold'), bg='gray10', fg='white')
label2.place(x=15, y=250)

btn1 = Button(root, text='Translate', command=translate, bd=5, bg='gray', activebackground='white', width=24,
              font=('calibri', 15, 'bold'))
btn1.place(x=0, y=350)

btn2 = Button(root, text='Exit', command=main_exit, bd=5, bg='gray', activebackground='white', width=23,
              font=('calibri', 15, 'bold'))
btn2.place(x=255, y=350)

entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

root.mainloop()
