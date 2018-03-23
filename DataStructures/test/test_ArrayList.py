import unittest

from DataStructures.ArrayList import ArrayList


class ArrayListTest(unittest.TestCase):
    def testCreate(self):
        # Empty create
        al = ArrayList()
        self.assertEqual(al.size, 0)
        self.assertEqual(al.capacity, 10)

        # Create with elements
        al = ArrayList(1, 2, 3)
        self.assertEqual(al.size, 3)
        self.assertEqual(al.capacity, 10)

    def testAppend(self):
        al = ArrayList()

        # Append 1
        al.append(1)

        self.assertEqual(al.get(0), 1)
        self.assertEqual(al.size, 1)

        # Append another
        al.append(2)
        self.assertEqual(al.get(0), 1)
        self.assertEqual(al.get(1), 2)
        self.assertEqual(al.size, 2)

    def testResize(self):
        al = ArrayList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        self.assertEqual(al.size, 10)
        self.assertEqual(al.capacity, 10)

        al.append(10)
        self.assertEqual(al.size, 11)
        self.assertEqual(al.capacity, 20)

    def testPop(self):
        al = ArrayList()

        # Append and pop
        al.append(1)
        rem_item = al.pop()
        self.assertEqual(rem_item, 1)
        self.assertEqual(al.size, 0)

        # try to pop from empty
        self.assertRaises(IndexError, al.pop)

    def testGet(self):
        al = ArrayList(1, 2, 3)

        self.assertEqual(al[0], 1)
        self.assertEqual(al[2], 3)

        # try to get out of index
        self.assertRaises(IndexError, al.get, 3)
        self.assertRaises(IndexError, al.get, -1)

    def testSet(self):
        al = ArrayList(1,2,3)

        self.assertEqual(al[2], 3)

        # Normal set
        al.set(2, 100)
        self.assertEqual(al[2], 100)

        # Try to set out of capacity
        al.set(1000, 5)
        self.assertEqual(al.capacity, 2000)

    def testRemove(self):
        al = ArrayList(1, 2, 3)

        # Remove normal
        rem_item = al.remove(0)
        self.assertEqual(rem_item, 1)

        # Remove out of bound
        self.assertRaises(IndexError, al.remove, 3)
        self.assertRaises(IndexError, al.remove, -1)

    def testPythonInterface(self):
        al = ArrayList()

        al[0] = 1
        self.assertEqual(al[0], 1)

        al[0] = 10
        self.assertEqual(al[0], 10)
