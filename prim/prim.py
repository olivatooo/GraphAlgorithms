"""
    Criado por:
    Gabriel Olivato - 743537
    Igor Raphael Magollo - 743550
    Claudia Sanches - 743521

    PROJETO 2: ÁRVORE GERADORA MÍNIMA

"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from math import inf

def load_labels(arq):
    labels = {}
    count = 0
    file = open(arq, "r")
    for f in file:
        if '#' not in f:
            labels[count] = f
            count+=1
    return labels


def init(graph):
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    return edges, weights


def prim(graph,initial):
    pi = {}
    visitados = []
    w = nx.get_edge_attributes(graph,'weight')
    
    # Iniciando pi
    for i in list(graph):
        pi[i] = None

    proximo = initial
    while proximo != "Done":
        menor = inf
        for i in list(graph.adj[proximo]):
            if i not in visitados:
                try:
                    value = int(w[(proximo,i)])
                except KeyError:
                    value = int(w[(i,proximo)])
                if value <= menor:
                    menor = value
                    pi[proximo] = i
        
        if menor == inf:
            proximo = "Done"
        else:
            proximo = pi[proximo]
            visitados.append(pi[proximo])
         

    edges = []
    for key, value in pi.items():
        temp = (key,value)
        if value != None:
            edges.append(temp)
    return edges 


def print_graph(graph,labels,edges=None,weights='red',layout=0):
    if not edges:
        edges = graph.edges()
    if layout == 0:
        pos = nx.circular_layout(G)
    else:
        pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, node_color='white', 
            node_size=50,
            labels=labels,width=1.0,
            edgelist=edges,
            edge_color=weights,
            font_size=9,
            edge_cmap=plt.cm.coolwarm,
            font_color="black",
            font_weight='bold')
    plt.show()


file_to_load = 'ha30_dist.txt'
file_with_labels = 'ha30_name.txt'
A = np.loadtxt(file_to_load)
G = nx.from_numpy_matrix(A)
initial_node = 0

labels = load_labels(file_with_labels)
edges, weights = init(G)
print_graph(G,labels,edges,weights)
edges = prim(G,initial_node)
print("A árvore geradora mínima por Prim começando em:"+str(initial_node))
print(edges)
print_graph(G,labels,edges,layout=1)
