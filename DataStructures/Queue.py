from DataStructures.Stack import Stack


class Queue:
    def __init__(self):
        self.add_stack = Stack()
        self.rem_stack = Stack()

    def push(self, val):
        self.add_stack.push(val)

    def pop(self):
        if len(self.rem_stack) > 0:
            return self.rem_stack.pop()

        if len(self.add_stack) < 1:
            return None

        for i in range(len(self.add_stack) - 1):
            self.rem_stack.push(self.add_stack.pop())

        return self.add_stack.pop()

    def is_empty(self):
        return (len(self.add_stack) + len(self.rem_stack)) == 0

    def __iter__(self):
        if len(self.rem_stack) > 0:
            node = self.rem_stack.head
            while node is not None:
                yield node
                node = node.next

        if len(self.add_stack) > 0:
            for node in self.add_stack.rev_iter():
                yield node


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.pop()

    for qe in q:
        print(qe)

    q.push(5)
    for qe in q:
        print(qe)

