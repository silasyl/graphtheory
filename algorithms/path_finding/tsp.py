from util.graph_structures import AdjacencyList, AdjacencyMatrix
import math
import itertools

class TSPAlgorithm:
    """
    Brute Force: Time Complexity: O(n!)
    Dynamic Programming: Time Complexity: O(n^2 * 2^n) Space Complexity: O(n * 2^n)
    Based on original code in Java from: https://github.com/williamfiset/Algorithms
    """

    def __init__(self, graph, start_node=0):
        if isinstance(graph, AdjacencyList):
            graph = AdjacencyMatrix(graph)
        self.graph = graph
        n = len(graph)
        self.n = n
        self.distance = graph
        self.START_NODE = start_node
        # The finished state is when the finished state mask has all bits are set to
        # one (meaning all the nodes have been visited).
        self.FINISHED_STATE = (1 << n) - 1
        self.min_tour_cost = math.inf
        self.tour = []
        self.solved = False


    def get_tour(self, brute=False):
        # Returns the optimal tour for the traveling salesman problem.
        if not self.solved:
            if brute:
                self.solve_brute_force()
            else:
                self.solve_dp()
        return self.tour
    

    def get_tour_cost(self, brute=False):
        # Returns the minimal tour cost.
        if not self.solved:
            if brute:
                self.solve_brute_force()
            else:
                self.solve_dp()
        return self.min_tour_cost



    def solve_brute_force(self):
        """
        This file shows how to solve the traveling salesman problem using a brute force approach.
        Since the time complexity is on the order of O(n!) this method is not convenient for n > 12.
        Time Complexity: O(n!)
        """
        # Given an nxn complete graph represented as an adjacency
        # matrix this method finds the best tour that visits all
        # the nodes while minimizing the overall visit cost.

        # Validate inputs.
        if self.n > 12:
            raise ValueError("Matrix too large! Time complexity of O(n!) is too high.")
        
        permutation = list(range(self.n))  # Create initial permutation [0, 1, 2, ..., n-1]
        best_tour = permutation[:]
        best_tour_cost = math.inf

        # Try all n! tours
        for perm in itertools.permutations(permutation):
            tour_cost = self.compute_tour_cost(perm)

            if tour_cost < best_tour_cost:
                best_tour_cost = tour_cost
                best_tour = perm

        self.tour = best_tour
        self.min_tour_cost = best_tour_cost
        self.solved = True
    
    def compute_tour_cost(self, tour):
        # Compute the total cost of the tour by summing the edge weights between consecutive nodes.
        cost = 0

        # Compute the cost of going to each node
        for i in range(1, self.n):
            from_node = tour[i - 1]
            to_node = tour[i]
            cost += self.graph[from_node][to_node]

        # Compute the cost to return to the starting node
        last = tour[self.n - 1]
        first = tour[0]
        return cost + self.graph[last][first]
    

    def solve_dp(self):
        """
        This file contains a recursive implementation of the TSP problem using dynamic programming. The
        main idea is that since we need to do all n! permutations of nodes to find the optimal solution
        that caching the results of sub paths can improve performance.
        
        For example, if one permutation is: '... D A B C' then later when we need to compute the value
        of the permutation '... E B A C' we should already have cached the answer for the subgraph
        containing the nodes {A, B, C}.
        Time Complexity: O(n^2 * 2^n) Space Complexity: O(n * 2^n)
        """
        # Validate inputs.
        if self.n > 32:
            raise ValueError("Matrix too large! Time complexity of O(n^2*2^n) is too high.")
        
        # Run the solver
        state = 1 << self.START_NODE
        memo = [[None] * (1 << self.n) for _ in range(self.n)]
        prev = [[None] * (1 << self.n) for _ in range(self.n)]

        self.min_tour_cost = self.tsp(self.START_NODE, state, memo, prev)

        # Regenerate path
        index = self.START_NODE
        while True:
            self.tour.append(index)
            next_index = prev[index][state]
            if next_index is None:
                break
            state |= (1 << next_index)
            index = next_index

        self.tour.append(self.START_NODE)  # Return to the start node
        self.solved = True

    def tsp(self, i, state, memo, prev):
        # Done this tour. Return cost of going back to start node.
        if state == self.FINISHED_STATE:
            return self.distance[i][self.START_NODE]

        # Return cached answer if already computed.
        if memo[i][state] is not None:
            return memo[i][state]

        min_cost = math.inf
        index = -1

        for next_node in range(self.n):
            # Skip if the next node has already been visited.
            if state & (1 << next_node):
                continue

            next_state = state | (1 << next_node)
            new_cost = self.distance[i][next_node] + self.tsp(next_node, next_state, memo, prev)

            if new_cost < min_cost:
                min_cost = new_cost
                index = next_node

        prev[i][state] = index
        memo[i][state] = min_cost

        return min_cost


if __name__ == "__main__":
    n = 10
    matrix = [[100] * n for _ in range(n)]

    # Construct an optimal tour
    edge_cost = 5
    optimal_tour = [2, 7, 6, 1, 9, 8, 5, 3, 4, 0, 2]
    for i in range(1, len(optimal_tour)):
        matrix[optimal_tour[i - 1]][optimal_tour[i]] = edge_cost

    tsp_solver = TSPAlgorithm(matrix)

    best_tour = tsp_solver.get_tour()
    print("Best tour:", best_tour)

    tour_cost = tsp_solver.get_tour_cost()
    print("Tour cost:", tour_cost)
