from copy import deepcopy
from collections import Counter

from bor import Bor


class Result:
    def __init__(self):
        self.words = []
        self.paths = []


class Founder:
    around = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

    def __init__(self):
        self.bor = Bor()

    def calculate(self, letters):
        char_matrix = [[l.get() for l in each] for each in letters]
        result = Result()
        open_set = set([((i, j),) for i in range(5) for j in range(5)])
        while len(open_set) > 0:
            path = open_set.pop()
            for direction in self.around:
                next_coord = (path[-1][0] + direction[0], path[-1][1] + direction[1])
                if next_coord[0] < 0 or next_coord[0] > 4 or next_coord[1] < 0 or next_coord[1] > 4 or next_coord in path:
                    continue
                new_path = list(path) + [next_coord]
                new_char_list = [char_matrix[i][j] for i, j in new_path]
                if self.bor.has_path(new_char_list):
                    if self.bor.is_leaf(new_char_list):
                        result.paths.append(deepcopy(new_path))
                        result.words.append(''.join(new_char_list))
                    open_set.add(tuple(new_path))
        # sorting as an idiot
        for i in range(result.words.__len__()):
            for j in range(i, result.words.__len__(), 1):
                if result.words[i].__len__() < result.words[j].__len__():
                    tmp = result.words[i]
                    result.words[i] = result.words[j]
                    result.words[j] = tmp
                    tmp = result.paths[i]
                    result.paths[i] = result.paths[j]
                    result.paths[j] = tmp
        words_met = set()
        unique_result = Result()
        for w, p in zip(result.words, result.paths):
            if w not in words_met:
                words_met.add(w)
                if w == 'ром':
                    print('add', w)
                unique_result.words.append(w)
                unique_result.paths.append(p)

        print(Counter(unique_result.words).most_common(10))
        return unique_result
