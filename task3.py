"""task3.py"""
import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Список вершин (зірок) і їх позицій
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
    "Планета X": (7, 2),
}

# Додавання вершин до графа з координатами
for star, pos in stars.items():
    G.add_node(star, pos=pos)

# Ребра між вершинами (зв'язки між зірками) з вагами
edges_with_weights = [
    ("Сонце", "Альфа Центавра", 5),
    ("Альфа Центавра", "Вега", 2),
    ("Вега", "Проціон", 6),
    ("Проціон", "Сонце", 7),
    ("Сонце", "Сіріус", 3),
    ("Сіріус", "Ріґель", 4),
    ("Ріґель", "Альдебаран", 8),
    ("Альдебаран", "Бетельгейзе", 10),
    ("Сонце", "Планета X", 9),
    ("Планета X", "Альдебаран", 3),
    ("Сонце", "Капела", 2),
    ("Капела", "Бетельгейзе", 4),
]

# Додавання ребер з вагами до графа
G.add_weighted_edges_from(edges_with_weights)

# Виконання алгоритму Дейкстри для знаходження найкоротших шляхів від "Сонце" до усіх інших вершин
shortest_paths = {}
for node in G.nodes:
    if node != "Сонце":  # Пропускаємо, бо шукаємо від "Сонце" до інших
        length, path = nx.single_source_dijkstra(G, "Сонце", node)
        shortest_paths[node] = (length, path)

# Виведення результатів
print("Найкоротші шляхи від 'Сонце' до інших вершин:")
for target, (length, path) in shortest_paths.items():
    print(f"Шлях від 'Сонце' до {target}: {path} з довжиною {length}")

# Візуалізація графа з вагою ребер
pos = nx.get_node_attributes(G, "pos")
plt.figure(figsize=(8, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="yellow",
    edge_color="cyan",
    node_size=1200,
    font_size=10,
    font_color="black",
)

# Показ ваги ребер на графі
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Назва графіка
plt.title("Модель зоряної мережі з вагами на ребрах", fontsize=14, color="black")
plt.gca().set_facecolor("black")
plt.show()
