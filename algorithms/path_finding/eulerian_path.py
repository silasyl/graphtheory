from util.graph_structures import AdjacencyList, AdjacencyMatrix
import math
import itertools

class EulerianPathAlgorithm:
    """
    Implementation of finding an Eulerian Path on a graph. This implementation verifies that the
    input graph is fully connected and supports self loops and repeated edges between nodes.
    Time Complexity: O(E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph, start_node=0):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(graph)
        self.n = n
        self.edge_count = 0
        # Arrays that track the in degree and out degree of each node.
        self.in_degree = [0] * n
        self.out_degree = [0] * n
        self.path = []
        self.solved = False


    def solve(self):
        # Returns a list of edge_count + 1 node ids that give the Eulerian path or
        # None if no path exists or the graph is dsconnected.
        if self.solved:
            return self.path
        
        self.solved = True
        self.set_up()

        if not self.graph_has_eulerian_path():
            return None
        
        self.dfs(self.find_start_node())

        # Make sure all edges of the graph were traversed. It could be the
        # case that the graph is disconnected in which case return None.
        if len(self.path) != self.edge_count + 1:
            return None
        
        self.path = self.path[::-1]
        
        return self.path
    
    def set_up(self):
        # Compute in and out node degrees.
        for from_node in range(self.n):
            for to_node, _ in self.graph[from_node]:
                self.out_degree[from_node] += 1
                self.in_degree[to_node] += 1
                self.edge_count += 1

    def graph_has_eulerian_path(self):
        if self.edge_count == 0:
            return False
        
        start_nodes = 0
        end_nodes = 0

        for i in range(self.n):
            if self.out_degree[i] - self.in_degree[i] > 1 or self.in_degree[i] - self.out_degree[i] > 1:
                return False
            elif self.out_degree[i] - self.in_degree[i] == 1:
                start_nodes += 1
            elif self.in_degree[i] - self.out_degree[i] == 1:
                end_nodes += 1
        return (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1)
    
    def find_start_node(self):
        start_node = 0
        for i in range(self.n):
            # Unique starting node.
            if self.out_degree[i] - self.in_degree[i] == 1:
                return i
            # Start at a node with an outgoing edge.
            if self.out_degree[i] > 0:
                start_node = i
        return start_node
    
    def dfs(self, at):
        # Perform DFS to find Eulerian path.
        while self.out_degree[at] > 0:
            next_node, _ = self.graph[at][self.out_degree[at] - 1]
            self.out_degree[at] -= 1
            self.dfs(next_node)
        self.path.append(at)


if __name__ == "__main__":
    graph = AdjacencyList(7)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 2)
    graph.add_edge(2, 4)
    graph.add_edge(2, 4)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 5)
    graph.add_edge(4, 3)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 3)

    ep = EulerianPathAlgorithm(graph)
    print(ep.solve())
