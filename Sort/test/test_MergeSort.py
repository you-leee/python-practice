import unittest
from Sort.MergeSort import mergesort


class MergeSortTest(unittest.TestCase):
    def testEmpty(self):
        arr = []

        self.assertEqual(mergesort(arr), arr)

    def testOneElement(self):
        arr = [1]

        self.assertEqual(mergesort(arr), arr)

    def testSorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = mergesort(arr)

        self.assertEqual(sorted_arr, arr)

    def testReversed(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = mergesort(arr)

        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def testSame(self):
        arr = [1, 1, 1, 1, 1, 1]
        sorted_arr = mergesort(arr)

        self.assertEqual(sorted_arr, arr)
