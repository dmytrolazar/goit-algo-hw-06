import networkx as nx
import matplotlib.pyplot as plt

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

# DFS
dfs_tree = nx.dfs_tree(G, source='Пасічна', depth_limit=5)
print(f"Шлях від зупинка Пасічна з максимальною глибиною 5 алгоритму DFS: {', '.join(list(dfs_tree.nodes()))}")
nx.draw(dfs_tree, with_labels=True)
plt.show()

# BFS
bfs_tree = nx.bfs_tree(G, source='Пасічна', depth_limit=5)
print(f"Шлях від зупинка Пасічна з максимальною глибиною 5 алгоритму BFS: {', '.join(list(bfs_tree.nodes()))}")
nx.draw(bfs_tree, with_labels=True)
plt.show()

nx.draw(G, with_labels=True)
plt.show()

# алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі між всіма ребрами
nx.set_edge_attributes(G, values = 1, name = 'weight')
length = dict(nx.all_pairs_dijkstra_path_length(G))

