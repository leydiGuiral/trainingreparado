import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from TrainingArboles.TDA_Arbol import Arbol, Nodo, dfs_preorden, mostrar_arbol, mostrar_arbol_con_networkx

arbol = Arbol(Nodo("raiz"))

def practica():
    st.title("Seccion de Árboles")
    st.write("Este programa te permitirá conocer las partes de un árbol binario.")
    
    opciones = [
        "Agregar nodo",
        "Eliminar nodo",
        "Buscar nodo",
        "Visualizar árbol",
        "Mostrar partes del árbol",
    ]
    st.sidebar.title("Practica Arboles")
    
    opcion = st.selectbox("Menu", opciones)
    
    if opcion == "Agregar nodo":
        with st.form(key="agregar_nodo_form"):
            valor = st.text_input("Ingrese el valor del nodo:", key="agregar_valor")
            padre_valor = st.text_input("Ingrese el valor del padre (Inicial: raiz):", key="agregar_padre",)
            submit_button = st.form_submit_button("Agregar")
        
        if submit_button:
            if padre_valor == "raiz":
                arbol.agregar_nodo(valor, arbol.raiz)
            else:
                padre = arbol.buscar_nodo(padre_valor)
                if padre is not None:
                    arbol.agregar_nodo(valor, padre)
                else:
                    st.write("El nodo padre no existe")
            
            st.success(f"Nodo '{valor}' agregado con éxito al padre '{padre_valor}' .")
                
    elif opcion == "Eliminar nodo":
        with st.form(key="eliminar_nodo_form"):
            valor = st.text_input("Ingrese el valor del nodo a eliminar:", key="eliminar_valor")
            submit_button = st.form_submit_button("Eliminar")
        
        if submit_button:
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                arbol.eliminar_nodo(nodo)
                st.success(f"Nodo '{valor}' eliminado con éxito.")
            else:
                st.write("El nodo no existe")
                
    elif opcion == "Buscar nodo":
        with st.form(key="buscar_nodo_form"):
            valor = st.text_input("Ingrese el valor del nodo a buscar:", key="buscar_valor")
            submit_button = st.form_submit_button("Buscar")
        
        if submit_button:
            nodo = arbol.buscar_nodo(valor)
            if nodo is not None:
                st.write("Nodo encontrado")
            else:
                st.write("Nodo no encontrado")
                
    elif opcion == "Visualizar árbol":
        fig = mostrar_arbol_con_networkx(arbol)
        st.pyplot(fig)
        
    elif opcion == "Mostrar partes del árbol":
        mostrar_arbol(arbol)
