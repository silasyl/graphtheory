from util.graph_structures import AdjacencyList, AdjacencyMatrix
from collections import deque

class BreadthFirstSearch:
    """
    This is an implementation of doing a breadth first search recursively with a slight cheat of
    passing in a queue as an argument to the function.
    Time Complexity: O(V + E)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph):
        if isinstance(graph, AdjacencyMatrix):
            graph = AdjacencyList(graph)
        self.graph = graph
        self.DEPTH_TOKEN = -1
        # Each breadth first search layer gets separated by a DEPTH_TOKEN.
        # DEPTH_TOKENs help count the distance from one node to another because
        # we can increment the depth counter each time a DEPTH_TOKEN is encountered
        n = len(self.graph)
        self.n = n
        self.visited = [False] * n

    
    def solve(self, start:int) -> int:
        # Computes the eccentricity (distance to furtherst node) from the starting node.
        queue = deque([start, self.DEPTH_TOKEN])
        return self.recursive_step(queue)
    
    def recursive_step(self, queue) -> int:
        
        at = queue.popleft()

        if at == self.DEPTH_TOKEN:
            queue.append(self.DEPTH_TOKEN)
            return 1
        
        # This node is already visited.
        if self.visited[at]:
            return 0
        
        # Visit this node.
        self.visited[at] = True

        # Add all neighbors to queue.
        neighbors = self.graph[at]
        if neighbors:
            for next_node in neighbors:
                if not self.visited[next_node[0]]:
                    queue.append(next_node[0])

        depth = 0

        while True:
            # Stop when the queue is empty (i.e there'a only one depth token remaining)
            if len(queue) == 1 and queue[0] == self.DEPTH_TOKEN:
                break

            # The depth is the sum of all DEPTH_TOKENS encountered.
            depth += self.recursive_step(queue)

        return depth


if __name__ == "__main__":
    graph = AdjacencyList(14)
    graph.add_edge(0, 1, directed=False)
    graph.add_edge(0, 2, directed=False)
    graph.add_edge(0, 3, directed=False)
    graph.add_edge(2, 9, directed=False)
    graph.add_edge(8, 2, directed=False)
    graph.add_edge(3, 4, directed=False)
    graph.add_edge(10, 11, directed=False)
    graph.add_edge(12, 13, directed=False)
    graph.add_edge(3, 5, directed=False)
    graph.add_edge(5, 7, directed=False)
    graph.add_edge(5, 6, directed=False)
    graph.add_edge(0, 10, directed=False)
    graph.add_edge(11, 12, directed=False)

    bfs = BreadthFirstSearch(graph)
    print(bfs.solve(start=12))