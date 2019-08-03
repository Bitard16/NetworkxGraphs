import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse
Graph_A = nx.DiGraph()
Graph_B = nx.DiGraph()
Graph_C = nx.DiGraph() # di means oriented

Nodes = range(1,6)
Edges_OK = [(1,2),(1,3),(2,3),(3,1),(3,2),(3,4),(4,5),(4,6),(5,4),(5,6),(6,5),(6,1)]
Edges_dead_end = [(1,2),(1,3),(3,1),(3,2),(3,4),(4,5),(4,6),(5,4),(5,6),(6,5),(6,1)]
Edges_trap = [(1,2),(1,3),(2,3),(3,1),(3,2),(3,4),(4,5),(4,6),(5,4),(5,6),(6,5)]

Graph_A.add_nodes_from(Nodes)
Graph_A.add_edges_from(Edges_OK)

Graph_B.add_nodes_from(Nodes)
Graph_B.add_edges_from(Edges_dead_end)

Graph_C.add_nodes_from(Nodes)
Graph_C.add_edges_from(Edges_trap)


pos = nx.spring_layout(Graph_A)
nx.draw(Graph_A,pos=pos,arrows = True,with_labels=True)
plt.show()

pos = nx.spring_layout(Graph_B)
nx.draw(Graph_B,pos=pos,arrows = True,with_labels=True)
plt.show()

pos = nx.spring_layout(Graph_C)
nx.draw(Graph_C,pos=pos,arrows = True,with_labels=True)
plt.show()

def initialize_PageRank(graph):
    nodes = len(graph)
    M = nx.to_numpy_matrix(graph) # matrix which based on graph nodes and edges
    outbound = np.squeeze(np.asarray(np.sum(M,axis=1))) # squeeze - delete the same pares
    prob_outbound = np.array([1.0/count
                             if count > 0 else 0.0 for count in outbound])
    G = np.asarray(np.multiply(M.T,prob_outbound))
    p = np.ones(nodes)/ float(nodes)
    if np.min(np.sum(G,axis=0)) < 1.0:
        print('Warning : matrix G could be a fake')
    return G,p

G,p = initialize_PageRank(Graph_A)
print(G)

sG = sparse.csr_matrix(G)
print(sG)

G_2,p_2 = initialize_PageRank(Graph_B)
print(p_2)

print(np.dot(G,p))

def PageRank_naive(graph, iters=50):
    G,p = initialize_PageRank(graph)
    for i in range(iters):
        p = np.dot(G,p)
    return  np.round(p,3)

print('---------')
print(PageRank_naive(Graph_A))
print(PageRank_naive(Graph_B))
print(PageRank_naive(Graph_C))


def Pgerank_teleporting(graph,iters = 50,alpha=0.85,rounding=3):
    G,p = initialize_PageRank(graph)
    u = np.ones(len(p) / float(len(p)))
    for i in range(iters):
        p = alpha * np.dot(G,p) + (1.0 - alpha) * u
    return np.round(p/np.sum(p),rounding)

print(nx.pagerank(Graph_A,alpha=0.85))

