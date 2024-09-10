from util.graph_structures import AdjacencyList, AdjacencyMatrix, BinaryNode, Node

class TreeHeightAlgorithm:
    """
    An algorithm to detect the height of a tree.
    Time Complexity: O(V)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, root):
        if isinstance(root, BinaryNode):
            self.binary = True
        elif isinstance(root, Node):
            self.binary = False
        else:
            raise TypeError("Argument must be a BinaryNode or a Node!")
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
        
        if self.binary:
            return max(self.recursive_step(node.left), self.recursive_step(node.right)) + 1
        else:
            return max(self.recursive_step(child) for child in node.children) + 1
    
    def is_leaf_node(self, node):
        if self.binary:
            return node.left == None and node.right == None
        else:
            return len(node.children) == 0


if __name__ == "__main__":
    root = BinaryNode(0)

    node1 = BinaryNode(1)
    node2 = BinaryNode(2)
    root.left = node1
    root.right = node2

    node3 = BinaryNode(3)
    node4 = BinaryNode(4)
    node1.left = node3
    node1.right = node4

    node5 = BinaryNode(5)
    node6 = BinaryNode(6)
    node2.left = node5
    node2.right = node6

    node7 = BinaryNode(7)
    node8 = BinaryNode(8)
    node3.left = node7
    node3.right = node8

    tree_h = TreeHeightAlgorithm(root)
    print(tree_h.solve())
