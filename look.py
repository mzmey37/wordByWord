# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *
import search, founder, tkinter.ttk as ttk, threading

class WordTable:
    pointer = {}
    height = None
    width = None
    btShow = None
    progr = None
    wordList = None
    pathList = []
    letter = [[], [], [], [], []]
    table = None
    idInNumber = {}
    canG = [[], [], [], [], []]
    canV = [[], [], [], [], []]
    canD = [[], [], [], [], []]

    def drawer(self, path):
        print(path)
        for i in range(5):
            for j in range(5):
                self.letter[i][j].configure(bg='white')
                if self.canD[i][j] is not None:
                    for item in self.canD[i][j].find_all():
                        self.canD[i][j].delete(item)

                if self.canV[i][j] is not None:
                    for item in self.canV[i][j].find_all():
                        self.canV[i][j].delete(item)

                if self.canG[i][j] is not None:
                    for item in self.canG[i][j].find_all():
                        self.canG[i][j].delete(item)

        self.letter[path[0][0]][path[0][1]].configure(bg='orange')
        for i in range(path.__len__() - 1):
            self.letter[path[i + 1][0]][path[i + 1][1]].configure(bg='orange')
            # diagonal
            if path[i][0] != path[i + 1][0] and path[i][1] != path[i + 1][1]:
                if path[i][0] < path[i + 1][0]:
                    if path[i][1] < path[i + 1][1]:
                        i0 = path[i][0]
                        i1 = path[i][1]
                        self.canD[i0][i1].create_polygon(0, 0, 0, 10, 10, 10, 10, 0, fill='orange')
                        self.canG[i0][i1].create_polygon(self.width - 10, 0, self.width, 10, self.width, 0,
                                                         fill='orange')
                        self.canG[i0][i1 + 1].create_polygon(0, 0, 0, 10, 10, 10, fill='orange')
                        self.canV[i0][i1].create_polygon(0, self.height - 10, 10, self.height, 0, self.height,
                                                         fill='orange')
                        self.canV[i0 + 1][i1].create_polygon(0, 0, 10, 10, 10, 0, fill='orange')
                        print([i0, i1])
                    else:
                        i0 = path[i][0]
                        i1 = path[i + 1][1]
                        self.canD[i0][i1].create_polygon(0, 0, 0, 10, 10, 10, 10, 0, fill='orange')
                        self.canG[i0][i1].create_polygon(self.width, 0, self.width - 10, 10, self.width, 10, fill='orange')
                        self.canG[i0][i1 + 1].create_polygon(0, 0, 10, 0, 0, 10, fill='orange')
                        self.canV[i0][i1].create_polygon(0, self.height, 10, self.height, 10, self.height - 10,
                                                         fill='orange')
                        self.canV[i0 + 1][i1].create_polygon(0, 0, 10, 0, 0, 10, fill='orange')
                        print([i0, i1])
                else:
                    if path[i][1] < path[i + 1][1]:
                        i0 = path[i + 1][0]
                        i1 = path[i][1]
                        self.canD[i0][i1].create_polygon(0, 0, 0, 10, 10, 10, 10, 0, fill='orange')
                        self.canG[i0][i1].create_polygon(self.width - 10, 10, self.width, 10, self.width, 0, fill='orange')
                        self.canG[i0][i1 + 1].create_polygon(0, 10, 10, 0, 0, 0, fill='orange')
                        self.canV[i0][i1].create_polygon(0, self.height, 10, self.height - 10, 10, self.height,
                                                         fill='orange')
                        self.canV[i0 + 1][i1].create_polygon(0, 0, 10, 0, 0, 10, fill='orange')
                        print([i0, i1])
                    else:
                        i0 = path[i + 1][0]
                        i1 = path[i + 1][1]
                        self.canD[i0][i1].create_polygon(0, 0, 0, 10, 10, 10, 10, 0, fill='orange')
                        self.canG[i0][i1].create_polygon(self.width - 10, 0, self.width, 10, self.width, 0, fill='orange')
                        self.canG[i0][i1 + 1].create_polygon(0, 0, 10, 10, 0, 10, fill='orange')
                        self.canV[i0][i1].create_polygon(0, self.height - 10, 10, self.height, 0, self.height,
                                                         fill='orange')
                        self.canV[i0 + 1][i1].create_polygon(0, 0, 10, 10, 10, 0, fill='orange')
                        print([i0, i1])
            elif path[i][0] == path[i + 1][0]:
                if path[i][1] < path[i + 1][1]:
                    self.canV[path[i][0]][path[i][1]].create_polygon(0, self.height/2 - 10, 0, self.height/2 + 10, 10,
                                                                     self.height/2 + 10, 10, self.height/2 - 10,
                                                                     fill='orange')
                else:
                    self.canV[path[i][0]][path[i + 1][1]].create_polygon(0, self.height/2 - 10, 0, self.height/2 + 10,
                                                                         10, self.height/2 + 10, 10, self.height/2 - 10,
                                                                         fill='orange')
            else:
                if path[i][0] < path[i + 1][0]:
                    self.canG[path[i][0]][path[i][1]].create_polygon(self.width/2 - 10, 0, self.width/2 + 10, 0,
                                                                     self.width/2 + 10, 10, self.width/2 - 10, 10,
                                                                     fill='orange')
                else:
                    self.canG[path[i + 1][0]][path[i + 1][1]].create_polygon(self.width/2 - 10, 0, self.width/2 + 10, 0,
                                                                             self.width/2 + 10, 10, self.width/2 - 10,
                                                                             10, fill='orange')
        self.letter[path[0][0]][path[0][1]].configure(bg='#D2691E')

    def listReader(self, event):
        id = self.wordList.curselection()[0]
        res = self.wordList.get(id, id)[0]
        print(self.pathList[self.idInNumber[id]], ', word is', res)
        self.drawer(self.pathList[self.idInNumber[id]])

    def threader(self):
        res = founder.Founder().calculate()
        k = 0
        for word in res.words:
            self.wordList.insert(END, word)
            self.idInNumber[self.wordList.size() - 1] = k
            k += 1
        for path in res.pathes:
            self.pathList.append(path)
        self.progr.destroy()
        self.wordList.pack()

    def shower(self, event):
        self.progr.pack()
        self.progr.start(7)
        threading.Thread(target=self.threader).start()

    def __init__(self):
        frameR = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        frameL = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        self.btShow = Button(frameL, text='show words')
        self.btShow.pack()
        self.btShow.bind('<Button-1>', self.shower)
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
                self.letter[i].append(Button(frameR, text=self.table[i][j].upper(), font='Arial 36', bg='white',
                                             height=1, width=2))
                self.letter[i][j].grid(row=i * 2, column=(j * 2))
                if i == j == 0:
                    self.width = self.letter[i][j].winfo_reqwidth()
                    self.height = self.letter[i][j].winfo_reqheight()
                self.pointer[label.winfo_id()] = [i, j]
                self.canD[i][j] = Canvas(frameR, width=10, height=10)
                self.canD[i][j].grid(row=2 * i + 1, column=2 * j + 1)
                self.canV[i][j] = Canvas(frameR, width=10, height=self.height)
                self.canV[i][j].grid(row=2 * i, column=2 * j + 1)
                self.canG[i][j] = Canvas(frameR, width=self.width, height=10)
                self.canG[i][j].grid(row=2 * i + 1, column=2 * j)

    root = Tk()


wt = WordTable()
wt.root.mainloop()
