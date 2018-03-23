from DataStructures.Stack import Stack


def DFS(graph, s):
    '''
    Depth-first search implementation:
    DFS is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root and explores as far as possible along each branch before backtracking.

    :param graph: the graph to be searched, nodes have to be integers
    :param s: the source node, where the search begins
    :return: ordered list of nodes of DFS traversal
    '''

    if graph.count_nodes() == 0:
        return []

    dfs = []
    visited = []
    stack = Stack()

    stack.push(s)
    visited.append(s)

    while len(stack) > 0:
        current = stack.pop()
        dfs.append(current)

        for n in graph[current]:
            if n not in visited:
                stack.push(n)
                visited.append(n)

    return dfs



