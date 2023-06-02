
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz

    def buscar_nodo(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.valor == valor:
            return nodo

        for hijo in nodo.hijos:
            nodo_encontrado = self.buscar_nodo(valor, hijo)
            if nodo_encontrado is not None:
                return nodo_encontrado

        return None

    def agregar_nodo(self, valor, padre):
        hijo = Nodo(valor)
        padre.agregar_hijo(hijo)

    def eliminar_nodo(self, nodo):
        if nodo.padre is None:
            self.raiz = None
        else:
            nodo.padre.hijos.remove(nodo)
            
def dfs_preorden(nodo):
    visitados = [nodo]
    for hijo in nodo.hijos:
        visitados.extend(dfs_preorden(hijo))
    return visitados

def mostrar_arbol(arbol):
    
    def mostrar_nodo(nodo, nivel):
        st.write("  "*nivel + f"{nodo.valor}")
        for hijo in nodo.hijos:
            mostrar_nodo(hijo, nivel+1)
   
    mostrar_nodo(arbol.raiz, 0)

# mostrar arbol ordenado con networkx
def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx, pos=pos,
                                     parent=root, parsed=parsed)
        return pos

    if root is None:
        root = next(iter(G))
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def mostrar_arbol_con_networkx(arbol):
    G = nx.DiGraph()
    for nodo in dfs_preorden(arbol.raiz):
        G.add_node(nodo.valor)
        if nodo.padre is not None:
            G.add_edge(nodo.padre.valor, nodo.valor)
    pos = hierarchy_pos(G)
    
    fig, ax = plt.subplots()
    nx.draw_networkx(G, pos, with_labels=True, arrows=True, ax=ax)
    return fig

