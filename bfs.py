from structures import AdjacencyList
from collections import deque

def breadth_first_search_recursive(graph: AdjacencyList, start:int, DEPTH_TOKEN=-1) -> int:
    """
    This is an implementation of doing a breadth first search recursively with a slight cheat of
    passing in a queue as an argument to the function.
    Time Complexity: O(V + E)
    Based on original code in Java from: https://github.com/williamfiset/
    """
                                   
    # Each breadth first search layer gets separated by a DEPTH_TOKEN.
    # DEPTH_TOKENs help count the distance from one node to another because
    # we can increment the depth counter each time a DEPTH_TOKEN is encountered

    # Computes the eccentricity (distance to furtherst node) from the starting node.
    n = len(graph)
    visited = [False] * n
    queue = deque([start, DEPTH_TOKEN])
    return bfs_recursive(visited, queue, graph, DEPTH_TOKEN)
    

def bfs_recursive(visited, queue, graph, DEPTH_TOKEN=-1) -> int:
        
    at = queue.popleft()

    if at == DEPTH_TOKEN:
        queue.append(DEPTH_TOKEN)
        return 1
        
    # This node is already visited.
    if visited[at]:
        return 0
        
    # Visit this node.
    visited[at] = True

    # Add all neighbors to queue.
    neighbors = graph[at]
    if neighbors:
        for next_node in neighbors:
            if not visited[next_node]:
                queue.append(next_node)

    depth = 0

    while True:
        # Stop when the queue is empty (i.e there'a only one depth token remaining)
        if len(queue) == 1 and queue[0] == DEPTH_TOKEN:
            break

        # The depth is the sum of all DEPTH_TOKENS encountered.
        depth += bfs_recursive(visited, queue, graph, DEPTH_TOKEN)

    return depth


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

    print(breadth_first_search_recursive(graph, start=12))