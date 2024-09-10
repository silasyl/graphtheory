from util.graph_structures import AdjacencyList, AdjacencyMatrix
from util.data_structures import IndexedPriorityQueue
from heapq import heappush, heappop
import math

class TopologicalSortAlgorithm:
    """
    This topological sort implementation takes an adjacency list of an acyclic graph and returns an
    array with the indexes of the nodes in a (non unique) topological order which tells you how to
    process the nodes in the graph. More precisely from wiki: A topological ordering is a linear
    ordering of its vertices such that for every directed edge uv from vertex v to vertex u, u comes
    before v in the ordering.
    Time Complexity: O(V+E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(self.graph)
        self.n = n
        self.visited = [False] * n
        self.ordering = [None] * n

    
    def dfs(self, i:int, at:int):
        # Perform a depth first search on the graph counting
        # the number of nodes traversed starting at some position
        
        # Visit this node
        self.visited[at] = True

        # Visit all edges adjacent to where we're at
        edges = self.graph[at]
        if edges:
            for edge in edges:
                if not self.visited[edge[0]]:
                    i = self.dfs(i, edge[0])

        self.ordering[i] = at
        return i-1
    

    def solve(self):
        # Finds a topological ordering of the nodes in a Directed Acyclic Graph (DAG)
        # The input to this function is an adjacency list for a graph.

        i = self.n-1

        for at in range(self.n):
            if self.visited[at]:
                continue
            i = self.dfs(i, at)

        return self.ordering
    

    def shortest_path(self, start:int, short=True):
        # A useful application of the topological sort is to find the shortest/longest path
        # between two nodes in a Directed Acyclic Graph (DAG). Given an adjacency list
        # this method finds the shortest/longest path to all nodes starting at 'start'.

        topsort = self.solve()
        dist = [math.inf] * self.n
        dist[start] = 0
        dist_aux = 1

        if short is False:
            dist_aux = -1

        for i in range(self.n):
            node_index = topsort[i]
            if dist[node_index] != math.inf:
                edges = self.graph[node_index]
                if edges:
                    for node_to, edge_cost in edges:
                        new_dist = dist[node_index] + dist_aux*edge_cost
                        if new_dist < dist[node_to]:
                            dist[node_to] = new_dist
        
        if short is False:
            for i in range(self.n):
                if dist[i] != math.inf:
                    dist[i] *= -1

        return dist


if __name__ == "__main__":
    graph = AdjacencyList(7)
    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 2)
    graph.add_edge(0, 5, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 2, 6)
    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 10)
    graph.add_edge(3, 4, 5)
    graph.add_edge(5, 4, 7)

    topsort = TopologicalSortAlgorithm(graph)
    print(topsort.solve())