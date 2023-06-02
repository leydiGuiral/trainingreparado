import matplotlib.pyplot as plt
import networkx as nx

# Creamos un grafo vacío
G = nx.Graph()

# Agregamos nodos al grafo
G.add_node(1, label="Nodo 1")
G.add_node(2, label="Nodo 2")
G.add_node(3, label="Nodo 3")

# Agregamos aristas (también llamadas "vértices") al grafo
G.add_edge(1, 2, label="Arista 1-2")
G.add_edge(2, 3, label="Arista 2-3")

# Asignamos pesos a las aristas
G[1][2]['weight'] = 0.5
G[2][3]['weight'] = 1.2

# Creamos el menú
menu = {
    "1": "¿Qué es un nodo?",
    "2": "¿Qué es una arista o vértice?",
    "3": "¿Qué es un peso?",
    "4": "Mostrar grafo",
    "5": "Salir"
}

# Función para mostrar información sobre un nodo
def mostrar_nodo():
    print("Un nodo es un punto en un grafo. En este grafo, los nodos son:", G.nodes())

# Función para mostrar información sobre una arista o vértice
def mostrar_arista_vertice():
    print("Una arista (o vértice) es una conexión entre dos nodos en un grafo. En este grafo, las aristas o vértices son:", G.edges())

# Función para mostrar información sobre un peso
def mostrar_peso():
    pesos = {}
    for u, v, data in G.edges(data=True):
        if 'weight' in data:
            pesos[(u, v)] = data['weight']
    print("Un peso es un valor numérico asociado a una arista en un grafo. En este grafo, los pesos de las aristas son:", pesos)


# Función para mostrar el grafo
def mostrar_grafo():
    # Dibujamos el grafo
    pos = nx.spring_layout(G)

    # Colores de los nodos, aristas y peso
    node_color = 'lightblue'
    edge_color = 'black'
    weight_color = 'red'
    node_label_color = 'white'
    edge_label_color = 'black'

    # Dibujamos los nodos
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=500, label="Nodos")
   
    # Dibujamos las aristas
    nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=2, alpha=0.7, label="Aristas")




    # Etiquetas de los nodos
    node_labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=14, font_color=node_label_color)

    # Etiquetas de las aristas con los pesos
    edge_labels = {(u, v): data['weight'] for u, v, data in G.edges(data=True) if 'weight' in data}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=12, font_color=edge_label_color)


    # Legendas
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)

    # Mostramos el grafo
    plt.axis('off')
    plt.show()
    
# Funcion del menu
def explicacion():
    # Bucle principal del programa
    while True:
        # Mostramos el menú
        print("\n-- Bienvenido al training de Grafos --")
        print("-- En este capitulo tendras un breve capitulo en el cual aprenderas lo necesario sobre grafos --")
        print("\n")
        for opcion, descripcion in menu.items():
            print(opcion, "-", descripcion)
        opcion = input("Selecciona una opción: ")

        # Ejecutamos la opción seleccionada
        if opcion == "1":
            mostrar_nodo()
        elif opcion == "2":
            mostrar_arista_vertice()
        elif opcion == "3":
            mostrar_peso()
        elif opcion == "4":
            mostrar_grafo()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor selecciona otra.")
