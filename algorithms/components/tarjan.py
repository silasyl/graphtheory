from util.graph_structures import AdjacencyList, AdjacencyMatrix

class TarjanAlgorithm:
    """
    An implementation of Tarjan's Strongly Connected Components algorithm using an adjacency list.
    Time Complexity: O(V+E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(graph)
        self.n = n
        # Used to give each node an id
        self.id = 0
        # Used to count number of SCCs found
        self.scc_count = 0
        # Nodes ids
        self.ids = [-1] * n
        # Low link values
        self.low = [-1] * n
        self.sccs = [-1] * n
        self.on_stack = [False] * n
        self.solved = False
        self.stack = []
        self.UNVISITED = -1


    def count_scc(self):
        # Returns the number of strongly connected components in the graph.
        if not self.solved:
            self.solve()
        return self.scc_count
    
    def get_scc(self):
        # Get the connected components of this graph. If two indexes
        # have the same value then they're in the same SCC.
        if not self.solved:
            self.solve()
        return self.sccs
    
    def solve(self):
        if self.solved:
            return None
        
        for i in range(self.n):
            if self.ids[i] == self.UNVISITED:
                self.dfs(i)

        self.solved = True
        
    def dfs(self, at):
        self.on_stack[at] = True
        self.low[at] = self.id
        self.ids[at] = self.id
        self.id += 1
        self.stack.append(at)

        # Visit all neighbours & min low-link on callback
        for node_to in self.graph[at]:
            to = node_to[0]
            if self.ids[to] == self.UNVISITED:
                self.dfs(to)
            if self.on_stack[to]:
                self.low[at] = min(self.low[at], self.low[to])

        # On recursive callback, if we're at the root node (start of SCC)
        # empty the seen stack until back to root.
        if self.ids[at] == self.low[at]:
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                self.sccs[node] = self.scc_count
                if node == at:
                    break
            self.scc_count += 1


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

    tarjan = TarjanAlgorithm(graph)
    print(tarjan.count_scc())
    print(tarjan.get_scc())