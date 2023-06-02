import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)

    def agregar_arista(self, origen, destino, peso):
        self.grafo.add_edge(origen, destino, weight=peso)

    def obtener_distancia(self, origen, destino):
        try:
            distancia = nx.dijkstra_path_length(self.grafo, origen, destino, weight='weight')
            return distancia
        except nx.NetworkXNoPath:
            return float('inf')

    def obtener_ruta_optima(self, origen, destino):
        try:
            ruta_optima = nx.dijkstra_path(self.grafo, origen, destino, weight='weight')
            return ruta_optima
        except nx.NetworkXNoPath:
            return None
    def eliminar_vertice(self, vertice):
        self.grafo.remove_node(vertice)

    def eliminar_arista(self, origen, destino):
        self.grafo.remove_edge(origen, destino)
        
    def obtener_vertices(self):
        return list(self.grafo.nodes())

def mostrar_grafo():
    fig, ax = plt.subplots()
    pos = nx.circular_layout(empresa.grafo.grafo)    # Especifica una semilla (seed) para las posiciones
    nx.draw_networkx(empresa.grafo.grafo, pos, ax=ax)
    labels = nx.get_edge_attributes(empresa.grafo.grafo, 'weight')
    nx.draw_networkx_edge_labels(empresa.grafo.grafo, pos, edge_labels=labels, ax=ax)
    st.pyplot(fig)
    plt.close(fig)

class EmpresaEmbarcaciones:
    def __init__(self):
        self.grafo = Grafo()

    def agregar_puerto(self, puerto):
        self.grafo.agregar_nodo(puerto)

    def agregar_ruta(self, origen, destino, distancia):
        self.grafo.agregar_arista(origen, destino, distancia)

    def obtener_distancia(self, origen, destino):
        return self.grafo.obtener_distancia(origen, destino)

    def obtener_ruta_optima(self, origen, destino):
        return self.grafo.obtener_ruta_optima(origen, destino)
        
    def eliminar_puerto(self, puerto):
        self.grafo.eliminar_vertice(puerto)
    
    def cambiar_puerto(self, antiguo_puerto, nuevo_puerto):
        if antiguo_puerto in self.grafo.obtener_vertices():
            self.grafo.eliminar_vertice(antiguo_puerto)
            self.grafo.agregar_nodo(nuevo_puerto)
            # Update edges connected to the old port
            for destino in self.grafo.obtener_vertices():
                distancia = self.grafo.obtener_distancia(antiguo_puerto, destino)
                if distancia != float('inf'):
                    self.grafo.agregar_arista(nuevo_puerto, destino, distancia)
            # Update edges connected from the old port
            for origen in self.grafo.obtener_vertices():
                distancia = self.grafo.obtener_distancia(origen, antiguo_puerto)
                if distancia != float('inf'):
                    self.grafo.agregar_arista(origen, nuevo_puerto, distancia)
                    
    def cambiar_ruta(self, origen, destino, nueva_distancia):
        if origen in self.grafo.obtener_vertices() and destino in self.grafo.obtener_vertices():
            self.grafo.eliminar_arista(origen, destino)
            self.grafo.agregar_arista(origen, destino, nueva_distancia)

    def eliminar_ruta(self, origen, destino):
        self.grafo.eliminar_arista(origen, destino)
        
        
# Ejemplo de uso
empresa = EmpresaEmbarcaciones()

empresa.agregar_puerto("Buenaventura")
empresa.agregar_puerto("Cartagena")
empresa.agregar_puerto("Barranquilla")
empresa.agregar_puerto("Santa Marta")
empresa.agregar_puerto("Puerto Bolívar")

empresa.agregar_ruta("Buenaventura", "Cartagena", 500)
empresa.agregar_ruta("Cartagena", "Barranquilla", 200)
empresa.agregar_ruta("Barranquilla", "Santa Marta", 150)
empresa.agregar_ruta("Cartagena", "Santa Marta", 300)
empresa.agregar_ruta("Santa Marta", "Puerto Bolívar", 400)

def agregar_puerto():
    st.subheader("Agregar Puerto")
    puerto = st.text_input("Ingrese el nombre del puerto:")
    if st.button("Agregar"):
        empresa.agregar_puerto(puerto)
        st.success(f"Se agregó el puerto {puerto} al sistema.")

def agregar_ruta():
    st.subheader("Agregar Ruta")
    origen = st.selectbox("Seleccione el puerto de origen:", empresa.grafo.obtener_vertices())
    destino = st.selectbox("Seleccione el puerto de destino:", empresa.grafo.obtener_vertices())
    distancia = st.number_input("Ingrese la distancia entre los puertos:")
    if st.button("Agregar"):
        empresa.agregar_ruta(origen, destino, distancia)
        st.success(f"Se agregó la ruta entre {origen} y {destino} con una distancia de {distancia}.")

def calcular_distancia():
    st.subheader("Calcular Distancia entre Puertos")
    origen = st.selectbox("Seleccione el puerto de origen:", empresa.grafo.obtener_vertices())
    destino = st.selectbox("Seleccione el puerto de destino:", empresa.grafo.obtener_vertices())
    if st.button("Calcular"):
        distancia = empresa.obtener_distancia(origen, destino)
        if distancia != float('inf'):
            st.success(f"La distancia entre {origen} y {destino} es {distancia}.")
        else:
            st.warning(f"No hay ruta disponible entre {origen} y {destino}.")

def calcular_ruta_optima():
    st.subheader("Calcular Ruta Óptima")
    origen = st.selectbox("Seleccione el puerto de origen:", empresa.grafo.obtener_vertices())
    destino = st.selectbox("Seleccione el puerto de destino:", empresa.grafo.obtener_vertices())
    if st.button("Calcular"):
        ruta_optima = empresa.obtener_ruta_optima(origen, destino)
        if ruta_optima:
            distancia = empresa.obtener_distancia(origen, destino)
            st.success(f"La ruta óptima desde {origen} hasta {destino} es: {ruta_optima}")
            st.success(f"Distancia total: {distancia}")
        else:
            st.warning(f"No hay ruta disponible entre {origen} y {destino}.")

def cambiar_puerto():
    st.subheader("Cambiar Puerto")
    antiguo_puerto = st.selectbox("Seleccione el puerto a cambiar:", empresa.grafo.obtener_vertices())
    nuevo_puerto = st.text_input("Ingrese el nuevo nombre del puerto:")
    if st.button("Cambiar"):
        empresa.cambiar_puerto(antiguo_puerto, nuevo_puerto)
        st.success(f"Se cambió el nombre del puerto {antiguo_puerto} por {nuevo_puerto}.")

def cambiar_ruta():
    st.subheader("Cambiar Ruta")
    origen = st.selectbox("Seleccione el puerto de origen de la ruta a cambiar:", empresa.grafo.obtener_vertices())
    destino = st.selectbox("Seleccione el puerto de destino de la ruta a cambiar:", empresa.grafo.obtener_vertices())
    nueva_distancia = st.number_input("Ingrese la nueva distancia entre los puertos:")
    if st.button("Cambiar"):
        empresa.cambiar_ruta(origen, destino, nueva_distancia)
        st.success(f"Se cambió la ruta entre {origen} y {destino} por una distancia de {nueva_distancia}.")

def eliminar_puerto():
    st.subheader("Eliminar Puerto")
    puerto = st.selectbox("Seleccione el puerto a eliminar:", empresa.grafo.obtener_vertices())
    if st.button("Eliminar"):
        empresa.eliminar_puerto(puerto)
        st.success(f"Se eliminó el puerto {puerto} del sistema.")

def eliminar_ruta():
    st.subheader("Eliminar Ruta")
    origen = st.selectbox("Seleccione el puerto de origen de la ruta a eliminar:", empresa.grafo.obtener_vertices())
    destino = st.selectbox("Seleccione el puerto de destino de la ruta a eliminar:", empresa.grafo.obtener_vertices())
    if st.button("Eliminar"):
        empresa.eliminar_ruta(origen, destino)
        st.success(f"Se eliminó la ruta entre {origen} y {destino} del sistema.")

menu = {
    "1": "Mostrar grafo",
    "2": "Agregar puerto",
    "3": "Agregar ruta",
    "4": "Calcular distancia entre puertos",
    "5": "Calcular ruta optima",
    "6": "Cambiar Puerto",
    "7": "Cambiar Ruta",
    "8": "Eliminar Puerto",
    "9": "Eliminar Ruta"
}
def puerto():
    st.title("Empresa de Embarcaciones")
    st.write("\n--- Menú de Empresa de Embarcaciones ---")

    # Mostramos el menú
    opciones = list(menu.keys())
    descripcion_opciones = [f"{opcion}: {menu[opcion]}" for opcion in opciones]
    opcion_seleccionada = st.selectbox("Selecciona una opción:", descripcion_opciones, key="menu_opcion_practica_Grafo")

    # Obtener la opción seleccionada sin el número
    opcion = opcion_seleccionada.split(":")[0].strip()

    if opcion == "1":
        mostrar_grafo()
    elif opcion == "2":
        agregar_puerto()
    elif opcion == "3":
        agregar_ruta()
    elif opcion == "4":
        calcular_distancia()
    elif opcion == "5":
        calcular_ruta_optima()
    elif opcion == "6":
        cambiar_puerto()
    elif opcion == "7":
        cambiar_ruta()
    elif opcion == "8":
        eliminar_puerto()
    elif opcion == "9":
        eliminar_ruta()
    else:
        st.warning("Opción inválida. Ingrese una opción válida.")
