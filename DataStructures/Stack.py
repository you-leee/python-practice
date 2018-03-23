class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class Stack:
    def __init__(self):
        self.head = None
        self.__size = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.__size += 1

    def pop(self):
        if self.head is None:
            return None

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.__size -= 1

        return popped_node.val

    def __len__(self):
        return self.__size

    def __str__(self):
        return self.__str(self.head)

    def __str(self, node):
        if node.next is None:
            return str(node)
        return self.__str(node.next) + '-' + str(node)

    def rev_iter(self):
        return self.__rev_iter(self.head)

    def __rev_iter(self, node):
        if node.next is None:
            yield node
            return

        yield from self.__rev_iter(node.next)
        yield node
