import unittest

from DataStructures.Graph import Graph
from Search.DFS import DFS

class DFSTest(unittest.TestCase):
    def testEmpty(self):
        g = Graph()

        dfs = DFS(g, 10)

        self.assertEqual(dfs, [])

    def testTree(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(1, 4)
        g.add_edge(4, 5)
        g.add_edge(2, 6)

        bfs = DFS(g, 1)

        self.assertEqual(bfs, [1, 4, 5, 2, 6, 3])

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

        bfs = DFS(g, 1)

        self.assertEqual(bfs, [1, 7, 5, 4, 2, 6, 3])
