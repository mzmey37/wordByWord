# -*- coding: utf-8-*-
__author__ = 'MZmey'
from tkinter import *
import sys
import os
import tkinter.ttk as ttk
import new_founder
import threading


class WordTable:
    pointer = {}
    height = None
    width = None
    btShow = None
    progr = None
    wordList = None
    pathList = []
    letter = [[], [], [], [], []]
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
        res = new_founder.Founder().calculate(self.letter)
        k = 0
        for word in res.words:
            self.wordList.insert(END, word)
            self.idInNumber[self.wordList.size() - 1] = k
            k += 1
        for path in res.paths:
            self.pathList.append(path)
        self.progr.destroy()
        self.wordList.pack()

    def shower(self, event):
        self.progr.pack()
        self.progr.start(1)
        threading.Thread(target=self.threader).start()

    def get_change_focus_callback(self, sv, i, j):
        def change_focus(name, index, mode, sv=sv):
            print('CALLBACK', i, j, name, index, mode, sv.get())
            if sv.get() == '':
                return
            if j < 4:
                self.letter[i][j+1].focus()
                print('trying to focus on', i, j+1)
            elif i < 4:
                self.letter[i+1][0].focus()
                print('trying to focus on', i + 1, 0)
        return change_focus

    def restart(self, event):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def __init__(self):
        self.root = Tk()
        self.frameR = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        self.frameL = Frame(self.root, height=200, width=1000, bd=20, bg='white')
        self.btShow = Button(self.frameL, text='show words')
        self.btShow.pack()
        self.btShow.bind('<Button-1>', self.shower)

        self.bt_restart = Button(self.frameL, text='restart')
        self.bt_restart.pack()
        self.bt_restart.bind('<Button-1>', self.restart)

        label = Label(self.frameL, text='chose\nthe word', font='Arial 14')
        label.pack()

        self.progr = ttk.Progressbar(self.frameL, orient='horizontal')
        self.wordList = Listbox(self.frameL, selectmode=SINGLE, height=30)
        self.wordList.bind('<Double-Button-1>', self.listReader)
        self.frameR.grid(row=1, column=2)
        self.frameL.grid(row=1, column=1)
        for i in range(5):
            for j in range(5):
                self.canV[i].append(None)
                self.canG[i].append(None)
                self.canD[i].append(None)

        for i in range(5):
            for j in range(5):
                sv = StringVar()
                sv.trace('w', self.get_change_focus_callback(sv, i, j))
                self.letter[i].append(Entry(self.frameR, textvariable=sv, font='Arial 36', bg='white', width=2,))
                self.letter[i][j].grid(row=i * 2, column=j * 2)
                if i == j == 0:
                    self.width = self.letter[i][j].winfo_reqwidth()
                    self.height = self.letter[i][j].winfo_reqheight()
                self.pointer[label.winfo_id()] = [i, j]
                self.canD[i][j] = Canvas(self.frameR, width=10, height=10)
                self.canD[i][j].grid(row=2 * i + 1, column=2 * j + 1)
                self.canV[i][j] = Canvas(self.frameR, width=10, height=self.height)
                self.canV[i][j].grid(row=2 * i, column=2 * j + 1)
                self.canG[i][j] = Canvas(self.frameR, width=self.width, height=10)
                self.canG[i][j].grid(row=2 * i + 1, column=2 * j)


if __name__ == '__main__':
    wt = WordTable()
    windowWidth = wt.root.winfo_reqwidth()
    windowHeight = wt.root.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)
    print(wt.root.winfo_screenwidth(), wt.root.winfo_screenheight())
    positionRight = int(wt.root.winfo_screenwidth() / 2 - windowWidth)
    positionDown = int(wt.root.winfo_screenheight() / 2 - windowHeight)
    wt.root.geometry("+{}+{}".format(positionRight, positionDown))
    wt.root.mainloop()
