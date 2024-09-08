from util.graph_structures import AdjacencyList, AdjacencyMatrix
import math

class FloydWarshallAlgorithm:
    """
    This file contains an implementation of the Floyd-Warshall algorithm to find all pairs of
    shortest path between nodes in a graph. We also demonstrate how to detect negative cycle and
    reconstruct the shortest path.
    Time Complexity: O(V^3)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, matrix):
        if isinstance(matrix, AdjacencyList):
            matrix = AdjacencyMatrix(matrix)
        self.matrix = matrix
        n = len(matrix)
        self.n = n
        # The memo table that will contain All Pairs Shortest Paths (APSP) through Dynamic Programming
        self.dp = [[None] * n for _ in range(n)]
        # Matrix used to reconstruct shortest paths
        self.next = [[None] * n for _ in range(n)]
        self.REACHES_NEGATIVE_CYCLE = -1
        self.solved = False

        # Setup step
        self.setup_step()


    def setup_step(self):
        # Copy input matrix and setupt 'next' matrix for path reconstruction.
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix.graph[i][j] != math.inf:
                    self.next[i][j] = j
                self.dp[i][j] = self.matrix.graph[i][j]

    def solve(self):
        # As input, this class takes an adjacency matrix with edge weights between nodes, where
        # math.inf is used to indicate that two nodes are not connected.
        # Usually the diagonal of the adjacency matrix is all zeros (i.e. matrix[i][i] = 0 for
        # all i) since there is typically no cost to go from a node to itself, but this may depend on
        # your graph and the problem you are trying to solve.
        
        # Execute the Floyd-Warshall algorithm
        self.solve_step()
        return self.dp
    
    def solve_step(self):
        # Runs Floyd-Warshall to compute the shortest distance between every pair of nodes.
        if self.solved:
            return None
        
        # Compute all pairs shortest paths.
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    new_dist = self.dp[i][k] + self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist
                        self.next[i][j] = self.next[i][k]

        # Identify negative cycles by propagating the value '-math.inf'
        # to every edge that is part of or reaches into a negative cycle.
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] != math.inf and self.dp[k][j] != math.inf and self.dp[k][k] < 0:
                        self.dp[i][j] = -math.inf
                        self.next[i][j] = self.REACHES_NEGATIVE_CYCLE

        self.solved = True
        return None
    
    def reconstruct_path(self, start, end):
        # Reconstructs the shortest path (of nodes) from 'start' to 'end' inclusive.
        # return an array of nodes indexes of the shortest path from 'start' to 'end'. If 'start' and
        # 'end' are not connected return an empty array. If the shortest path from 'start' to 'end'
        # are reachable by a negative cycle return -1.

        if end < 0 or end >= self.n:
            raise ValueError("Invalid node index")
        if start < 0 or start >= self.n:
            raise ValueError("Invalid node index")
        
        self.solve_step()
        path = []
        if self.dp[start][end] == math.inf:
            return path
        at = start
        while at != end:
            # Return math.inf since there are an infinite number of shortest paths.
            if at == self.REACHES_NEGATIVE_CYCLE:
                return math.inf
            path.append(at)
            at = self.next[at][end]
        
        # Return math.inf since there are an infinite number of shortest paths.
        if self.next[at][end] == self.REACHES_NEGATIVE_CYCLE:
            return math.inf
        path.append(end)
        return path


if __name__ == "__main__":
    graph = AdjacencyMatrix(7)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 5)
    graph.add_edge(0, 6, 10)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 4, 11)
    graph.add_edge(2, 6, 2)
    graph.add_edge(6, 5, 11)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 4, -2)

    fw = FloydWarshallAlgorithm(graph)
    print(fw.solve())