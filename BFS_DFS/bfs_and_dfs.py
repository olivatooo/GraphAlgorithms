"""
    Criado por:
    Gabriel Olivato - 743537
    Igor Raphael Magollo - 743550
    Claudia Sanches - 743521

    PROJETO 3: BUSCA EM LARGURA E PROFUNDIDADE

    Functions:

    bfs_tree(graph,v)
    dfs_tree_with_stack(graph,v)
    edge_in(ed_list,ed)
    highlight_edges(graph,edges)

"""

import queue
import networkx as nx
import matplotlib.pyplot as plt
from random import choice

def bfs_tree(graph,v):
    """ 
        Retorna uma lista de pares de nodes
        que formam uma BFS Tree 

        Keyword arguments:
        graph -- tipo Graph do networkx
        v -- node inicial
    """
    q = queue.Queue()
    visitados = []
    visitados.append(v)
    q.put(v)
    tree = []
    while not q.empty():
        s = q.get()
        for x in list(graph.adj[s]):
            if x not in visitados:
                visitados.append(x)
                q.put(x)
                tree.append( (s,x) )

    return tree


def buscaProfPilha(graph,s):
    """ 
        Retorna uma lista de pares de nodes
        que formam uma BFS Tree 

        Keyword arguments:
        graph -- tipo Graph do networkx
        v -- node inicial
    """
    stack = [s]
    visitados = []
    tree = {}
    while stack:
        removido = stack.pop()
        if removido not in visitados:
            visitados.append(removido)
            for i in list(graph.adj[removido]):
                if i not in visitados:
                    tree[i] = removido
                    stack.append(i)

    dictlist = []
    for key, value in tree.items():
        temp = (key,value)
        dictlist.append(temp)
    return dictlist
    

def edge_in(ed_list,ed):
    """
        Retorna se uma edge está em uma lista de edges
        Ex: (1,3) = (3,1)
        Função usada para colorir corretamente
    """

    ed1 = (ed[1],ed[0])
    if ed1 in ed_list or ed in ed_list:
        return True
    else:
        return False

    

def highlight_edges(graph,edges):
    """
        Retorna uma lista de cores para
        adicionar em `edge_color`

        Keyword arguments:
        graph -- tipo Graph do networkx
        edges -- lista de edges no formato (x,y)
    """
    colors = []
    for e in list(graph.edges()):
        if edge_in(edges,e):
            colors.append('red')
        else:
            colors.append('black')

    return colors

# Lista de arquivos de entrada
entradas = ["karate.paj","dolphins.paj"]

for e in entradas:
    print("")
    print("Processando "+e+"...")
    G = nx.read_pajek(e)
 
    initial_node = choice(list(G))
    print("\nIniciando no node:"+str(initial_node)+"\n")
    my_bfs_tree = bfs_tree(G,initial_node)
    print(my_bfs_tree)

     # Printing BFS
    colors = highlight_edges(G,my_bfs_tree)
    plt.title("BFS de "+e+" iniciando em "+str(initial_node))
    nx.draw(G,with_labels=True,edge_color=colors)
    plt.show()
    print("BFS de "+e)
    print(my_bfs_tree)
 
    # Lista de cores para fazer o desenho bonitinho
    colors = highlight_edges(G,my_bfs_tree)
    # DFS - Tree do NX para poeder "conferir"
    # nx_dfs_tree = nx.dfs_tree(G,source=initial_node).edges()
    my_dfs_tree = buscaProfPilha(G,initial_node)
    print(my_dfs_tree)

    # Printing DFS
    colors = highlight_edges(G,my_dfs_tree)
    plt.title("DFS de "+e+" iniciando em "+str(initial_node))
    nx.draw(G,with_labels=True,edge_color=colors)
    plt.show()
    print("DFS de "+e)
    print(my_dfs_tree)
    print("")
