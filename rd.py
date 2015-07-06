# -*- coding: utf-8-*-
__author__ = 'mzmey'

import search, threading, hash, time

around = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]


def copy_path(path):
    copy = []
    for i in range(path.__len__()):
        copy.append([])
    for j in range(path.__len__()):
        copy[j].append(path[j][0])
        copy[j].append(path[j][1])

    return copy


copy_time = 0


def jump(list, path, arr, current):
    global copy_time
    path.append(current)
    i = current[0]
    j = current[1]
    if path.__len__() < 10:
        for cell in around:
            place = [i + cell[0], j + cell[1]]
            if not path.__contains__([place[0], place[1]]) and -1 < place[0] < 5 and -1 < place[1] < 5:
                check_path = copy_path(path)
                check_path.append(place)
                word = ''
                for letter in check_path:
                    word += arr[letter[0]][letter[1]]
                if list.has_word(word):
                    print('\nword', word, 'exists, path is ', end='')
                    for elem in check_path:
                        print(elem, end='->')
                check_path.pop()
                jump(list, check_path, arr, place)


table = hash.MyHash()
start_time = time.time()
table.init()
end_time = time.time()
print('initialising time is', 1000 * (end_time - start_time))
arr = search.getTable()
start_time = time.time()
t = []
for i in range(5):
    for j in range(5):
        print('\n===================================================================='
              '===============================\nstarts in "', arr[i][j], '"', sep='')
        t.append(threading.Thread(target=jump, args=(table, [], arr, [i, j])))
        t[t.__len__() - 1].start()
for i in range(t.__len__()):
    t[i].join()

end_time = time.time()
print('working time is', 1000 * (end_time - start_time))
print(copy_time * 1000, 'is measured time')
