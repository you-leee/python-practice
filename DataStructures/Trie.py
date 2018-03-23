from builtins import ord


class Node:
    def __init__(self):
        self.children = [None]*26 # alphabet size
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def __char2idx(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        current = self.root

        for l in range(len(key)):
            index = self.__char2idx(key[l])
            if current.children[index] is None:
                current.children[index] = Node()

            current = current.children[index]

        current.is_leaf = True

    def search(self, key):
        return self.__search(key, self.root)

    def __search(self, key, current):
        if len(key) == 0:
            return current.is_leaf

        idx = self.__char2idx(key[0])
        if current.children[idx] is None:
            return False

        return self.__search(key[1:], current.children[idx])


if __name__ == '__main__':

    tr = Trie()
    tr.insert("the")
    tr.insert("their")
    tr.insert("alma")
    tr.insert("almost")

    print(tr.search("the"))
    print(tr.search("thei"))
    print(tr.search("almas"))
    print(tr.search("e"))