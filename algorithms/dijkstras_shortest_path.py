from util.graph_structures import AdjacencyList
from util.data_structures import IndexedPriorityQueue
from heapq import heappush, heappop
import math

class DijkstrasShortestPath:

    def __init__(self, graph: AdjacencyList):
        self.graph = graph
        n = len(graph)
        self.n = n
        self.visited = [False] * n
        self.prev = [None] * n
        self.dist = [math.inf] * n


    def solve_lazy(self, start, end):
        """
        This is an implementation of Dijkstra's shortest path algorithm from a start node to a
        specific ending node. Dijkstra can also be modified to find the shortest path between a starting
        node and all other nodes in the graph. However, in this implementation since we're only going
        from a starting node to an ending node we can employ an optimization to stop early once we've
        visited all the neighbors of the ending node.
        Based on original code in Java from: https://github.com/williamfiset/
        """
        self.__init__(self.graph)
        self.dist[start] = 0
        pq = []
        heappush(pq, (0, start))

        while pq:
            node_val, node_from = heappop(pq)
        
            # We already visited this node and can ignore it
            if self.visited[node_from]:
                continue
            self.visited[node_from] = True

            # We already found a better path before we got to
            # processing this node so we can ignore it
            if self.dist[node_from] < node_val:
                continue

            edges = self.graph[node_from]
            for node_to, edge_cost in edges:
                # You cannot get a shorter path by revisiting
                # a node you have already visited before.
                if self.visited[node_to]:
                    continue

                # Relax edge by updating minimum cost if applicable.
                new_dist = self.dist[node_from] + edge_cost
                if new_dist < self.dist[node_to]:
                    self.prev[node_to] = node_from
                    self.dist[node_to] = new_dist
                    heappush(pq, (self.dist[node_to], node_to))

            # Once we've visited all the nodes spanning from the end
            # node we know we can return the minimum distance value to
            # the end node because it cannot get any better after this point.
            if node_from == end:
                return self.dist[end]

        # End node is unreachable
        return math.inf
    

    def solve_eager(self, start, end):
        """
        This file contains an implementation of Dijkstra's shortest path algorithm from a start node to a
        specific ending node. Dijkstra's can also be modified to find the shortest path between a
        starting node and all other nodes in the graph with minimal effort.
        Based on original code in Java from: https://github.com/williamfiset/
        """
        self.__init__(self.graph)
        self.dist[start] = 0

        # This implementation uses an Indexed Priority Queue.
        ipq = IndexedPriorityQueue()
        ipq.push(start, 0)

        while not ipq.is_empty():
            node_from, node_val = ipq.pop()
        
            # We already visited this node and can ignore it
            if self.visited[node_from]:
                continue
            self.visited[node_from] = True

            # We already found a better path before we got to
            # processing this node so we can ignore it
            if self.dist[node_from] < node_val:
                continue

            edges = self.graph[node_from]
            for node_to, edge_cost in edges:
                # You cannot get a shorter path by revisiting
                # a node you have already visited before.
                if self.visited[node_to]:
                    continue

                # Relax edge by updating minimum cost if applicable.
                new_dist = self.dist[node_from] + edge_cost
                if new_dist < self.dist[node_to]:
                    self.prev[node_to] = node_from
                    self.dist[node_to] = new_dist
                    ipq.push(node_to, self.dist[node_to])

            # Once we've visited all the nodes spanning from the end
            # node we know we can return the minimum distance value to
            # the end node because it cannot get any better after this point.
            if node_from == end:
                return self.dist[end]

        # End node is unreachable
        return math.inf
    

    def reconstruct_path(self, start, end, lazy=False):
        if end < 0 or end >= self.n:
            raise ValueError("Invalid node index")
        if start < 0 or start >= self.n:
            raise ValueError("Invalid node index")
        if lazy:
            dist = self.solve_lazy(start, end)
        else:
            dist = self.solve_eager(start, end)
        path = []
        if dist == math.inf:
            return path
        at = end
        while at is not None:
            path.append(at)
            at = self.prev[at]
        path.reverse()
        return path


if __name__ == "__main__":
    graph = AdjacencyList(n=5)
    graph.add_directed_edge(0, 1, 4)
    graph.add_directed_edge(0, 2, 1)
    graph.add_directed_edge(1, 3, 1)
    graph.add_directed_edge(2, 1, 2)
    graph.add_directed_edge(2, 3, 5)
    graph.add_directed_edge(3, 4, 3)

    dijkstra = DijkstrasShortestPath(graph)
    print(dijkstra.solve_lazy(start=0, end=4))