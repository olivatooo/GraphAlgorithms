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


def add_random_weight(graph):
    for u,v,d in graph.edges(data=True):
        d['weight'] = random()
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    return edges, weights
        

def distancias(graph,node):
    dist = {}
    encontrados = []
    q = queue.Queue()

    for n in list(graph):
        dist[n] = inf
    encontrados.append(node)
    q.put(node)
    while not q.empty():
        v = q.get()
        for x in graph.adj[v]:
            if x not in encontrados:
                encontrados.append(x)
                q.put(x)
                dist[x]=dist[v]+1
    return dist



def dijkstra(graph,node):
    dist = {}
    prev = {}
    for n in list(graph):
        dist[n] = inf
        prev[n] = None
    dist[node] = 0
    R = []
    while R != list(graphs):
        return
        

def print_graph(graph,edges,weights):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color='black', edgelist=edges, edge_color=weights, width=1.0, edge_cmap=plt.cm.Blues)
    plt.show()


file_to_load = 'wg59_dist.txt'
file_with_labels = 'wg59_name.txt'
A = np.loadtxt(file_to_load)
G = nx.from_numpy_matrix(A)
edges, weights = add_random_weight(G)
#dijkstra(G,2)
print(distancias(G,2))
#print_graph(G,edges,weights)

