class Node(object):
    def __init__(self, ):
        self.children = dict()
        self.is_leaf = False


class Bor(object):
    def __init__(self):
        self.head = Node()
        with open('zdb-win.txt', 'r', encoding='cp1251') as f:
            for line in f:
                word = line.strip().lower()
                self._add_to_bor(word)

    def _add_to_bor(self, word):
        current_node = self.head
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]
        current_node.is_leaf = True

    def is_leaf(self, path):
        current_node = self.head
        for ch in path:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False
        return current_node.is_leaf

    def has_path(self, path):
        current_node = self.head
        for ch in path:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False
        return True


if __name__ == '__main__':
    print('hello')
    bor = Bor()
    words = ['фураж', 'фуражк', 'фуражка', 'фуражкат']
    for w in words:
        print(w, bor.has_path(list(w)), bor.is_leaf(list(w)))

