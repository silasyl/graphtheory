from auxiliars.structures import AdjacencyList
import networkx as nx
import matplotlib.pyplot as plt

def view_graph(graph):
    G = nx.Graph()

    if isinstance(graph, AdjacencyList):
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    plt.show()