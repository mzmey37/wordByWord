# -*- coding: utf-8-*-
__author__ = 'mzmey'

import hash


class Res:
    words = []
    pathes = []


class Founder:
    around = [[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]

    def copy_path(self, path):
        copy = []
        for i in range(path.__len__()):
            copy.append([])
        for j in range(path.__len__()):
            copy[j].append(path[j][0])
            copy[j].append(path[j][1])
        return copy

    def jump(self, list, path, arr, current, res):
        path.append(current)
        i = current[0]
        j = current[1]
        if path.__len__() < 9:
            for cell in self.around:
                place = [i + cell[0], j + cell[1]]
                if not path.__contains__([place[0], place[1]]) and -1 < place[0] < 5 and -1 < place[1] < 5:
                    check_path = self.copy_path(path)
                    check_path.append(place)
                    word = ''.join([arr[i1][i2] for i1, i2 in check_path])
                    if list.has_word(word):
                        res.words.append(word)
                        res.pathes.append(check_path)
                    check_path.pop()
                    self.jump(list, check_path, arr, place, res)

    def calculate(self, letters):
        table = hash.MyHash()
        arr = [[l.get() for l in each] for each in letters]
        res = Res
        for i in range(5):
            for j in range(5):
                self.jump(table, [], arr, [i, j], res)

        for i in range(res.words.__len__()):
            for j in range(i, res.words.__len__(), 1):
                if res.words[i].__len__() < res.words[j].__len__():
                    tmp = res.words[i]
                    res.words[i] = res.words[j]
                    res.words[j] = tmp
                    tmp = res.pathes[i]
                    res.pathes[i] = res.pathes[j]
                    res.pathes[j] = tmp

        return res
