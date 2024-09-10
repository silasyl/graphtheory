from util.graph_structures import AdjacencyList, AdjacencyMatrix, Node

class TreeHeightAlgorithm:
    """
    An algorithm to detect the height of a tree.
    Time Complexity: O(V)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, root: Node):
        self.root = root


    def solve(self):
        # Returns the height of the binary tree which is the number of edges from the
        # root to the deepest leaf node, or -1 if the input is an empty tree.
        node = self.root

        return self.recursive_step(node)


    def recursive_step(self, node):
        # Returns the height of the binary tree which is the number of edges from the
        # root to the deepest leaf node, or -1 if the input is an empty tree.

        if (node == None):
            return -1
        
        if self.is_leaf_node(node):
            return 0
        
        return max(self.recursive_step(node.left), self.recursive_step(node.right)) + 1
    
    def is_leaf_node(self, node):
        return node.left == None and node.right == None


if __name__ == "__main__":
    root = Node(0)

    node1 = Node(1)
    node2 = Node(2)
    root.left = node1
    root.right = node2

    node3 = Node(3)
    node4 = Node(4)
    node1.left = node3
    node1.right = node4

    node5 = Node(5)
    node6 = Node(6)
    node2.left = node5
    node2.right = node6

    node7 = Node(7)
    node8 = Node(8)
    node3.left = node7
    node3.right = node8

    tree_h = TreeHeightAlgorithm(root)
    print(tree_h.solve())
