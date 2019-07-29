import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# traversal graph
# There are a lot of algorithms for traversing graphs
graph = { 'A' : ['B','C'], # our graph
          'B' : ['A','C','D'],
          'C' : ['A','B','D','E'],
          'D' : ['B', 'C', 'E', 'F'],
          'E' : ['C', 'D', 'F'],
          'F' : ['D' , 'E']}

Graph  = nx.Graph() # creating networkx graph
for node in graph: # adding nodes and edges here
    Graph.add_nodes_from(node)
    for edge in graph[node]:
        Graph.add_edge(node,edge)

pos = { 'A' : [0.00 , 0.50 ], 'B' : [0.25,0.75],
        'C' : [0.25,0.25], 'D' : [0.75, 0.75],
        'E' : [0.75, 0.25], 'F' : [1.00, 0.50]} # Nodes positions on picture ( First number - x,second number - y

nx.draw(Graph,pos,with_labels=True) # draw graph
nx.draw_networkx(Graph,pos)
plt.show()
# This part for BFS - breadth-first search

def bfs(graph,start):
    queue = [start]
    queued = list()
    path = list()
    while queue:
        #print ('Обработка %s' %vertex)
        vertex = queue.pop(0)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queued.append(candidate)
                queue.append(candidate)
                path.append(vertex+'>'+candidate)
                print('Добавление %s в очередь ' % candidate)
    return path

steps = bfs(graph,'A')
print('\nBFS:',steps)

# depth-first search
def dfs(graph,start):
    stack = [start]
    parents = {start : start}
    path = list()
    while stack:
        print('Стек содержит :%s' %stack)
        vertex = stack.pop(-1)
        print('Обработка %s' %vertex)
        for candidate in graph[vertex]:
            if candidate not in parents:
                parents[candidate] = vertex
                stack.append(candidate)
                print('Добавление %s в стек ' % candidate )
        path.append(parents[vertex] + '>' + vertex)
    return path
steps_2 = dfs(graph,'A')
print('\nDFS:',steps)
