from util.graph_structures import AdjacencyList, AdjacencyMatrix
from collections import deque

class DepthFirstSearch:
    """
    An implementation of a recursive approach to depth first search
    Time Complexity: O(V + E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(self.graph)
        self.n = n
        self.visited = [False] * n

    
    def solve(self, at:int) -> int:
        # Perform a depth first search on the graph counting
        # the number of nodes traversed starting at some position

        # We have already visited this node
        if self.visited[at]:
            return 0
        
        # Visit this node
        self.visited[at] = True
        count = 1

        # Visit all edges adjacent to where we're at
        edges = self.graph[at]
        if edges:
            for edge in edges:
                count += self.solve(edge[0])

        return count


if __name__ == "__main__":
    graph = AdjacencyList(5)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, -2)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 2, 10)

    dfs = DepthFirstSearch(graph)
    print(dfs.solve(0))