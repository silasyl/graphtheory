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
    - eulerian_path.py
    - floyd_warshall.py
    - topological_sort.py
    - tsp.py
  - trees
    - ahu.py
    - center.py
    - rooting.py
    - tree_height.py
  - breadth_first_search.py
  - depth_first_search.py
- util
  - data_structures.py (indexed priority queue)
  - graph_structures.py (adjacency list, adjacency matrix, binary node, tree node)
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

|Metrics|Topological Sort|Shortest/Longest Path|
|--|--|--|
|Complexity|O(V+E)|O(V+E)|
|Directed or Undirected graphs|Directed|Directed|
|Cycles on graphs|Acyclic|Acyclic|
|Weigths|Does not matter|Weighted|

## Travelling Salesman Problem:

|Metrics|TSP Brute Force|TSP Dynamic Programming|
|--|--|--|
|Complexity|O(n!)|Time Complexity: O(n<sup>2</sup> * 2<sup>n</sup>) / Space Complexity: O(n * 2<sup>n</sup>)|
Recommendation|Up until 12 nodes|Up until 23 nodes|

Definitions:

- <b>TSP</b>: Travelling Salesman Problem, which is the Hamiltonian cycle (path that visits every node once) of minimum cost.

## Eulerian Paths

|Settings|Eulerian Circuit|Eulerian Path|
|--|--|--|
|Undirected Graph|Every vertex has an even degree.|Either every vertex has even degree or exactly two vertices have odd degree.|
|Directed Graph|Every vertex has equal indegree and outdegree.|At most one vertex has (outdegree)-(indegree)=1 and at most one vertex has (indegree)-(outdegree)=1 and all other vertices have equal in and out degrees.|
|Complexity|O(E)|O(E)|

Definitions:

- <b>Eulerian Path/Trail</b>: A path of edges that visits all the edges in a graph exactly once.
- <b>Eulerian Circuit/Cycle</b>: An Eulerian Path which starts and ends on the same vertex.

# Trees Algorithms:

|Metrics|Tree Height|Rooting|Center|AHU (Aho, Hopcroft, Ullman)|
|--|--|--|--|--|
|Complexity|O(V)|O(V+E)|O(V+E)||
|Application|Detect height of a tree|Transform an undirected graph into a rooted tree|Identify tree center(s)|Detect isomorphic trees|

Definitions:

- <b>Tree</b>: A connected graph with N nodes an N-1 edges.
- <b>Isomorphism</b>: Isomorphic graphs are graphs that are structurally the same. In simple terms, for an isomorphism to exist there needs to be a function which can map all the nodes/edges in G1 to G2 and vice-versa.
