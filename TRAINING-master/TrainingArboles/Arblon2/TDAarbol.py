from graphviz import Digraph

class NodoArbol:
    def _init_(self, val):
        self.val = val
        self.padre = None
        self.hijos = []

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def encontrar_nodo(self, val):
        if self.val == val:
            return self
        for hijo in self.hijos:
            nodo = hijo.encontrar_nodo(val)
            if nodo:
                return nodo
        return None

    def encontrar_hojas(self):
        if not self.hijos:
            return [self.val]
        else:
            hojas = []
            for hijo in self.hijos:
                hojas += hijo.encontrar_hojas()
            return hojas

    def _repr_(self, nivel=0):
        ret = "\t" * nivel + repr(self.val) + "\n"
        for hijo in self.hijos:
            ret += hijo._repr_(nivel + 1)
        return ret

class Arbol:
    def _init_(self, valor_raiz):
        self.raiz = NodoArbol(valor_raiz)

    def agregar_nodo(self, val, val_padre):
        nodo_padre = self.raiz.encontrar_nodo(val_padre)
        if nodo_padre:
            nuevo_nodo = NodoArbol(val)
            nodo_padre.agregar_hijo(nuevo_nodo)
        else:
            raise ValueError("valor del padre no encontrado")

    def encontrar_nodo(self, val):
        return self.raiz.encontrar_nodo(val)

    def encontrar_hojas(self):
        return self.raiz.encontrar_hojas()
    
    def graficar(self):
        dot = Digraph(comment='Arbol')
        self._agregar_nodos(dot, self.raiz)
        return dot

    def _agregar_nodos(self, dot, nodo):
        dot.node(str(nodo.val))
        for hijo in nodo.hijos:
            hijo_val = str(hijo.val)
            dot.node(hijo_val)
            dot.edge(str(nodo.val), hijo_val)
            self._agregar_nodos(dot, hijo)

    def _repr_(self):
        return self.raiz._repr_()