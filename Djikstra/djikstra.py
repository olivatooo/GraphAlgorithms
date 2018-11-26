#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from heapq import heappush,heappop

"""
    Aresta (u,v)
    Peso = w
    λ(u) = Custo de sair da origem até u
    π(u) = Antecessor de u
"""

def djikstra(graph,initial):
    pi = {}
    lam = {}
    pq = []
    w = nx.get_edge_attributes(graph,'weight')

    # Iniciando lambda, pi e a priority queue
    for i in list(graph):
        pi[i] = None
        if i in initial:
            lam[i] = 0
            heappush(pq,(0,i))
        else:
            lam[i] = inf
            heappush(pq,(inf,i))
    while pq:
        p = heappop(pq)[1]
        for i in list(graph.adj[p]):
            try:
                peso = int(w[(p,i)]) + int(lam[p])
            except KeyError:
                peso = int(w[(i,p)]) + int(lam[p])
            if(peso < lam[i]):
                pi[i] = p
                lam[i] = peso
                if i in pq:
                    pq[i] = peso
    edges = []
    for key, value in pi.items():
        temp = (key,value)
        if value != None:
            edges.append(temp)

    return edges, lam
    


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
         

def print_graph(graph,edges,weights,labels):
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, node_color='white', 
            edgelist=edges,
            node_size=50,
            edge_color=weights,
            labels=labels,width=1.0, 
            edge_cmap=plt.cm.coolwarm,
            font_size=9,
            font_color="black",
            font_weight='bold')
    plt.show()


def print_tree(graph,edges,labels):
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, node_color='grey', 
            edgelist=edges,
            node_size=50,
            labels=labels,width=1.0,
            edge_color='red', 
            font_size=9,
            font_color="black",
            font_weight='bold')
    plt.show()


file_to_load = 'wg59_dist.txt'
file_with_labels = 'wg59_name.txt'
A = np.loadtxt(file_to_load)
G = nx.from_numpy_matrix(A)

# Lista de nodes iniciais
nodes_iniciais = [0,1,25,27,4]

edges, weights = init(G)
labels = load_labels(file_with_labels)
print("Grafo do arquivo:"+file_to_load)
print_graph(G,edges,weights,labels)

edges, lam = djikstra(G,nodes_iniciais)
print("Árvore de caminhos mínimos (pi):")
print(edges)
print("Menor caminho até (lambda):")
print(lam)
print_tree(G,edges,labels)
