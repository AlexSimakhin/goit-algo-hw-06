"""task1.py"""
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
    "Планета X": (7, 2)
}

# Додавання вершин до графа з координатами
for star, pos in stars.items():
    G.add_node(star, pos=pos)

# Ребра між вершинами (зв'язки між зірками)
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

# Додавання ребер до графа
G.add_edges_from(edges)

# Отримання позицій для візуалізації
pos = nx.get_node_attributes(G, "pos")

# Побудова графіка
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

# Назва графіка
plt.title("Модель зоряної мережі", fontsize=14, color="black")
plt.gca().set_facecolor("black")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_centrality = nx.degree_centrality(G)

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degree_centrality.items():
    print(f"{node}: {degree:.2f}")
