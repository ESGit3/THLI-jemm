import pymongo
import tkinter as tkt
import time

#gui
top = tkt.tk()
window.title("Procrastination")
window.geometry('1250x350')

qe = Button(Window, text = "Stop", command = clicked)

combo = Combobox(window)
combo['Values'] = ("10 min": 10, "20 min": 20, "30 min": 30, "40 min": 40, "50 min": 50, "60 min": 60)
combo.grid (column = 0, row = 0)

top.mainloop()

def clicked():
    qe.configure(text = "Would you like to quit?\n If you quit now your points will not be awarded")