# -*- coding: utf-8-*-
__author__ = 'mzmey'

class MyHash:

    table = {}

    def init(self):
        if self.table.get('р') is None:
            print(self.table)
        f = open('zdb-win.txt', 'rt', encoding='cp1251')

        for line in f:
            # delete ' ' from start
            for l in range(line.__len__()):
                if line[0] == ' ':
                    line = line[1:line.__len__()]
            # delete ' ' from end
            if line[line.__len__() - 1] == '\n':
                line = line[0:line.__len__() - 1]
            # replacing ee letters
            new_line = ''
            for cur in range(line.__len__()):
                if line[cur] == 'ё':
                    new_line += 'е'
                else:
                    new_line += line[cur]
            # inserting
            if self.table.get(new_line[0]) is None:
                self.table[new_line[0]] = []
            self.table[new_line[0]].append(line)

        f.close()
        
    def has_word(self, word):
        if self.table.get(word[0]) is None:
            return False
        elif self.table[word[0]].__contains__(word):
            return True
        else:
            return False
