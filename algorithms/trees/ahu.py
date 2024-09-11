from util.graph_structures import AdjacencyList, AdjacencyMatrix, Node
from algorithms.trees.center import CenterAlgorithm
from algorithms.trees.rooting import RootingAlgorithm

class AHUAlgorithm:
    """
    AHU (Aho, Hopcroft, Ullman)
    Determines if two unrooted trees are isomorphic. This algorithm can easily be modified to support
    checking if two rooted trees are isomorphic.
    
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph1, graph2):
        if isinstance(graph1, AdjacencyMatrix):
            graph1 = AdjacencyList(graph1)
        if isinstance(graph2, AdjacencyMatrix):
            graph2 = AdjacencyList(graph2)
        self.graph1 = graph1
        self.graph2 = graph2


    def solve(self):
        # Determins if two unrooted trees are isomorphic
        centers1 = CenterAlgorithm(self.graph1).solve()
        centers2 = CenterAlgorithm(self.graph2).solve()

        tree1_rooted = RootingAlgorithm(self.graph1).build_tree(centers1[0])
        tree1_encoded = self.encode(tree1_rooted)

        for center in centers2:
            tree2_rooted = RootingAlgorithm(self.graph2).build_tree(center)
            tree2_encoded = self.encode(tree2_rooted)
            # Two trees are isomorphic if their encoded
            # canonical forms are equal.
            if tree1_encoded == tree2_encoded:
                return True
        return False
    

    def encode(self, node):
        # Constructs the canonical form representation of a tree as a string.
        if node == None:
            return ''
        
        labels = []
        for child in node.children:
            labels.append(self.encode(child))

        labels.sort()

        return '(' + ''.join(labels) + ')'


if __name__ == "__main__":
    graph1 = AdjacencyList(5)
    graph1.add_edge(2, 0, directed=False)
    graph1.add_edge(3, 4, directed=False)
    graph1.add_edge(2, 1, directed=False)
    graph1.add_edge(2, 3, directed=False)

    graph2 = AdjacencyList(5)
    graph2.add_edge(1, 0, directed=False)
    graph2.add_edge(2, 4, directed=False)
    graph2.add_edge(1, 3, directed=False)
    graph2.add_edge(1, 2, directed=False)

    ahu = AHUAlgorithm(graph1, graph2)
    print(ahu.solve())
