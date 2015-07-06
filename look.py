# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *

time = 0

def printer(event):
    global time
    time += 1
    bt['text'] = str(time)
root = Tk()
bt = Button(root, width=30, height=10)
bt['text'] = 'btText'
bt.bind('<Button-1>', printer)
bt.pack()
root.mainloop()