import unittest
from Search.BinarySearch import binary_search

class BinarySearchTest(unittest.TestCase):
    def testEmpty(self):
        arr = []
        elem = 1

        self.assertEqual(binary_search(arr, elem), -1)

    def testMiddle(self):
        arr = [1,2,3,4,5]
        elem = 3

        index = binary_search(arr, elem)

        self.assertEqual(index, 2)

    def testNotInList(self):
        arr = [1, 2, 3, 4, 5]
        elem = 6

        index = binary_search(arr, elem)

        self.assertEqual(index, -1)

    def testLowest(self):
        arr = [1, 2, 3, 4, 5]
        elem = 1

        index = binary_search(arr, elem)

        self.assertEqual(index, 0)

    def testHihgest(self):
        arr = [1, 2, 3, 4, 5]
        elem = 5

        index = binary_search(arr, elem)

        self.assertEqual(index, 4)