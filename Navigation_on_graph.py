import networkx as nx
import matplotlib.pyplot as plt
import random
random.seed(0)
# random navigation can be used in imitation of livilg animal for finging food or water
data = {'A' : ['B','H'],
        'B': ['A','C'],
        'C': ['B', 'D'],
        'D' : ['C','E'],
        'E': ['D','F','G'],
        'F': ['E','A'],
        'G' : ['E','H'],
        'H': ['G','A']}

graph = nx.DiGraph(data) # oriented graph

print(nx.shortest_path_length(graph,'A'))

paths = nx.all_simple_paths(graph,'A','F')
path_list = []
for path in paths:
    path_list.append(path)
    print('Direction-candidate:',path)

sel_path = random.randint(0,len(path_list)-1)
print("Chosen path is: %s" %path_list[sel_path])


pos = nx.spring_layout(graph)
nx.draw_networkx_labels(graph,pos)
nx.draw_networkx_edges(graph,pos)
nx.draw_networkx_nodes(graph,pos)
plt.show()
