class AdjacencyList:

    # Adjacency List representation of a graph
    # Will begin with undirected graph
    # Will begin with graph without weights

    def __init__(self, n: int):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def __len__(self):
        return len(self.graph)
    
    def __getitem__(self, index):
        return self.graph[index]

    def add_undirected_edge(self, from_node, to_node):
        self.graph[from_node].append(to_node)
        self.graph[to_node].append(from_node)


if __name__ == "__main__":
    graph = AdjacencyList(n=14)
    graph.add_undirected_edge(0, 1)
    graph.add_undirected_edge(0, 2)
    graph.add_undirected_edge(0, 3)
    graph.add_undirected_edge(2, 9)
    graph.add_undirected_edge(8, 2)
    graph.add_undirected_edge(3, 4)
    graph.add_undirected_edge(10, 11)
    graph.add_undirected_edge(12, 13)
    graph.add_undirected_edge(3, 5)
    graph.add_undirected_edge(5, 7)
    graph.add_undirected_edge(5, 6)
    graph.add_undirected_edge(0, 10)
    graph.add_undirected_edge(11, 12)

    print(graph.graph)