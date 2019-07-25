import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc




somegraph = nx.Graph()
rand_graph = nx.dense_gnm_random_graph(4,3)
Nodes = range(1,5)

Edges = [(1,2),(1,3),(2,3),(3,4),(4,5),(1,5)] # Один способ представления графа

somegraph.add_nodes_from(Nodes)
somegraph.add_edges_from(Edges) # Добавляем элементы в граф
somegraph.add_edge(1,6)
somegraph.add_node(6)

print(sorted(nx.connected_components(somegraph))) # Связь компонентов
print(nx.degree(somegraph))
print(nx.clustering(somegraph)) # Важность узла в целов в графе
print(nx.degree_centrality(somegraph)) # Ценность
print(nx.betweenness_centrality(somegraph)) # Ценность каждой вершины

dictsome = nx.to_dict_of_lists(somegraph) # Различные ввиды представления данных графа
print(dictsome)
matrixgraph = nx.to_numpy_matrix(somegraph) # numpy matrix and there is another numpy type could be - array
print(matrixgraph)
scipygraph = nx.to_scipy_sparse_matrix(somegraph) # Разряженная матрица
print(scipygraph)

nx.draw(somegraph)
plt.show()






