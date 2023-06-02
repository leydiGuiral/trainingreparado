import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

class Heap(object):
    def __init__(self, tamano):
        self.tamano = 0
        self.vector = [None] * tamano

def agregar(heap, dato):
    heap.vector[heap.heap] = dato
    flotar(heap, heap.tamano)
    heap.tamano += 1

def cantidad_elementos(heap):
    return heap.tamano

def heap_vacio(heap):
    return heap.tamano == 0

def heap_lleno(heap):
    return heap.tamano == len(heap.vector)

def flotar(heap, indice):
    while (indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre

def hundir(heap, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while (control and hijo_izq < heap.tamano):
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if (hijo_der < heap.tamano):
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der

        if (heap.vector[indice] < heap.vector[aux]):
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False

def intercambio(vector, i, j):
    vector[i], vector[j] = vector[j], vector[i]

def monticulizar(heap):
    for i in range(len(heap.vector) // 2, -1, -1):
        hundir(heap, i)

def arribo(heap, dato, prioridad):
    agregar(heap, [prioridad, dato])

def atencion(heap):
    return quitar(heap)

def quitar(heap):
    intercambio(heap.vector, 0, heap.tamano-1)
    dato = heap.vector[heap.tamano-1]
    heap.tamano -= 1
    hundir(heap, 0)
    return dato

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad > prioridad_anterior:
        flotar(heap, indice)
    elif prioridad < prioridad_anterior:
        hundir(heap, indice)

class MonticuloColaPrioridades:
    def __init__(self):
        self.heap = Heap(100)
        self.pacientes_orden_llegada = []

    def insertar(self, prioridad, paciente):
        agregar(self.heap, (prioridad, paciente))
        self.pacientes_orden_llegada.append(paciente)

    def extraer_maximo(self):
        maxima_prioridad, paciente = atencion(self.heap)
        self.pacientes_orden_llegada.remove(paciente)
        return maxima_prioridad, paciente

    def obtener_prioridades(self):
        heap_aux = Heap(len(self.heap.vector))
        vector_aux = []

        # Extraer los elementos del heap original sin eliminarlos
        while not heap_vacio(self.heap):
            prioridad, paciente = self.heap.vector[0]
            vector_aux.append(prioridad)
            agregar(heap_aux, (prioridad, paciente))
            intercambio(self.heap.vector, 0, self.heap.tamano - 1)
            self.heap.tamano -= 1
            hundir(self.heap, 0)

        # Restaurar el heap original
        while not heap_vacio(heap_aux):
            prioridad, paciente = atencion(heap_aux)
            agregar(self.heap, (prioridad, paciente))

        return vector_aux

    def ver_pacientes_orden_llegada(self):
        return self.pacientes_orden_llegada

    def ver_pacientes_por_prioridad(self):
        heap_aux = Heap(len(self.heap.vector))
        pacientes_por_prioridad = []

        # Extraer los elementos del heap original sin eliminarlos
        while not heap_vacio(self.heap):
            prioridad, paciente = atencion(self.heap)
            pacientes_por_prioridad.append(paciente)
            agregar(heap_aux, (prioridad, paciente))

        # Restaurar el heap original
        while not heap_vacio(heap_aux):
            prioridad, paciente = atencion(heap_aux)
            agregar(self.heap, (prioridad, paciente))

        return pacientes_por_prioridad

    def contiene(self, paciente):
        for prioridad, paciente_actual in self.heap.vector[:self.heap.tamano]:
            if paciente_actual[1] == paciente:
                return True
        return False

    def eliminar_paciente(self, paciente):
        for i in range(self.heap.tamano):
            if self.heap.vector[i][1][1] == paciente:
                self.heap.vector[i] = self.heap.vector[self.heap.tamano - 1]
                self.heap.tamano -= 1
                flotar(self.heap, i)
                hundir(self.heap, i)
                return
            
    def reconstruir_monticulo(self):
        pacientes = [(prioridad, paciente) for prioridad, paciente in self.heap.vector[:self.heap.tamano]]
        self.heap.vector = pacientes
        monticulizar(self.heap)
        
def pos_jerarquica(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcentro=0.5):
    pos = {}

    def _pos_jerarquica(G, root, width=1., vert_gap=0.2, vert_loc=0, xcentro=0.5, pos=None, padre=None, analizado=[]):
        if pos is None:
            pos = {root: (xcentro, vert_loc)}
        else:
            pos[root] = (xcentro, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and padre is not None:
            children.remove(padre)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcentro - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _pos_jerarquica(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcentro=nextx, pos=pos,
                                     padre=root, analizado=analizado)
        return pos

    if root is None:
        root = next(iter(G))
    return _pos_jerarquica(G, root, width, vert_gap, vert_loc, xcentro)
