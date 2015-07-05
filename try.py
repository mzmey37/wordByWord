# -*- coding: cp1251-*-
__author__ = 'mzmey'
import time

f = open('zdb-win.txt', 'rt', encoding='cp1251')
dict = []
for line in f:
    for l in range(line.__len__()):
        if line[0] == ' ':
            line = line[1:line.__len__()]
    if line[line.__len__() - 1] == '\n':
        line = line[0:line.__len__() - 1]
    dict.append(line)

startTime = int(round(time.time() * 1000))

for i in range(15000000):
    g = 'привет'
    if not dict.__contains__(dict[10]):
        print('a')

endTime = int(round(time.time() * 1000))

print('work time is', endTime - startTime)