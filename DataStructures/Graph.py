class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node, edge):
        # if node isn't in graph
        if not self.nodes.get(node):
            self.nodes[node] = []

        # if edge is not in the current graph
        if edge not in self.nodes:
            self.nodes[edge] = []

        self.nodes[node].append(edge)
        self.nodes[edge].append(node)

    def remove(self, node):
        if node not in self.nodes:
            return -1

        neighbours = self.nodes.pop(node)
        for n in self.nodes:
            if n in neighbours:
                self.nodes[n].remove(node)

    def count_nodes(self):
        return len(self.nodes)

    def find_shortest_path(self, start, end):
        return self.__find_shortest_path(start, end, [])

    def __find_shortest_path(self, start, end, path):
        path = path + [start]

        if start == end:
            return path
        if not self.nodes.get(start):
            return None

        shortest = None
        for node in self.nodes[start]:
            if node not in path:
                newpath = self.__find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def __str__(self):
        return str(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]

if __name__ == '__main__':

    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 4)
    print(g2)

    x = 1
    print(g2[x])
