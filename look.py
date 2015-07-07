# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *
import search, founder


class WordTable:
    pointer = {}
    table = None
    canG = [[], [], [], [], []]
    canV = [[], [], [], [], []]
    canD = [[], [], [], [], []]

    def shower(self, event):
        event.widget.config(text=self.pointer[event.widget.winfo_id()])

    def __init__(self):
        frameR = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        frameL = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        bt_show = Button(frameL)
        bt_show.bind('<Button-1>', self.shower)
        bt_show.grid(row=1, column=1)
        label = Label(frameL, text='chose\nthe word', font='Arial 14')
        label.bind('<Button-1>', self.shower)
        label.grid(row=2, column=1)
        frameR.grid(row=1, column=2)
        frameL.grid(row=1, column=1)
        for i in range(5):
            for j in range(5):
                self.canV[i].append(None)
                self.canG[i].append(None)
                self.canD[i].append(None)

        self.table = search.getTable()
        for i in range(5):
            for j in range(5):
                label = Button(frameR, text=self.table[i][j].upper(), font='Arial 45', bg='white', height=2, width=2)
                label.grid(row=i * 2, column=(j * 2))
                self.pointer[label.winfo_id()] = [i, j]
                label.bind('<Button-1>', self.shower)
                self.canD[i][j] = Canvas(frameR, width=15, height=15, bg='blue')
                self.canD[i][j].grid(row=2 * i + 1, column=2 * j + 1)
                self.canG[i][j] = Canvas(frameR, width=15, height=82, bg='green')
                self.canG[i][j].grid(row=2 * i, column=2 * j + 1)
                self.canV[i][j] = Canvas(frameR, width=68, height=15, bg='red')
                self.canV[i][j].grid(row=2 * i + 1, column=2 * j)

    root = Tk()


wt = WordTable()
wt.root.mainloop()
