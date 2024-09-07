from util.graph_structures import AdjacencyList
from util.data_structures import IndexedPriorityQueue
from heapq import heappush, heappop
import math

class BellmanFordAlgorithm:
    """
    An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path betwen a
    starting node and all other nodes in the graph. The algorithm also detects negative cycles.
    Time Complexity: O(EV)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph: AdjacencyList):
        self.graph = graph
        n = len(graph)
        self.n = n
        # Maintain an array of the minimum distance to each node
        self.dist = [math.inf] * n


    def solve(self, start):
        # An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path between
        # a starting node and all other nodes in the graph. The algorithm also detects negative cycles.
        # If a node is a part of a negative cycle then the minimum cost for that node is set to -math.inf.
        
        self.__init__(self.graph)
        self.dist[start] = 0

        # For each node, apply relaxation for all the edges
        for node in range(0, self.n-1):
            for node_from, edges in enumerate(self.graph):
                for node_to, edge_cost in edges:
                    new_dist = self.dist[node_from] + edge_cost
                    if new_dist < self.dist[node_to]:
                        self.dist[node_to] = new_dist

        # Run algorithm a second time to detect which nodes are part
        # of a negative cycle. A negative cycle has occurred if we
        # can find a better path beyond the optimal solution.
        for node in range(0, self.n-1):
            for node_from, edges in enumerate(self.graph):
                for node_to, edge_cost in edges:
                    new_dist = self.dist[node_from] + edge_cost
                    if new_dist < self.dist[node_to]:
                        self.dist[node_to] = -math.inf

        # Return the array containing the shortest distance to every node
        return self.dist


if __name__ == "__main__":
    graph = AdjacencyList(n=9)
    graph.add_directed_edge(0, 1, 1)
    graph.add_directed_edge(1, 2, 1)
    graph.add_directed_edge(2, 4, 1)
    graph.add_directed_edge(4, 3, -3)
    graph.add_directed_edge(3, 2, 1)
    graph.add_directed_edge(1, 5, 4)
    graph.add_directed_edge(1, 6, 4)
    graph.add_directed_edge(5, 6, 5)
    graph.add_directed_edge(6, 7, 4)
    graph.add_directed_edge(5, 7, 3)

    bf = BellmanFordAlgorithm(graph)
    print(bf.solve(start=0))