#Homework6 task1
"""
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
(наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

Візуалізуйте створений граф, проведіть аналіз основних характеристик 
наприклад, кількість вершин та ребер, ступінь вершин).
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # неорієнтований граф(Київський метрополітен)
G.graph["name"] = "Kyiv Metro"

red_line = ["Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska", 
            "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet",
            "Teatralna", "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark", 
            "Livoberezhna", "Darnytsia", "Chernihivska", "Lisova"]
green_line = ["Syrets", "Dorohozhychi", "Lukianivska", "Zoloti Vorota", "Palats Sportu",
              "Klovska", "Pecherska", "Zvirynetska", "Vydubychi", "Slavutych",
              "Osokorky", "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska",
              "Chervonyi Khutir"]
blue_line = ["Heroiv Dnipra", "Minska", "Obolon", "Pochaina", "Tarasa Shevchenka",
             "Kontraktova Ploshcha", "Poshtova Ploshcha", "Maidan Nezalezhnosti",
             "Ploshcha Ukrainskykh Heroiv", "Olimpiiska", "Palats Ukraina", 
             "Lybidska", "Demiivska", "Holosiivska", "Vasylkivska", 
             "Vystavkovyi Tsentr", "Ipodrom", "Teremky"]
G.add_nodes_from(red_line) # Червона гілка
G.add_nodes_from(green_line) # Зелена гілка
G.add_nodes_from(blue_line) # Синя гілка

print("All Kyiv metro stations:")
print(G.nodes())
print("=================================")
station_count = len(list(G.nodes()))
print(f"Total amount of stations is: {station_count}")
print("=================================")



#додати ребра між станціями гілок 
for item in range(0,len(red_line) - 1):
    G.add_edge(red_line[item], red_line[item+1])

for item in range(0,len(green_line) - 1):
    G.add_edge(green_line[item], green_line[item+1])

for item in range(0,len(blue_line) - 1):
    G.add_edge(blue_line[item], blue_line[item+1])

#додати переходи між станціями 
G.add_edge("Teatralna", "Zoloti Vorota") 
G.add_edge("Khreshchatyk", "Maidan Nezalezhnosti")
G.add_edge("Palats Sportu", "Ploshcha Ukrainskykh Heroiv")

print(f"Is Kyiv metro connected graph: {nx.is_connected(G)}")
print("=================================")

degree_centrality = nx.degree_centrality(G)
print("degree_centrality")
print(degree_centrality)
print("=================================")

betweenness_centrality = nx.betweenness_centrality(G)
print("betweenness_centrality")
print(betweenness_centrality)
print("=================================")

nx.draw(G, with_labels=True)
plt.show()
