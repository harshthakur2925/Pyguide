import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

top = tk.Toplevel()
ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
cal = DateEntry(top, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)
top.mainloop()
