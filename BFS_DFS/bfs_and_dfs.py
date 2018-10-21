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


def dfs_tree_with_stack(graph,v):
    """
        Retorna uma lista de pares de nodes
        que formam uma DFS Tree 

        Keyword arguments:
        graph -- tipo Graph do networkx
        v -- node inicial
    """
    stack = []
    visitados = []
    tree = []
    stack.append(v)
    anterior = ""
    while stack:
        s = stack.pop()
        if s not in visitados:
            if (anterior == ""):
                anterior = s
            else:
                tree.append( (anterior,s) )
                anterior = s
            visitados.append(s)
            for i in list(graph.adj[s]):
                if i not in visitados:
                    stack.append(i)
    return tree


    


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

# Node inicial arbitrario
# Não realizei a checagem para saber se o node existe
initial_node = "3"

for e in entradas:
    print("")
    print("Processando "+e+"...")
    G = nx.read_pajek(e)
    my_bfs_tree = bfs_tree(G,initial_node)
    # BFS - Tree do NX para poder "conferir"
    nx_bfs_tree = nx.bfs_tree(G,source=initial_node).edges()
    # Lista de cores para fazer o desenho bonitinho
    colors = highlight_edges(G,my_bfs_tree)
    # DFS - Tree do NX para poeder "conferir"
    nx_dfs_tree = nx.dfs_tree(G,source=initial_node).edges()

    my_dfs_tree = dfs_tree_with_stack(G,initial_node)
    # Printing BFS
    colors = highlight_edges(G,my_bfs_tree)
    nx.draw(G,with_labels=True,edge_color=colors)
    plt.show()
    print("BFS de "+e)
    print(my_bfs_tree)
    # Printing DFS
    colors = highlight_edges(G,my_dfs_tree)
    nx.draw(G,with_labels=True,edge_color=colors)
    plt.show()
    print("DFS de "+e)
    print(my_dfs_tree)
    print("")
