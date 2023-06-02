import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from Training_Grafos_Interfaz.TDA_Grafo import exportar_tda_grafo
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
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G, seed=42)  # Especifica una semilla (seed) para las posiciones
    nx.draw_networkx(G, pos, ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    st.pyplot(fig)
    plt.close(fig)


# Definimos una función para agregar un nodo al grafo
def agregar_nodo():
    form = st.form(key="agregar_nodo_form")
    with form:
        nuevo_nodo = st.number_input("Ingrese el número del nuevo nodo:", min_value=1, step=1)
        submit_button = st.form_submit_button(label="Enviar")
    if submit_button:
        G.add_node(nuevo_nodo)
        st.success(f"Se agregó el nodo {nuevo_nodo} al grafo.")

# Definimos una función para agregar una arista con peso al grafo
def agregar_arista():
    form = st.form(key="agregar_arista_form")
    with form:
        peso = st.number_input("Ingrese el peso de la arista:", min_value=0, step=1)
        nodo_origen = st.number_input("Ingrese el número del nodo de origen:", min_value=1, step=1)
        nodo_destino = st.number_input("Ingrese el número del nodo de destino:", min_value=1, step=1)
        submit_button = st.form_submit_button(label="Enviar")
    if submit_button:
        G.add_edge(nodo_origen, nodo_destino, weight=peso)
        st.success(f"Se agregó la arista ({nodo_origen}, {nodo_destino}) con peso {peso} al grafo.")

# Definimos una función para cambiar el peso de una arista en el grafo
def cambiar_peso_arista():
    form = st.form(key="cambiar_peso_arista_form")
    with form:
        nodo_origen = st.number_input("Ingrese el número del nodo de origen:", min_value=1, step=1)
        nodo_destino = st.number_input("Ingrese el número del nodo de destino:", min_value=1, step=1)
        peso_nuevo = st.number_input("Ingrese el nuevo peso de la arista:", min_value=0, step=1)
        submit_button = st.form_submit_button(label="Enviar")
    if submit_button:
        if G.has_edge(nodo_origen, nodo_destino):
            G[nodo_origen][nodo_destino]['weight'] = peso_nuevo
            st.success(f"Se cambió el peso de la arista ({nodo_origen}, {nodo_destino}) a {peso_nuevo}.")
        else:
            st.write(f"No hay arista entre el nodo {nodo_origen} y el nodo {nodo_destino}.")

# Definimos una función para obtener la distancia entre dos nodos
def obtener_distancia():
    form = st.form(key="obtener_distancia_form")
    with form:
        nodo_origen = st.number_input("Ingrese el número del nodo de origen:", min_value=1, step=1)
        nodo_destino = st.number_input("Ingrese el número del nodo de destino:", min_value=1, step=1)
        submit_button = st.form_submit_button(label="Enviar")
    if submit_button:
        try:
            distancia = nx.dijkstra_path_length(G, nodo_origen, nodo_destino)
            st.write(f"La menor distancia entre el nodo {nodo_origen} y el nodo {nodo_destino} es {distancia}.")
        except nx.NetworkXNoPath:
            st.write(f"No hay camino entre el nodo {nodo_origen} y el nodo {nodo_destino}.")

menu = {
    "1": "Mostrar grafo",
    "2": "Agregar nodo",
    "3": "Agregar arista",
    "4": "Cambiar peso de una arista",
    "5": "Obtener la menor distancia entre nodos",
    "6": "Salir"
}

def practica():
    # Mostramos el menú
    st.title("\n--- Diseña tu grafo ---")
    st.subheader("-- En este capítulo puedes modificar el grafo --")
    opciones = list(menu.keys())
    descripcion_opciones = [f"{opcion}: {menu[opcion]}" for opcion in opciones]
    opcion_seleccionada = st.selectbox("Selecciona una opción:", descripcion_opciones, key="menu_opcion_practica_Grafo")

    # Obtener la opción seleccionada sin el número
    opcion = opcion_seleccionada.split(":")[0].strip()

    if opcion == "1":
        mostrar_grafo()
    elif opcion == "2":
        agregar_nodo()
    elif opcion == "3":
        agregar_arista()
    elif opcion == "4":
        cambiar_peso_arista()
    elif opcion == "5":
        obtener_distancia()
    elif opcion == "6":
        st.write("¡Hasta luego!")
