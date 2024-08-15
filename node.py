import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')

G.add_edge('a', 'b', weight = 4)
G.add_edge('b', 'd', weight = 2)
G.add_edge('c', 'd', weight = 4)
G.add_edge('c', 'a', weight = 3)

nx.draw(G)
plt.show()
