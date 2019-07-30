import networkx as nx
import matplotlib.pyplot as plt


graph = nx.karate_club_graph() # Graph about some karate club
# Searching and finding all cliques less than 4
cliques = nx.find_cliques(graph)
print('Cliques size less than 4 : %s' %[c for c in cliques if len(c) >= 4])

# Uniting cliques into communities
#communities = nx.k_clique_communities(graph,k=4)
#communities_list = [list(c) for c in communities]
#nodes_list = [node for community in communities_list for node in communities]
#print('Finding next communities :%s' % communities_list)
# Conclusing
#subgraph = graph.subgraph(nodes_list)

pos = nx.spring_layout(graph) # Для построений графа воспользуемся силовым алгоритмом Фрюхтена-Рейгольда
nx.draw(graph,pos=pos,with_labels=True)
plt.show()

