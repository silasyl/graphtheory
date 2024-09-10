from util.graph_structures import AdjacencyList, AdjacencyMatrix, Node

class RootingAlgorithm:
    """
    Often when working with trees we are given them as a graph with undirected edges, however
    sometimes a better representation is a rooted tree.
    Time Complexity: O(V+E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph


    def build_tree(self, root_index):
        # Create the rood node
        root = Node(root_index)

        # Build the tree starting from the rood node
        return self.dfs(root, None)


    def dfs(self, node, parent):
        # Helper method to recursively build the tree.

        for edge in self.graph[node.index]:
            if parent and edge[0] == parent.index:
                continue
            child = Node(edge[0])
            node.children.append(child)
            # Recursively build the subtree for the child node
            self.dfs(child, node)
        return node


if __name__ == "__main__":
    graph = AdjacencyList(9)
    graph.add_edge(0, 1, directed=False)
    graph.add_edge(0, 2, directed=False)
    graph.add_edge(1, 3, directed=False)
    graph.add_edge(1, 4, directed=False)
    graph.add_edge(3, 7, directed=False)
    graph.add_edge(3, 8, directed=False)
    graph.add_edge(2, 5, directed=False)
    graph.add_edge(2, 6, directed=False)

    rooting = RootingAlgorithm(graph)
    print(rooting.build_tree(0))
