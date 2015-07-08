# -*- coding: utf-8-*-

__author__ = 'mzmey'
from tkinter import *

def change(event):
    bt1.destroy()
    bt2.pack()

root = Tk()
bt1 = Button(root, text='hello')
bt1.pack()
bt1.bind('<Button-1>', change)
bt2 = Button(root, text='good bye')
root.mainloop()