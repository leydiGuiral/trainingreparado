# from Colores import color

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

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
    "2": "¿De qué está compuesto un Grafo?",
    "3": "¿Qué es la etiqueta (peso) de una arista?",
    "4": "Mostrar grafo",
    "5": "¿Qué es un camino?",
    "6": "¿Qué es la longitud de un camino?",
    "7": "¿Para qué se usan?",
    "8": "Volver al menú principal"
}

# Función para mostrar información sobre un grafo
def mostrar_info_grafo():
    st.write("# ¿Qué es un Grafo?")
    st.write("Un Grafo es una manera de representar de manera simbólica problemas o situaciones de la vida cotidiana o temas laborales, se aplica mucho para mejorar las tomas de decisiones.")

# Función para mostrar de qué está compuesto un grafo
def partes_grafo():
    st.write("# ¿De qué está compuesto un Grafo?")
    st.write("Los grafos son estructuras que están compuestas principalmente por **Vertices** y **Aristas** que conectan entre sí a los Vertices. Los nodos se ven en forma de un circulo (O) y las Aristas como una línea (________).")
    st.write("\n\n* **Vertice**: Los Vertices son los puntos de referencia que se definen según la necesidad; por ejemplo, tener un Vertice llamado Cali, otro Vertice llamado Bogota, etc...")
    st.write("\n\n* **Aristas**: Las Aristas son las responsables de conectar los Vertices entre sí; continuando con el ejemplo anterior, podemos agregar una Arista que conectará el Vertice Cali al Vertice Bogota; esta arista puede ser considerada el camino que se recorre para ir desde Cali a Bogota.")

# Función para mostrar qué es la etiqueta (peso) de una arista
def mostrar_info_peso():
    st.write("# ¿Qué es la etiqueta (peso) de una arista?")
    st.write("El peso en un Grafo es una especie de etiqueta que contiene un valor el cual se le asigna a las Aristas. Este valor puede representar, por ejemplo, tiempos o costos. Continuando con el ejemplo de los Vertices Cali y Bogota que se encuentran conectados por una Arista, se le puede asignar un peso a esta Arista, que podría equivaler al tiempo que se toma en llegar de una ciudad a la otra o al costo de los peajes.")
    
# Función para mostrar qué es un camino
def que_es_camino():
    st.write("# ¿Qué es un camino?")
    st.write("Los caminos son las diferentes formas que podemos obtener para poder ir de un Vertice de origen a un Vertice de destino. Por ejemplo, tenemos los Vertices Cali, Armenia, Manizales, Ibague y Bogota, y se tienen las siguientes Aristas: {Cali-Armenia}, {Cali-Manizales}, {Armenia-Ibague}, {Ibague-Bogota}, {Manizalez-Bogota}.")
    st.write("En este caso, si queremos ir de Cali a Bogota, tenemos 2 caminos posibles: Cali-Armenia-Ibague-Bogota y Cali-Manizalez-Bogota.")

# Función para mostrar qué es la longitud de un camino
def longitud_camino():
    st.write("# ¿Qué es la longitud de un camino?")
    st.write("La longitud de un camino es el número de aristas en el camino que elijamos del grafo para ir de un Vertice inicial a uno de destino. Continuando con el ejemplo anterior donde queríamos ir desde Cali a Bogota, se definieron 2 posibles caminos: Cali-Armenia-Ibague-Bogota y Cali-Manizalez-Bogota.")
    st.write("Para el caso del primer camino, se tiene que su longitud es de 3, y para el segundo camino se tiene que su longitud es de 2. Por ende, si se elige el primer camino, se pasaría por 3 ciudades sin contar la ciudad de destino, pero si se elige el segundo camino, únicamente se pasaría por 2 ciudades.")

# Función para mostrar información sobre el uso de los grafos
def mostrar_uso():
    st.write("# ¿Para qué se usan los grafos?")
    st.write("Los grafos se usan para resolver problemas en muchos campos. En el campo de la ingeniería, pueden ser utilizados para establecer si dos computadoras están conectadas por un enlace de comunicación entre las redes de computadoras.")


# Función para mostrar el grafo
def mostrar_grafo():
    st.write("# Mostrar Grafo")
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

    # Mostramos el grafo
    plt.axis('off')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)
    plt.show()
    
# Funcion del menu
def explicacion():
        # Mostramos el menú
    opciones = list(menu.keys())
    descripcion_opciones = [f"{opcion}: {menu[opcion]}" for opcion in opciones]
    opcion_seleccionada = st.selectbox("Selecciona una opción:", descripcion_opciones)

    # Obtener la opción seleccionada sin el número
    opcion = opcion_seleccionada.split(":")[0].strip()
    
    if opcion == "1":
        mostrar_info_grafo()
    elif opcion == "2":
        partes_grafo()
    elif opcion == "3":
        mostrar_info_peso()
    elif opcion == "4":
        fig = mostrar_grafo()
        st.pyplot(fig)
    elif opcion == "5":
        que_es_camino()
    elif opcion == "6":
        longitud_camino()
    elif opcion == "7":
        mostrar_uso()
    elif opcion == "8":
        st.write("Volver al menú principal")