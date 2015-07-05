# -*- coding: utf-8-*-
__author__ = 'mzmey'

import search
import hash
import time


def copy_path(path):
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
    if path.__len__() < 10:
        if not path.__contains__([i + 1, j + 1]) and i + 1 != 5 and j + 1 != 5:
            check_path = copy_path(path)
            check_path.append([i + 1, j + 1])
            word = ''
            for letter in check_path:
                word += arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i + 1, j + 1])

        if not path.__contains__([i + 1, j]) and i + 1 != 5:
            check_path = copy_path(path)
            check_path.append([i + 1, j])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i + 1, j])

        if not path.__contains__([i + 1, j - 1]) and i + 1 != 5 and j - 1 != -1:
            check_path = copy_path(path)
            check_path.append([i + 1, j - 1])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i + 1, j - 1])

        if not path.__contains__([i, j - 1]) and j - 1 != -1:
            check_path = copy_path(path)
            check_path.append([i, j - 1])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i, j - 1])

        if not path.__contains__([i - 1, j - 1]) and i - 1 != -1 and j - 1 != -1:
            check_path = copy_path(path)
            check_path.append([i - 1, j - 1])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i - 1, j - 1])

        if not path.__contains__([i - 1, j]) and i - 1 != -1:
            check_path = copy_path(path)
            check_path.append([i - 1, j])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i - 1, j])

        if not path.__contains__([i - 1, j + 1]) and i - 1 != -1 and j + 1 != 5:
            check_path = copy_path(path)
            check_path.append([i - 1, j + 1])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            jump(list, copy_path(path), arr, [i - 1, j + 1])

        if not path.__contains__([i, j + 1]) and j + 1 != 5:
            check_path = copy_path(path)
            check_path.append([i, j + 1])
            word = ''
            for letter in check_path:
                word = word + arr[letter[0]][letter[1]]
            if list.has_word(word):
                print('word', word, 'exists')
            jump(list, copy_path(path), arr, [i, j + 1])


table = hash.MyHash()
start_time = time.time()
table.init()
end_time = time.time()
print('initialising time is', 1000 * (end_time - start_time))
arr = search.getTable()
start_time = time.time()
jump(table, [], arr, [0, 0])
end_time = time.time()
print('working time is', 1000 * (end_time - start_time))
