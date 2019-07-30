import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from heapq import heapify,heappop,heappush

class priority_queue(): # Создаем класс для очереди с приоритетом
    def __init__(self):
        self.queue = list()
        heapify(self.queue)
        self.index = dict()
    def push(self,priority,label):
        if label in self.index:
            self.queue = [(w,l) for w,l in self.queue if l != label ]
            heapify(self.queue)
        heappush(self.queue, (priority, label))
        self.index[label] = priority
    def pop(self):
        if self.queue:
            return heappop(self.queue)
    def __contains__(self, label):
        return label in self.index
    def __len__(self):
        return len(self.queue)


# traversal graph
# There are a lot of algorithms for traversing graphs
graph = { 'A' : {'B':2,'C':3}, # our graph
          'B' : {'A':2,'C':2,'D':2},
          'C' : {'A':3,'B':2,'D':3,'E':2},
          'D' : {'B':2, 'C':3, 'E':1, 'F':3},
          'E' : {'C':2, 'D':1, 'F':1},
          'F' : {'D':3 , 'E':1}}

Graph  = nx.Graph() # creating networkx graph
for node in graph: # adding nodes and edges here
    Graph.add_nodes_from(node)
    for edge,weight in graph[node].items():
        Graph.add_edge(node,edge,weight=weight)

pos = { 'A' : [0.00 , 0.50 ], 'B' : [0.25,0.75],
        'C' : [0.25,0.25], 'D' : [0.75, 0.75],
        'E' : [0.75, 0.25], 'F' : [1.00, 0.50]} # Nodes positions on picture ( First number - x,second number - y

labels = nx.get_edge_attributes(Graph,'weight')

nx.draw(Graph,pos,with_labels=True) # draw graph
nx.draw_networkx_edge_labels(Graph,pos,edge_lbels=labels)
nx.draw_networkx(Graph,pos)
plt.show()

# ПОстроение отстовного дерева используя алгоритм Прима :
# Сравниваем два рбра и выбираем наименьшее для вергины и идем дальше
def prim(graph,start):
    treepath = {}
    total = 0
    queue = priority_queue()
    queue.push(0,(start,start))
    while queue:
        weight, (node_start,node_end) = queue.pop()
        if node_end not in treepath:
            treepath[node_end] = node_start
            if weight:
                print("Добавление ребра из %s" " в %s с весом %i" %(node_start,node_end,weight))
                total += weight
            for next_node,weight in graph[node_end].items():
                queue.push(weight,(node_end,next_node))
    print("Общая длина отстовного дерева : %i" %total)
    return treepath

def represent_tree(treepath):
    progressin = list()
    for node in treepath:
        if node != treepath[node]:
            progressin.append((treepath[node],node))
    return sorted(progressin,key=lambda x:x[0])



treepath = prim(graph,'A')
print(represent_tree(treepath))


def kruskal(graph):
    priority = priority_queue()
    print("Внесение все реьбер в очередь с приоритетами")
    treepath = list()
    connected = dict()
    for node in graph:
        connected[node] = [node]
        for dest,weight in graph[node].items():
            priority.push(weight,(node,dest))
        print("Всего %i ребер " %len(priority))
        print("Связные компоненты :%s" % connected.values())

        total = 0
        while len(treepath) < (len(graph)-1):
            (weight,(start,end)) = priority.pop()
            if end not in connected[start]:
                treepath.append((start,end))
                print("Обьединение компонентов %s and %s:" %(connected[start],connected[end]))
                print("Добавление ребра из %s в %s с весом %i" % (start,end,weight))
                total += weight
                connected[start] += connected[end][:]
                for element in connected[end]:
                    connected[element] = connected[start]
    print("Общая длина :%i" %total )
    return sorted(treepath,key=lambda x:x[0])


def dijkstra(graph,start,end):
    inf = float('inf')
    known = set() # Множество для сохранения путей которые мы просматривали
    priority = priority_queue()
    path = {start: start}
    for vertex in graph: # Проходимся по алгоритму
        if vertex == start:
            priority.push(0,vertex)
        else:
            priority.push(inf, vertex)
    last = start
    while last != end: # Первое не ровняется последнему
        (weight, actual_node) = priority.pop() # Удаляем путь с которым мы работали и который в приоритете
        if actual_node not in known: # Пока путь с которым мы работаем не входит в мно-во лушчего пути
            for next_node in graph[actual_node]: # Прозодимся по след его путям
                upto_actual = priority.index[actual_node] # Мы ставим вначале приоритет на 1 путь
                upto_next = priority.index[next_node] # И берем значения следуйщих путей
                to_next = upto_actual +  graph[actual_node][next_node]# Получаем значения будушего пути
                if to_next < upto_next: # Сравниваем с другим будущим аутем
                    priority.push(to_next,next_node) # Если возможный приоритетные путь лучше то добавляем го
                    path[next_node] = actual_node # Добавляем его в переменную лучшего пути
            last = actual_node # Актуальная вершина становится точкой старта последуйщих обоходов
            known.add(actual_node) # Добавляем в наше множество путей которые мы просматривали
    return priority.index, path








