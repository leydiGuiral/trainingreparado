
import streamlit as st 
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import networkx as nx
from TrainingArboles.TDA_Arbol import Arbol, Nodo, dfs_preorden,mostrar_arbol_con_networkx
from TrainingArboles.arbol_RojoNegro import arbolRN

# Creamos el árbol
raiz = Nodo("raiz")
nodo1 = Nodo("nodo1")
nodo2 = Nodo("nodo2")
nodo3 = Nodo("nodo3")
nodo4 = Nodo("nodo4")
nodo5 = Nodo("nodo5")

arbol = Arbol(raiz)
arbol.agregar_nodo("nodo1", arbol.raiz)
arbol.agregar_nodo("nodo2", arbol.raiz)
padre = arbol.buscar_nodo("nodo1")
arbol.agregar_nodo("nodo3", padre)
arbol.agregar_nodo("nodo4", padre)
padre = arbol.buscar_nodo("nodo2")
arbol.agregar_nodo("nodo5", padre)

# Creamos el menú
menu = {
    "1": "¿Qué es un Arbol?",
    "2": "¿Qué es un nodo?",
    "3": "¿Qué es una raiz?",
    "4": "¿Qué es una hoja?",
    "5": "¿Qué es un padre?",
    "6": "¿Qué es un hijo?",
    "7": "¿Qué es una rama?",
    "8": "¿Qué es un subárbol?",
    "9": "Arbol Rojo Negro",
    "10": "Arbol Binario lineal",
    "11": "Mostrar árbol"
}

# Funciónes que definen y muestran cada parte de un arbol
def Def_Arbol():
    st.write ("\nEs una estructura jerárquica compuesta por nodos y aristas, donde cada nodo tiene un nodo padre y cero o más nodos hijos.")
    st.write ("Se utilizan ampliamente en ciencias de la computación y programación debido a su capacidad para representar estructuras jerárquicas y relaciones entre elementos.")

def mostrar_nodo():
    st.write("\nUn nodo es un elemento en un árbol, es decir una entidad que contiene información y está conectada a otros nodos, formando así la estructura jerárquica del árbol.")

def mostrar_raiz():
    st.write("\nEs el nodo principal y el nivel superior del árbol. Es el único nodo que no tiene un nodo padre y sirve como punto de partida para acceder a todos los demás nodos del árbol.")

def mostrar_hoja():
    
    st.write("\nUna hoja en un árbol es un nodo final o terminal que no tiene hijos ni ramificaciones adicionales, en este arbol las hojas son:")

def mostrar_padre():
    st.write("\nUn padre es un nodo en un árbol que tiene al menos un hijo. En este árbol los padres son:")

def mostrar_hijo():
    
    st.write("\nUn hijo en un árbol es un nodo cuya escala jerarquica es inferior al nodo que está conectado directamente, el cual se llama nodo padre, en este arbol los hijos son:")

def mostrar_rama():
    st.write("\nUna rama en un árbol es un camino o secuencia de nodos que se extiende desde un nodo padre hasta uno de sus nodos hijos.")
    st.write("Representa una conexión jerárquica y proporciona una ruta para recorrer la estructura del árbol,"+"\n"+ "En este arbol las ramas son:")
    
def mostrar_subarbol():
    st.write("\nUn subárbol es una porción de un árbol más grande que se deriva de un nodo raíz específico y que incluye a ese nodo y a todos sus descendientes.")
    st.write("Es decir que son los posibles caminos a recorrer en un arbol a partir de un punto de partida y destino especificado.")

# Funcion del menú
def explicacion():
    # Mostramos el menú
    opciones = list(menu.keys())
    descripcion_opciones = [f"{opcion}: {menu[opcion]}" for opcion in opciones]
    opcion_seleccionada = st.selectbox("Selecciona una opción:", descripcion_opciones)

    # Obtener la opción seleccionada sin el número
    opcion = opcion_seleccionada.split(":")[0].strip()

    # Ejecutamos la opción seleccionada
    if opcion == "1":
        Def_Arbol()
    elif opcion == "2":
        mostrar_nodo()
    elif opcion == "3":
        mostrar_raiz()
    elif opcion == "4":
        mostrar_hoja()
    elif opcion == "5":
        mostrar_padre()
    elif opcion == "6":
        mostrar_hijo()
    elif opcion == "7":
        mostrar_rama()
    elif opcion == "8":
        mostrar_subarbol()
    elif opcion == "9":
        arbolRN()
    elif opcion == "10":
        st.write("\n es una estructura de datos que consta de nodos enlazados de manera lineal, donde cada nodo tiene un máximo de dos hijos: un hijo izquierdo y un hijo derecho. Cada nodo en el árbol binario lineal se conecta a su hijo izquierdo y/o derecho, formando una secuencia lineal de nodos.")
        st.write(" los subárboles en un árbol binario lineal son porciones del árbol más grande que se derivan de un nodo raíz específico. Representan posibles caminos a recorrer en el árbol y nos permiten analizar y manipular secciones específicas de la estructura de datos.")

    elif opcion == "11":
        fig = mostrar_arbol_con_networkx(arbol)
        st.pyplot(fig)