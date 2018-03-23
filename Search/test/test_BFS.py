import unittest

from DataStructures.Graph import Graph
from Search.BFS import BFS


class BSFTest(unittest.TestCase):
    def testEmpty(self):
        # Empty create
        g = Graph()

        bfs = BFS(g, 5)

        self.assertEqual(bfs, [])

    def testTree(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(1, 4)
        g.add_edge(4, 5)
        g.add_edge(2, 6)

        bfs = BFS(g, 1)

        self.assertEqual(bfs, [1, 2, 4, 3, 6, 5])

    def testGraph(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(2, 6)
        g.add_edge(5, 7)
        g.add_edge(1, 7)

        bfs = BFS(g, 1)

        self.assertEqual(bfs, [1, 2, 4, 7, 3, 6, 5])
