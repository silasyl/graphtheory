from util.graph_structures import AdjacencyList, AdjacencyMatrix, Node

class CenterAlgorithm:
    """
    This algorithm finds the center(s) of a tree.
    Time Complexity: O(V+E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        n = len(graph)
        self.n = n


    def solve(self):
        # Find all leaf nodes
        degree = [0] * self.n
        leaves = []

        for i in range(self.n):
            edges = self.graph[i]
            degree[i] = len(edges)
            if degree[i] <= 1:
                leaves.append(i)
                degree[i] = 0

        processed_leaves = len(leaves)

        # Remove leaf nodes and decrease the degree of each node adding new leaf nodes progressively
        # until only the centers remain.
        while processed_leaves < self.n:
            new_leaves = []
            for node in leaves:
                for neighbor in self.graph[node]:
                    degree[neighbor[0]] -= 1
                    if degree[neighbor[0]] == 1:
                        new_leaves.append(neighbor[0])
                degree[node] = 0
            processed_leaves += len(new_leaves)
            leaves = new_leaves
        return leaves # center(s)


if __name__ == "__main__":
    graph = AdjacencyList(10)
    graph.add_edge(0, 1, directed=False)
    graph.add_edge(1, 2, directed=False)
    graph.add_edge(2, 3, directed=False)
    graph.add_edge(2, 6, directed=False)
    graph.add_edge(2, 9, directed=False)
    graph.add_edge(3, 4, directed=False)
    graph.add_edge(3, 5, directed=False)
    graph.add_edge(6, 7, directed=False)
    graph.add_edge(6, 8, directed=False)

    center = CenterAlgorithm(graph)
    print(center.solve())
