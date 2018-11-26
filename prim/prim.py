"""
    Criado por:
    Gabriel Olivato - 743537
    Igor Raphael Magollo - 743550
    Claudia Sanches - 743521

    PROJETO 4: ÁRVORES DE CAMINHOS MÍNIMOS E AGRUPAMENTO DE DADOS

"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import inf
from random import random
import queue


def load_labels(arq):
    labels = {}
    count = 0
    file = open(arq, "r")
    for f in file:
        if '#' not in f:
            labels[count] = f
    return labels


def init_djikstra_with_rng_weights(graph):
    for u,v,d in graph.edges(data=True):
        d['weight'] = random()
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    return edges, weights
         

def print_graph(graph,edges,weights):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color='blue', edgelist=edges, edge_color=weights, width=1.0, edge_cmap=plt.cm.Blues)
    plt.show()


file_to_load = 'ha30_dist.txt'
file_with_labels = 'ha30_name.txt'
A = np.loadtxt(file_to_load)
G = nx.from_numpy_matrix(A)

edges, weights = init_djikstra_with_rng_weights(G)

print_graph(G,edges,weights)

#djikstra(G,1)

