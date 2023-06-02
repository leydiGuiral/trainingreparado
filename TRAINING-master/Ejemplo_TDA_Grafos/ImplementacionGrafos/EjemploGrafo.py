import networkx as nx
import matplotlib.pyplot as plt
from TDA2 import Grafo

# Crear un grafo y agregar algunos nodos y aristas
g = Grafo()
g.agregar_nodo('A')
g.agregar_nodo('B')
g.agregar_nodo('C')
g.agregar_nodo('D')
g.agregar_arista('A', 'B', 4)
g.agregar_arista('B', 'C', 5)
g.agregar_arista('A', 'C', 2)
g.agregar_arista('A', 'D', 2)
g.agregar_arista('C', 'D', 3)
g.agregar_arista('A', 'A', 5)

# Crear un grafo de networkx a partir del grafo de nuestra clase Grafo  
    
g_nx = nx.Graph()
g_nx.add_nodes_from(g.nodos())
for inicio, fin, peso in g.aristas_con_pesos():
    g_nx.add_edge(inicio, fin, weight=peso)

# Dibujar el grafo con networkx y matplotlib.pyplot
pos = nx.spring_layout(g_nx)  # necesitamos usar spring_layout para que las aristas se dibujen espaciadas adecuadamente
nx.draw(g_nx, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=800, font_size=20, font_family='monospace')

# agregar etiquetas de peso de las aristas (opcional)
labels = nx.get_edge_attributes(g_nx, 'weight')
nx.draw_networkx_edge_labels(g_nx, pos, edge_labels=labels, font_size=20)

plt.show()
