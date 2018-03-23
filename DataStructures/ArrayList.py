class ArrayList:
    def __init__(self, *args):
        self.capacity = max(10, len(args))
        self.elems = [None] * self.capacity
        self.size = len(args)

        for i in range(len(args)):
            self.elems[i] = args[i]

    def append(self, val):
        if self.size == self.capacity:
            self._increase_capacity()

        self.elems[self.size] = val
        self.size += 1

    def _increase_capacity(self, n=None):
        if n:
            self.capacity = n*2
        else:
            self.capacity *= 2
        new_elems = [None] * self.capacity
        new_elems[0:self.size] = self.elems
        self.elems = new_elems

    def pop(self):
        if self.size == 0:
            raise IndexError('Pop from empty list')

        popped = self.elems[self.size - 1]
        self.elems[self.size - 1] = None
        self.size -= 1

        return popped

    def _check_index(self, n):
        if n > self.size - 1 or n < 0:
            raise IndexError('Index out of range')

    def get(self, n):
        self._check_index(n)

        return self.elems[n]

    def set(self, n, val):
        if n < 0:
            raise IndexError('No negative indices')

        if n >= self.capacity:
            self._increase_capacity(n)

        if n >= self.size:
            self.size += 1

        self.elems[n] = val

        return self

    def remove(self, n):
        self._check_index(n)

        removed_item = self.elems[n]
        self.elems = self.elems[0:n] + self.elems[n+1:]
        self.size -= 1

        return removed_item

    ### Python list interface
    def __str__(self):
        return str(self.elems[0:self.size])

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)


if __name__ == "__main__":
    # Run unit tests
    import unittest

    testsuite = unittest.TestLoader().discover('test', pattern="*ArrayList*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
