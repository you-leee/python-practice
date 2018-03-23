import unittest
from DataStructures.BinaryHeap import BinaryHeap


class BinaryHeapTest(unittest.TestCase):
    def testCreate(self):
        bh = BinaryHeap()
        self.assertEqual(bh.elems, [])

    def testPush(self):
        bh = BinaryHeap()

        bh.hpush(10)
        self.assertEqual(bh.elems[0], 10)

        # push larger
        bh.hpush(20)
        self.assertEqual(len(bh.elems), 2)
        self.assertEqual(bh.elems[0], 20)

        # push smaller
        bh.hpush(5)
        self.assertEqual(len(bh.elems), 3)
        self.assertEqual(bh.elems[2], 5)

        # push inbetween
        bh.hpush(12)
        self.assertEqual(bh.elems[0], 20)
        self.assertEqual(bh.elems[1], 12)

    def testPop(self):
        # pop from empty
        bh = BinaryHeap()

        self.assertRaises(IndexError, bh.hpop)

        # pop largest element
        bh.hpush(10)
        bh.hpush(20)

        self.assertEqual(bh.hpop(), 20)

        # pop remaining element
        self.assertEqual(bh.hpop(), 10)

    def testLargestChildIdx(self):
        bh = BinaryHeap()
        bh.hpush(10)
        bh.hpush(15)
        bh.hpush(11)
        bh.hpush(20)
        bh.hpush(21)

        self.assertEqual(bh.largest_child_idx(0), 1)
        self.assertEqual(bh.largest_child_idx(1), 4)

    def testStr(self):
        bh = BinaryHeap()
        bh.hpush(10)
        bh.hpush(15)
        bh.hpush(11)
        bh.hpush(20)
        bh.hpush(21)

        self.assertEqual(str(bh), '[21, 20, 11, 10, 15]')
