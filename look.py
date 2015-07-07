# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *
import search


class WordTable:
    def shower(self, event):
        print('hello')

    def __init__(self):
        frameR = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        frameL = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        bt_show = Button(frameL, command=self.shower)
        bt_show.grid(row=1, column=1)
        label = Label(frameL, text='chose\nthe word', font='Arial 14')
        label.bind('<Button-1>', self.shower)
        label.grid(row=2, column=1)
        frameR.grid(row=1, column=2)
        frameL.grid(row=1, column=1)
        canG = [[], [], [], [], []]
        canV = [[], [], [], [], []]
        canD = [[], [], [], [], []]
        for i in range(5):
            for j in range(5):
                canV[i].append(None)
                canG[i].append(None)
                canD[i].append(None)

        table = search.getTable()
        for i in range(5):
            for j in range(5):
                label = Button(frameR, text=table[i][j].upper(), font='Arial 45', bg='white')
                label.grid(row=i * 2, column=(j * 2))
                canD[i][j] = Canvas(frameR, width=15, height=15, bg='blue')
                canD[i][j].grid(row=2 * i + 1, column=2 * j + 1)
                canG[i][j] = Canvas(frameR, width=15, height=82, bg='green')
                canG[i][j].grid(row=2 * i, column=2 * j + 1)
                canV[i][j] = Canvas(frameR, width=68, height=15, bg='red')
                canV[i][j].grid(row=2 * i + 1, column=2 * j)

                canV[i][j].create_polygon(68-15, 0, 68, 15, 68, 0)
    root = Tk()


wt = WordTable()
wt.root.mainloop()
