import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def dfs_traverse(graph: nx.Graph, start_vertex, depth_limit=math.inf):
    visited = set()
    order = []
    stack = [(start_vertex, 0)]

    while stack:
        vertex, depth = stack.pop()
        if vertex not in visited and depth <= depth_limit:
            order.append(vertex)
            visited.add(vertex)
            stack.extend([(n, depth + 1) for n in set(graph.neighbors(vertex)) - visited])
            
    return order

def bfs_traverse(graph: nx.Graph, start_vertex, depth_limit=math.inf):
    visited = set()
    order = []
    queue = deque()
    queue.append((start_vertex, 0))

    while queue:
        vertex, depth = queue.popleft()
        if vertex not in visited and depth <= depth_limit:
            order.append(vertex)
            visited.add(vertex)
            queue.extend([(n, depth + 1) for n in set(graph.neighbors(vertex)) - visited])

    return order

def dijkstra(graph: nx.Graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start_vertex] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in [(n, graph.get_edge_data(n, current_vertex)['weight']) for n in graph.neighbors(current_vertex)]:
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)

    return distances

G = nx.Graph()

with open('data.txt', 'r', encoding='utf8') as file:
    previous_line = ""
    for line in file:
        line = line.strip()
        if not (line.startswith("трамвай") or line == ""):
            G.add_node(line)
            if previous_line != "":
                G.add_edge(line, previous_line)
            previous_line = line
        else:
            previous_line = ""

print(f"Кількість вершин у графі: {G.number_of_nodes()}.")
print(f"Кількість ребер у графі:  {G.number_of_edges()}.")

print(f"Близькість вузлів у графі в порядку зростання:\n\
{'\n'.join("    {}: {}".format(k, v) for k, v in dict(sorted(nx.closeness_centrality(G).items(), key=lambda item: item[1])).items())}")

print(f"Шлях від зупинка Пасічна з максимальною глибиною 5 алгоритму DFS: {dfs_traverse(G, 'Пасічна', 5)}")
print(f"Шлях від зупинка Пасічна з максимальною глибиною 5 алгоритму BFS: {bfs_traverse(G, 'Пасічна', 5)}")
nx.set_edge_attributes(G, values = 1, name = 'weight')
distances = dijkstra(G, 'Пасічна')
print(f"Результат роботи алгоритму Дейкстри для знаходження найкоротших шляхів між всіма вершинами графа: {distances}")

# nx.draw(G, with_labels=True)
# plt.show()


