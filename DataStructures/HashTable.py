class HashTable:
    def __init__(self, capacity=1000):
        '''
        Hash table implementation with string keys.

        Example usage:
        ht = HashTable()
        ht.set('apple', 3).set('t', 100).set('asd', 'asd').set('list', [1,2,3])

        print(ht)

        ht['apple'] = 5
        ht.remove('apple')

        :param capacity: initial capacity of hash table
        '''
        self._capacity = capacity
        self._size = 0
        self._keys = []

        # Store both keys and values
        self._data = [None] * capacity

    def _hash(self, key, size):
        return sum([ord(c) for c in key]) % size

    def get(self, key):
        if key not in self._keys:
            raise KeyError('No such key: {}'.format(key))

        idx = self._hash(key, self._capacity)
        return self._data[idx][1]

    def set(self, key, val):
        # Update value
        if key in self._keys:
            idx = self._hash(key, self._capacity)
            self._data[idx][1] = val
        # Add new element
        else:
            # Resizing before if needed (resize when it hits half capacity (for hash algorithm)
            if len(self._keys) == (self._capacity // 2):
                self._resize()

            idx = self._hash(key, self._capacity)
            self._data[idx] = [key, val]
            self._size += 1
            self._keys.append(key)

        return self

    def _add_to(self, hash_table, size, key_val):
        idx = self._hash(key_val[0], size)
        hash_table[idx] = key_val

    def _resize(self):
        self._capacity *= 2
        new_data = [None] * self._capacity
        for kv in self._data:
            if kv:
                self._add_to(new_data, self._capacity, kv)

        self._data = new_data

    def remove(self, key):
        if key not in self._keys:
            raise KeyError('No such key: {}'.format(key))

        idx = self._hash(key, self._capacity)
        removed_item = self._data[idx][1]
        self._data[idx] = None
        self._keys.remove(key)
        self._size -= 1

        return removed_item


    ### Python dict interface
    def keys(self):
        return self._keys.copy()

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'


if __name__ == "__main__":
    # Run unit tests
    import unittest

    testsuite = unittest.TestLoader().discover('test', pattern="*HashTable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)
