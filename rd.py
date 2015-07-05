# -*- coding: cp1251-*-
__author__ = 'mzmey'

import search


def copyPath(path):
    copy = []

    for i in range(path.__len__()):
        copy.append([])
    for j in range(path.__len__()):
        copy[j].append(path[j][0])
        copy[j].append(path[j][1])

    return copy

def jump(list, path, arr, current):
    path.append(current)
    i = current[0]
    j = current[1]
    print('\npath = ', end='')
    for k in range(path.__len__()):
            print(path[k], '->', end='', sep='')
    if path.__len__() < 10:
        if not path.__contains__([i + 1, j + 1]):
            if i + 1 != 5 and j + 1 != 5:
                jump(list, copyPath(path), arr, [i + 1, j + 1])

        if not path.__contains__([i + 1, j]):
            if i + 1 != 5:
                jump(list, copyPath(path), arr, [i + 1, j])

        if not path.__contains__([i + 1, j - 1]):
            if i + 1 != 5 and j - 1 != -1:
                jump(list, copyPath(path), arr, [i + 1, j - 1])

        if not path.__contains__([i, j - 1]):
            if j - 1 != -1:
                jump(list, copyPath(path), arr, [i, j - 1])

        if not path.__contains__([i - 1, j - 1]):
            if i - 1 != -1 and j - 1 != -1:
                jump(list, copyPath(path), arr, [i - 1, j - 1])

        if not path.__contains__([i - 1, j]):
            if i - 1 != -1:
                jump(list, copyPath(path), arr, [i - 1, j])

        if not path.__contains__([i - 1, j + 1]):
            if i - 1 != -1 and j + 1 != 5:
                jump(list, copyPath(path), arr, [i - 1, j + 1])

        if not path.__contains__([i, j + 1]):
            if j + 1 != 5:
                jump(list, copyPath(path), arr, [i, j + 1])
        #for k in range(path.__len__()):
            #print(path[k], '->', end='', sep='')


class MyMap:
    first = ['а', '�', '�', '�', '�''�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�',
             '�', '�', '�', '�', '�', '�', '�', '�', '�', '�']
    word = []

f = open('zdb-win.txt', 'rt', encoding='cp1251')
list = []
for line in f:
    for l in range(line.__len__()):
        if line[0] == ' ':
            line = line[1:line.__len__()]
    if line[line.__len__() - 1] == '\n':
        line = line[0:line.__len__() - 1]
    list.append(line)

arr = search.getTable()
jump(list, [], arr, [0, 0])
