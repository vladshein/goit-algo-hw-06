#Homework6 task3
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

#додати ребра між станціями гілок 
for item in range(0,len(red_line) - 1):
    G.add_edge(red_line[item], red_line[item+1], weight=2)

for item in range(0,len(green_line) - 1):
    G.add_edge(green_line[item], green_line[item+1], weight=3)

for item in range(0,len(blue_line) - 1):
    G.add_edge(blue_line[item], blue_line[item+1], weight=2)

#додати переходи між станціями 
G.add_edge("Teatralna", "Zoloti Vorota", weight=1) 
G.add_edge("Khreshchatyk", "Maidan Nezalezhnosti", weight=1)
G.add_edge("Palats Sportu", "Ploshcha Ukrainskykh Heroiv", weight=1)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", font_size=10, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

shortest_paths = nx.single_source_dijkstra_path(G, source='Akademmistechko')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Akademmistechko')
print("=================================")
print(shortest_paths)
print("=================================")
print(shortest_path_lengths)
print("=================================")
plt.show()