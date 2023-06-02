import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo vacío
G = nx.Graph()

# Agregamos nodos al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

# Agregamos aristas al grafo con peso
G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=1)
G.add_edge(3, 4, weight=5)
G.add_edge(4, 5, weight=6)


# Definimos una función para mostrar el grafo
def mostrar_grafo():
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Definimos una función para agregar un nodo al grafo
def agregar_nodo():
    nuevo_nodo = int(input("Ingrese el número del nuevo nodo: "))
    G.add_node(nuevo_nodo)
    print(f"Se agregó el nodo {nuevo_nodo} al grafo.")

# Definimos una función para agregar una arista con peso al grafo
def agregar_arista():
    nodo_origen = int(input("Ingrese el número del nodo de origen: "))
    nodo_destino = int(input("Ingrese el número del nodo de destino: "))
    peso = int(input("Ingrese el peso de la arista: "))
    G.add_edge(nodo_origen, nodo_destino, weight=peso)
    print(f"Se agregó la arista ({nodo_origen}, {nodo_destino}) con peso {peso} al grafo.")

# Definimos una función para cambiar el peso de una arista en el grafo
def cambiar_peso_arista():
    nodo_origen = int(input("Ingrese el número del nodo de origen: "))
    nodo_destino = int(input("Ingrese el número del nodo de destino: "))
    peso_nuevo = int(input("Ingrese el nuevo peso de la arista: "))
    if G.has_edge(nodo_origen, nodo_destino):
        G[nodo_origen][nodo_destino]['weight'] = peso_nuevo
        print(f"Se cambió el peso de la arista ({nodo_origen}, {nodo_destino}) a {peso_nuevo}.")
    else:
        print(f"No hay arista entre el nodo {nodo_origen} y el nodo {nodo_destino}.")

# Definimos una función para obtener la distancia entre dos nodos
def obtener_distancia():
    nodo_origen = int(input("Ingrese el número del nodo de origen: "))
    nodo_destino = int(input("Ingrese el número del nodo de destino: "))
    try:
        distancia = nx.dijkstra_path_length(G, nodo_origen, nodo_destino)
        print(f"La distancia entre el nodo {nodo_origen} y el nodo {nodo_destino} es {distancia}.")
    except nx.NetworkXNoPath:
        print(f"No hay camino entre el nodo {nodo_origen} y el nodo {nodo_destino}.")

def practica():
    # Mostramos el grafo inicial
    mostrar_grafo()
    # Definimos el menú interactivo
    while True:
        print("\n--- Diseña tu grafo ---")
        print("--En este capitulo puedes modificar el grafo--")
        print("1. Mostrar grafo")
        print("2. Agregar nodo")
        print("3. Agregar arista")
        print("4. Cambiar peso de una arista")
        print("5. Obtener la menor distancia entre nodos")
        print("6. Salir")
        opcion = int(input("Ingrese la opción deseada: "))
        if opcion == 1:
            mostrar_grafo()
        elif opcion == 2:
            agregar_nodo()
        elif opcion == 3:
            agregar_arista()
        elif opcion == 4:
            cambiar_peso_arista()
        elif opcion == 5:
            obtener_distancia()
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")