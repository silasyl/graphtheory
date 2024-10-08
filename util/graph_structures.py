import math

class AdjacencyList:

    # Adjacency List representation of a graph

    def __init__(self, source):
        if isinstance(source, int):
            # Build an adjacency list from scratch
            self.n = source
            self.graph = [[] for _ in range(source)]
        elif isinstance(source, AdjacencyMatrix):
            # Convert the AdjacencyMatrix into an AdjacencyList
            self.n = len(source)
            self.graph = [[] for _ in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    if source.graph[i][j] != math.inf and i != j:
                        self.graph[i].append((j, source.graph[i][j]))
        elif isinstance(source, BinaryNode):
            # Helper function to recursively traverse the tree
            def traverse(node):
                if node is None:
                    return None
                # Add the connection for the left child if it exists
                if node.left is not None:
                    self.add_edge(node.index, node.left.index, directed=False)
                    traverse(node.left)
                # Add the connection for the right child if it exists
                if node.right is not None:
                    self.add_edge(node.index, node.right.index, directed=False)
                    traverse(node.right)

            # Helper function to count the number of nodes in the tree
            def count_nodes(node):
                if node is None:
                    return 0
                return 1 + count_nodes(node.left) + count_nodes(node.right)
            
            # Convert the tree starting from a root Node into an AdjacencyList
            self.n = count_nodes(source)
            self.graph = [[] for _ in range(self.n)]
            traverse(source)
        else:
            raise TypeError("Argument must be an integer or an AdjacencyMatrix instance!")

    def __len__(self):
        return len(self.graph)
    
    def __getitem__(self, index):
        return self.graph[index]
    
    def add_edge(self, from_node, to_node, weight=0, directed=True):
        self.graph[from_node].append((to_node, weight))
        if directed is False:
            self.graph[to_node].append((from_node, weight))


class AdjacencyMatrix:

    # Adjacency Matrix representation of a graph

    def __init__(self, source):
        if isinstance(source, int):
            # Build an adjacency matrix from scratch
            self.n = source
            self.graph = [[math.inf] * source for _ in range(source)]
            # Fill main diagonal with 0
            for i in range(source):
                self.graph[i][i] = 0
        
        elif isinstance(source, AdjacencyList):
            # Convert the AdjacencyList into an AdjacencyMatrix
            self.n = len(source)
            self.graph = [[math.inf] * self.n for _ in range(self.n)]
            # Fill main diagonal with 0
            for i in range(self.n):
                self.graph[i][i] = 0
            for from_node, edges in enumerate(source):
                for to_node, weight in edges:
                    self.graph[from_node][to_node] = weight
        else:
            raise TypeError("Argument must be an integer or an AdjacencyList instance!")

    def __len__(self):
        return self.n
    
    def __getitem__(self, indices):
        i, j = indices
        return self.graph[i][j]
    
    def add_edge(self, from_node, to_node, weight=1, directed=True):
        self.graph[from_node][to_node] = weight
        if directed is False:
            self.graph[to_node][from_node] = weight


class BinaryNode:

    # Build a Binary Tree structure.

    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.left = None
        self.right = None


class Node:

    # Build a Tree structure.

    def __init__(self, index, value=None):
        self.index = index
        self.value = value
        self.children = []


if __name__ == "__main__":
    graph = AdjacencyList(n=14)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(2, 9)
    graph.add_edge(8, 2)
    graph.add_edge(3, 4)
    graph.add_edge(10, 11)
    graph.add_edge(12, 13)
    graph.add_edge(3, 5)
    graph.add_edge(5, 7)
    graph.add_edge(5, 6)
    graph.add_edge(0, 10)
    graph.add_edge(11, 12)

    print(graph.graph)