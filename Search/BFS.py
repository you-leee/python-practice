from DataStructures.Queue import Queue


def BFS(graph, s):
    '''
    Breadth-first search implementation:
    BFS is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root and explores the neighbor nodes first, before moving to the next level neighbours.

    :param graph: the graph to be searched, nodes have to be integers
    :param s: the source node, where the search begins
    :return: ordered list of nodes of BFS traversal
    '''

    if graph.count_nodes() == 0:
        return []

    visited = []
    bfs_trav = []

    queue = Queue()
    queue.push(s)
    visited.append(s)

    while not queue.is_empty():
        current = queue.pop()
        bfs_trav.append(current)

        print(current)
        for n in graph[current]:

            if n not in visited:
                print('node: {}'.format(n))
                queue.push(n)
                visited.append(n)

    return bfs_trav


if __name__ == "__main__":
    # Run unit tests
    import unittest

    testsuite = unittest.TestLoader().discover('test', pattern="*BFS*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)