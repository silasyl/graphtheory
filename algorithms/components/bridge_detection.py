from util.graph_structures import AdjacencyList, AdjacencyMatrix

class BridgeDetectionAlgorithm:
    """
    Finds all the bridges on an undirected graph.
    Time Complexity: O(V+E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(graph)
        self.n = n
        self.id = 0
        # Nodes ids
        self.ids = [-1] * n
        # Low link values
        self.low = [-1] * n
        self.visited = [False] * n
        self.bridges = []
        self.solved = False


    def solve(self):
        # Returns a list of pairs of nodes indicating which nodes form bridges.
        # The returned list is always of even length and indexes (2*i, 2*i+1) form a
        # pair. For example, nodes at indexes (0, 1) are a pair, (2, 3) are another
        # pair, etc...

        if self.solved:
            return self.bridges

        # Finds all bridges in the graph across various connected components.
        for i in range(self.n):
            if self.visited[i]:
                continue
            self.dfs(i, -1)

        self.solved = True
        return self.bridges
        
    
    def dfs(self, at, parent):
        # Perform Depth First Search to find bridges.
        # # at = current node, parent = previous node. The
        # bridges list is always of even length and indexes
        # (2*i, 2*i+1) form a bridge. For example, nodes at
        # indexes (0, 1) are a bridge, (2, 3) is another etc...

        self.visited[at] = True
        self.low[at] = self.id
        self.ids[at] = self.id
        self.id += 1

        # For each edge from node 'at' to node 'to'
        for node_to in self.graph[at]:
            to = node_to[0]
            if to == parent:
                continue
            if self.visited[to]:
                self.low[at] = min(self.low[at], self.ids[to])
            else:
                self.dfs(to, at)
                self.low[at] = min(self.low[at], self.low[to])
                if self.ids[at] < self.low[to]:
                    self.bridges.append((at, to))


if __name__ == "__main__":
    graph = AdjacencyList(9)
    graph.add_edge(0, 1, directed=False)
    graph.add_edge(0, 2, directed=False)
    graph.add_edge(1, 2, directed=False)
    graph.add_edge(2, 3, directed=False)
    graph.add_edge(2, 5, directed=False)
    graph.add_edge(3, 4, directed=False)
    graph.add_edge(5, 6, directed=False)
    graph.add_edge(5, 8, directed=False)
    graph.add_edge(6, 7, directed=False)
    graph.add_edge(7, 8, directed=False)

    bridges = BridgeDetectionAlgorithm(graph)
    print(bridges.solve())