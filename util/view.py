from util.graph_structures import AdjacencyList
import networkx as nx
import matplotlib.pyplot as plt

def view_graph(graph, directed=True):
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()

    if isinstance(graph, AdjacencyList):
        is_weighted = False
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                if neighbor[1] != 0:
                    if is_weighted is False:
                        is_weighted = True
                    G.add_edge(node, neighbor[0], weight=neighbor[1])
                elif is_weighted is True:
                    G.add_edge(node, neighbor[0], weight=neighbor[1])
                else:
                    G.add_edge(node, neighbor[0])

    pos = nx.spring_layout(G)  # Layout para o grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')

    if is_weighted:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()