import networkx as nx 
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from(["Alcalá","Barranquilla","Cartagena","Darien","El banco","Florida"])

grafo.add_edges_from([
    ("Barranquilla","Cartagena"),
    ("Cartagena","El banco"),
    ("Alcalá","Darien"),
    ("El banco","Alcalá"),
    ("Alcalá","Florida"),
    ("Florida","Darien")
])

# print(nx.adjacency_matrix(grafo))
# print(nx.adjacency_matrix(grafo).todense())
# print(nx.incidence_matrix(grafo).todense())
nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True,node_size=1000)
plt.show()

e = ("Barranquilla","Darien")

grafo.add_edge(*e)

nx.draw(grafo, pos=nx.spring_layout(grafo), with_labels=True,node_size=1000)
plt.show()