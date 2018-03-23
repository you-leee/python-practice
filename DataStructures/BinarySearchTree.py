class BST:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        # Inorder traversal
        def __iter__(self):
            if self.left is not None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right is not None:
                for elem in self.right:
                    yield elem

        def __str__(self):
            return 'BST node(' + str(self.val) + ', ' + str(self.left) + ', ' + str(self.right) + ')'

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        self.root = self.__insert(val, self.root)

    def __insert(self, val, current):
        if current is None:
            current = self.Node(val)
            return current

        if current.val > val:
            current.left = self.__insert(val, current.left)

        elif current.val < val:
            current.right = self.__insert(val, current.right)

        return current

    def __iter__(self):
        if self.root is not None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return str(self.root)

if __name__ == '__main__':

    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(4)

    print(bst)

    for node in bst:
        print(node)