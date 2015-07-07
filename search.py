# -*- coding: utf-8 -*-

__author__ = 'mzmey'

def getTable():
    t = []
    f = open('example', 'rt', encoding='utf-8')
    for i in range(5):
        t.append([])
    k = 0
    for i in f:
        if i[i.__len__() - 1] == '\n':
            i = i[0:i.__len__() - 1]
        for l in i:
            t[k].append(l)
        k += 1
    return t