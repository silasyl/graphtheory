from util.graph_structures import AdjacencyList, AdjacencyMatrix

class ArticulationDetectionAlgorithm:
    """
    Finds all the articulation points on an undirected graph.
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
        self.is_articulation_point = [False] * n
        self.solved = False
        self.root_node_outcoming_edge_count = 0


    def solve(self):
        # Returns the indexes for all articulation points in the graph even if the
        # graph is not fully connected.

        if self.solved:
            return self.is_articulation_point

        # Finds all articulation points in the graph across various connected components.
        for i in range(self.n):
            if self.visited[i]:
                continue
            self.root_node_outcoming_edge_count = 0
            self.dfs(i, i, -1)
            self.is_articulation_point[i] = (self.root_node_outcoming_edge_count > 1)

        self.solved = True
        return self.is_articulation_point
        
    
    def dfs(self, root, at, parent):
        # Perform Depth First Search to find articulation points.

        if parent == root:
            self.root_node_outcoming_edge_count += 1

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
                self.dfs(root, to, at)
                self.low[at] = min(self.low[at], self.low[to])
                if self.ids[at] <= self.low[to]:
                    self.is_articulation_point[at] = True


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

    bridges = ArticulationDetectionAlgorithm(graph)
    print(bridges.solve())