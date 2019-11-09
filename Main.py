from idlelib import window

import pymongo
import tkinter as tkt
import time


top = tkt.tk()
window.title("Procrastination")
window.geometry('1250x350')

#logins
un = tk.Label(window, text = "Username").grid(row = 0)
tk.Entry(window).grid(row = 0, column = 1)
passw = tk.Label(window, text = "Password").grid(row = 1)
tk.Entry(window).grid(row = 1, column = 1)
tk.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)

btn1 = Button(Window, text = "Start", command = clicked)
btn2 = Button(Window, text = "Stop", command = clickQuit).pack()

combo = Combobox(window)
combo['Values'] = ("10 min": 10, "20 min": 20, "30 min": 30, "40 min": 40, "50 min": 50, "60 min": 60)
combo.grid (column = 0, row = 0)

def clickStart():
    btn1.configure(text = "")
def clickQuit():
    response = tkt.messagebox.askquestion("Would you like to quit?\n If you quit now, no points will be awarded (Y, N)")
    if response == 1:
        quit()
    else:
        tkt.Label(window, text = "You're back to progress!")


top.mainloop()
