import unittest

from DataStructures.HashTable import HashTable


class HashTableTest(unittest.TestCase):
    def testCreate(self):
        ht = HashTable(10)
        self.assertEqual(ht._capacity, 10)
        self.assertEqual(ht._size, 0)

        ht = HashTable()
        self.assertEqual(ht._capacity, 1000)

    def testSetAndGet(self):
        # Basic set and get
        ht = HashTable(10)
        ht.set('a', 1)
        self.assertEqual(ht.get('a'), 1)
        self.assertEqual(ht._size, 1)

        # Check update functionality
        ht.set('a', 2)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht._size, 1)

        # Make sure we can add a 2nd element
        ht.set('b', 10)
        self.assertEqual(ht.get('b'), 10)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht._size, 2)

        # Assert ht.set returns itself (for fluent calls)
        self.assertEqual(ht.set('c', 5), ht)

        # Test fluent set functionality
        ht.set('d', 100).set('e', 200).set('f', 300)
        self.assertEqual(ht.get('d'), 100)
        self.assertEqual(ht.get('e'), 200)
        self.assertEqual(ht.get('f'), 300)

    def testBadGet(self):
        ht = HashTable(10)
        self.assertRaises(KeyError, ht.get, 'a')

    def testRemove(self):
        ht = HashTable(10)
        self.assertRaises(KeyError, ht.remove, 'a')

        ht.set('a', 1)
        removed_item = ht.remove('a')
        self.assertEqual(removed_item, 1)
        self.assertEqual(ht._size, 0)

    def testPythonDictInterface(self):
        ht = HashTable(10)

        ht['a'] = 10
        self.assertEqual(ht.get('a'), 10)

        ht['a'] = 20
        self.assertEqual(ht['a'], 20)

        self.assertIn('a', ht.keys())

        del ht['a']
        self.assertRaises(KeyError, ht.get, 'a')

if __name__ == '__main__':
    unittest.main()
