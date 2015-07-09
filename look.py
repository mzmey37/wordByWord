# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *
import search, founder, tkinter.ttk as ttk, threading

class WordTable:
    pointer = {}
    progr = None
    wordList = None
    table = None
    canG = [[], [], [], [], []]
    canV = [[], [], [], [], []]
    canD = [[], [], [], [], []]

    def listReader(self, event):
        id = self.wordList.curselection()[0]
        res = self.wordList.get(id, id)[0]
        print(res)

    def threader(self):
        res = founder.Founder().calculate()
        for word in res.words:
            self.wordList.insert(END, word)
        self.progr.destroy()
        self.wordList.pack()

    def shower(self, event):
        self.progr.pack()
        self.progr.start(7)
        threading.Thread(target=self.threader).start()

    def __init__(self):
        frameR = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        frameL = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        bt_show = Button(frameL, text='show words')
        bt_show.pack()
        bt_show.bind('<Button-1>', self.shower)
        label = Label(frameL, text='chose\nthe word', font='Arial 14')
        label.pack()
        self.progr = ttk.Progressbar(frameL, orient='horizontal')
        self.wordList = Listbox(frameL, selectmode=SINGLE, height=30)
        self.wordList.bind('<Double-Button-1>', self.listReader)
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
                label = Button(frameR, text=self.table[i][j].upper(), font='Arial 45', bg='white', height=1, width=1)
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
