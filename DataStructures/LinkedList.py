class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        # adding tail would be a big improvement

    def append(self, value):
        if self.head is None:
            self.head = Node()
            self.head.value = value
            return None

        return self._append(self.head, value)

    def _append(self, current, value):
        if current.next is None:
            new_node = Node()
            new_node.value = value
            current.next = new_node

            return None

        return self._append(current.next, value)

    def pop(self):
        if self.head is None:
            return None

        return self._pop(self.head)

    def _pop(self, current):
        if current.next is None:
            current = None
            return None

        return self._pop(current.next)

    def get(self, n):
        if self.size() <= n:
            return None

        return self._get(n, self.head, 0)

    def _get(self, n, current, count):
        if count == n:
            return current.value

        return self._get(n, current.next, count + 1)

    def is_empty(self):
        return not self.head

    def size(self):
        return self._size(self.head, 0)

    def _size(self, current, count):
        if current is None:
            return count

        return self._size(current.next, count + 1)

    def __str__(self):
        s = '[' + str(self.head.value)

        current = self.head.next
        while(current != None):
            s += ',' + str(current.value)
            current = current.next

        s += ']'

        return s

if __name__ == '__main__':

    ll = LinkedList()
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print(ll.is_empty())
    print(ll)
    print(ll.size())

    print(ll.get(2))
    print(ll.get(3))