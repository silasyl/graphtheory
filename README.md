# graphtheory
Graph Algorithms with Python

Based on original codes in Java from: https://github.com/williamfiset/Algorithms
<br>With my own improvements
<br>@silasyl

# Files:

- algorithms
  - components
    - articulation_detection.py
    - bridge_detection.py
    - tarjan.py
  - path_finding
    - bellman_ford.py
    - dijkstra.py
    - floyd_warshall.py
    - topological_sort.py
  - breadth_first_search.py
  - depth_first_search.py
- util
  - data_structures.py (indexed priority queue)
  - graph_structures.py (adjacency list, adjacency matrix)
  - view.py

# Components Algorithms:

|Metric|Bridge detection|Articulation detection|Tarjan|
|--|--|--|--|
|Complexity|O(V+E)|O(V+E)|O(V+E)|
|Detection|Bridges|Articulation points|Strongly Connected Components|
|Directed or Undirected graphs|Undirected|Undirected|Directed|
|Weights|Does not matter|Does not matter|Does not matter|

Definitions:

- <b>Bridges</b>: Edges in a graph whose removal increases the number of connected components, thereby disconnecting parts of the graph.
- <b>Articulation Points</b>: Vertices in a graph whose removal increases the number of connected components, causing the graph to become disconnected.
- <b>Strongly Connected Components</b>: Subsets of a directed graph where every vertex is reachable from every other vertex within the same subset.

# Path Findings

## Shortest Path Algorithms:

|Metric|BFS|Dijkstra|Bellman Ford|Floyd Warshall|
|--|--|--|--|--|
|Complexity|O(V+E)|O((V+E)logV)|O(VE)|O(V<sup>3</sup>)|
|Recommended graph size|Large|Large/Medium|Medium/Small|Small|
|Good for APSP?|Only works on unweighted graphs|Ok|Bad|Yes|
|Can detect negative cycles?|No|No|Yes|Yes|
|SP on graph with weighted edges|Incorrect SP answer|Best algorithm|Works|Bad in general|
|SP on graph with unweighted edges|Best algorithm|Ok|Bad|Bad in general|

Reference: Competitive Programming 3, P. 161, Steven & Felix Halim

## Directed Acyclic Graphs (DAG):

|Metrics|Topological Sort|
|--|--|
|Complexity|O(V+E)|
|Directed or Undirected graphs|Directed|
|Cycles on graphs|Acyclic|
|Weigths|Does not matter|
