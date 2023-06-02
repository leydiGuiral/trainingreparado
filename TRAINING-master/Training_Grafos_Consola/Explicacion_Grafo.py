from Colores import color

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
    "1": "¿Qué es un Grafo?",
    "2": "¿De que esta compuesto un Grafo?",
    "3": "¿Qué es la etiqueta (peso) de una arista?",
    "4": "Mostrar grafo",
    "5": "¿Qué es un camino",
    "6": "¿Qué es la longitud de un camino?",
    "7": "¿Para que se usan?",
    "8": "Volver al menú principal"
}

# Funcion para mostrar informacion sobre un grafo
def mostrar_info_grafo():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" Un Grafo es una manera de representar de manera simbolica problemas o situaciones de la vida cotidiana o temas laborales, se aplica mucho para mejorar las tomas de decisiones.\n\n\n"+color.FIN)
    
# Funcion para mostrar de que esta compuesto un grafo
def partes_grafo():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" Los grafos son estructuras que estan compuestas principalmente por " + color.CIAN + "Vertices y Aristas " + color.FIN + "que conectan entre si a los Vertices. Los nodos se ven en forma de un circulo => " + color.AZUL + "O" + color.FIN + " Y las Aristas como una linea => " + color.AZUL + " _______ " + color.FIN + "\n" 
          + color.CIAN + "\n    * Vertice: " + color.FIN + "Los Vertices son los puntos de referencia que se definen segun la necesidad; por ejemplo tener un Vertice llamado Cali, otro vertice llamado Bogota, etc...\n" 
          + color.CIAN + "\n    * Aristas: " + color.FIN + "Las Aristas son las responsables de conectar los vertices entre si; continuando con el ejemplo anterior, podemos agragar una Arista, que concectara el Vertice Cali al Vertices Bogota; esta arista puede ser considerada el camino que se recorre para ir desde Cali a Bogota\n\n\n"+color.FIN)
  
# Funcion para mostrar que es la etiqueta (peso) de una arista
def mostrar_info_peso():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" El peso en un Grafo es una especie de etiqueta que contiene un valor el cual se le asigna a las Aristas, este valor puede representar por ejemplo, tiempos o costos; continuando con el ejemplo de los Vertices Cali y Bogota que se encuentran conectados por una Arista, se le puede asignar un peso a esta (Arista) que podria equivaler al tiempo que se toma en llegar de una ciudad a la otra, o al costo de los peajes.\n\n"+color.FIN)
    
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
  
# Funcion para mostrar que es un camino
def que_es_camino():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" Los caminos son las diferentes formas que podemos obtener para poder ir de un Vertice de origen a un Vertice de destino; por ejemplo, tengo los vertices " + color.MORADO + 
          "Cali, Armenia, Manizales, Ibague y Bogota " + color.FIN + "y se tienen las siguientes Aristas " + color.MORADO + "{Cali-Armenia}, {Cali-Manizales}, {Armenia-Ibague}, {Ibague-Bogota}, {Manizalez-Bogota}" + color.FIN + 
          "\n\nEn este caso quiero ir de Cali a Bogota y tengo 2 caminos para poder ir, que serian: Cali-Armenia-Ibague-Bogota y Cali-Manizalez-Bogota\n\n\n"+color.FIN)

# Funcion para mostrar que es la longitud de un camino
def longitud_camino():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" La longitud de un camino son el numero de aristas en el camino que elija del grafo para ir de un Vertice inicial a uno de destino; continuando con el ejemplo anterior donde queria ir desde Cali a Bogota, se definieron 2 posibles caminos " + color.MORADO + 
          "Cali-Armenia-Ibague-Bogota"+ color.FIN + " y " +color.MORADO+ "Cali-Manizalez-Bogota" + color.FIN + "\n\nPara el caso del primer camino se tiene que su longitud es de 3 y para el segundo camino se tiene que su longitud es de 2; por ende si se quiere tomar el primer camino estaria pasando por 3 ciudades sin contar la ciudad de destino, pero si tomo el segundo camino unicamente pasaria por 2 ciudades.\n\n\n"+color.FIN)
   
#  Funcion para mostrar informacion de para que se usan los grafoss
def mostrar_uso():
    print(color.NEGRITA+"\n\n\n"+color.ROJO+"°"+color.FIN+" Los grafos son usados para resolver problemas en muchos campos, en el campo de la ingeniería pueden ser utilizados para establecer si dos computadoras están conectadas oír un enlace de comunicación entre las de las de redes de computadoras\n\n\n"+color.FIN)

# # Función para mostrar información sobre un peso
# def info_peso():
#     pesos = {}
#     for u, v, data in G.edges(data=True):
#         if 'weight' in data:
#             pesos[(u, v)] = data['weight']
#     print(color.NEGRITA+"Un peso es un valor numérico asociado a una arista en un grafo. En este grafo, los pesos de las aristas son:", pesos)
    
    
    
# Funcion del menu
def explicacion():
    # Bucle principal del programa
    while True:
        # Mostramos el menú
        print(color.VERDE+"\n--Bienvenido al training de Grafos--"+color.FIN)
        print(color.SUBRAYAR+"\nEn este capitulo tendras un breve capitulo en el cual aprenderas lo necesario sobre grafos."+color.FIN)
        print("\n")
        for opcion, descripcion in menu.items():
            print(opcion, "-", descripcion)
        opcion = input("\nSelecciona una opción:")

        # Ejecutamos la opción seleccionada
        if opcion == "1":
            mostrar_info_grafo()
        elif opcion == "2":
            partes_grafo()
        elif opcion == "3":
            mostrar_info_peso()
        elif opcion == "4":
            mostrar_grafo()
        elif opcion == "5":
            que_es_camino()
        elif opcion == "6":
            longitud_camino()
        elif opcion == "7":
            mostrar_uso()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción inválida, por favor selecciona otra.")