#Homework6 task2
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
    G.add_edge(red_line[item], red_line[item+1])

for item in range(0,len(green_line) - 1):
    G.add_edge(green_line[item], green_line[item+1])

for item in range(0,len(blue_line) - 1):
    G.add_edge(blue_line[item], blue_line[item+1])

#додати переходи між станціями 
G.add_edge("Teatralna", "Zoloti Vorota") 
G.add_edge("Khreshchatyk", "Maidan Nezalezhnosti")
G.add_edge("Palats Sportu", "Ploshcha Ukrainskykh Heroiv")

# DFS
dfs_tree = nx.dfs_tree(G, source='Akademmistechko')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A
print("=================================")
print(list(dfs_tree.nodes()))  # виведе вузли DFS-дерева з коренем у вузлі A
print("=================================")
# BFS
bfs_tree = nx.bfs_tree(G, source='Akademmistechko')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
print("=================================")
print(list(bfs_tree.nodes()))  # виведе вузли BFS-дерева з коренем у вузлі A
print("=================================")