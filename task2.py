"""task2.py"""
import networkx as nx
from collections import deque

# Змінили структуру графа
G = nx.Graph()
stars = {
    "Сонце": (5, 5),
    "Альфа Центавра": (7, 8),
    "Вега": (3, 10),
    "Сіріус": (8, 3),
    "Проціон": (2, 7),
    "Бетельгейзе": (6, 9),
    "Ріґель": (4, 3),
    "Альдебаран": (9, 6),
    "Капела": (5, 4),
    "Планета X": (7, 2)
}

for star, pos in stars.items():
    G.add_node(star, pos=pos)

# Змінили ребра і додали більше варіантів
edges = [
    ("Сонце", "Альфа Центавра"),
    ("Альфа Центавра", "Вега"),
    ("Вега", "Проціон"),
    ("Проціон", "Сонце"),
    ("Сонце", "Сіріус"),
    ("Сіріус", "Ріґель"),
    ("Ріґель", "Альдебаран"),
    ("Альдебаран", "Бетельгейзе"),
    ("Сонце", "Планета X"),
    ("Планета X", "Альдебаран"),
    ("Сонце", "Капела"),
    ("Капела", "Бетельгейзе")
]
G.add_edges_from(edges)

# Функція пошуку у глибину (DFS)
def dfs_path(graph, start, target):
    visited = set()
    path = []

    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        path.append(node)
        if node == target:
            return True
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        path.pop()
        return False

    dfs(start)
    return path

# Функція пошуку у ширину (BFS)
def bfs_path(graph, start, target):
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        if node == target:
            return path
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
    return []

# Виконання алгоритмів для пошуку шляху
start = "Сонце"
target = "Бетельгейзе"
dfs_result = dfs_path(G, start, target)
bfs_result = bfs_path(G, start, target)

# Порівняння результатів
print("Результат пошуку шляхів:")
print(f"DFS шлях від '{start}' до '{target}': {dfs_result}")
print(f"BFS шлях від '{start}' до '{target}': {bfs_result}")
