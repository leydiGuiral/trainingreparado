class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.color = "ROJO"  # Por defecto, el nuevo nodo se coloca como rojo
        self.padre = None
        self.izquierdo = None
        self.derecho = None

class ArbolRojoNegro:
    def _init_(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            self.raiz.color = "NEGRO"
        else:
            nodo_actual = self.raiz
            padre_actual = None
            while nodo_actual is not None:
                padre_actual = nodo_actual
                if dato < nodo_actual.dato:
                    nodo_actual = nodo_actual.izquierdo
                else:
                    nodo_actual = nodo_actual.derecho

            nuevo_nodo.padre = padre_actual

            if dato < padre_actual.dato:
                padre_actual.izquierdo = nuevo_nodo
            else:
                padre_actual.derecho = nuevo_nodo

            self.__balancear(nuevo_nodo)

    def __balancear(self, nodo):
        while nodo.padre is not None and nodo.padre.color == "ROJO":
            if nodo.padre == nodo.padre.padre.izquierdo:
                nodo_tio = nodo.padre.padre.derecho

                if nodo_tio is not None and nodo_tio.color == "ROJO":
                    nodo.padre.color = "NEGRO"
                    nodo_tio.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecho:
                        nodo = nodo.padre
                        self.__rotar_izquierda(nodo)

                    nodo.padre.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"
                    self.__rotar_derecha(nodo.padre.padre)
            else:
                nodo_tio = nodo.padre.padre.izquierdo

                if nodo_tio is not None and nodo_tio.color == "ROJO":
                    nodo.padre.color = "NEGRO"
                    nodo_tio.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierdo:
                        nodo = nodo.padre
                        self.__rotar_derecha(nodo)

                    nodo.padre.color = "NEGRO"
                    nodo.padre.padre.color = "ROJO"
                    self.__rotar_izquierda(nodo.padre.padre)

        self.raiz.color = "NEGRO"

    def __rotar_izquierda(self, nodo):
        nodo_derecho = nodo.derecho
        nodo.derecho = nodo_derecho.izquierdo

        if nodo_derecho.izquierdo is not None:
            nodo_derecho.izquierdo.padre = nodo

        nodo_derecho.padre = nodo.padre

        if nodo.padre is None:
            self.raiz = nodo_derecho
        elif nodo == nodo.padre.izquierdo:
            nodo.padre.izquierdo = nodo_derecho
        else:
            nodo.padre.derecho = nodo_derecho
        nodo_derecho.izquierdo

    def __rotar_derecha(self, nodo):
        nodo_izquierdo = nodo.izquierdo
        nodo.izquierdo = nodo_izquierdo.derecho

        if nodo_izquierdo.derecho is not None:
            nodo_izquierdo.derecho.padre = nodo

        nodo_izquierdo.padre = nodo.padre

        if nodo.padre is None:
            self.raiz = nodo_izquierdo
        elif nodo == nodo.padre.izquierdo:
            nodo.padre.izquierdo = nodo_izquierdo
        else:
            nodo.padre.derecho = nodo_izquierdo

        nodo_izquierdo.derecho = nodo
        nodo.padre = nodo_izquierdo

        if nodo_izquierdo.padre is not None:
            if nodo_izquierdo.padre.izquierdo == nodo:
                nodo_izquierdo.padre.izquierdo = nodo_izquierdo
            else:
                nodo_izquierdo.padre.derecho = nodo_izquierdo

    def eliminar(self, dato):
        nodo = self.buscar_nodo(self.raiz, dato)  # Buscar el nodo con el dato proporcionado
        if nodo is None:
            return False  # El nodo no existe en el árbol, no hay nada que eliminar

        # Encontrar el sucesor del nodo a eliminar (el nodo más pequeño en el subárbol derecho)
        if nodo.izquierdo is not None and nodo.derecho is not None:
            sucesor = self.minimo(nodo.derecho)
            nodo.dato = sucesor.dato  # Reemplazar el dato del nodo con el sucesor
            nodo = sucesor  # El nodo a eliminar ahora es el sucesor

        # El nodo a eliminar tiene a lo sumo un hijo
        hijo = nodo.izquierdo if nodo.izquierdo is not None else nodo.derecho

        if hijo is not None:
            hijo.padre = nodo.padre  # Actualizar el padre del hijo

        if nodo.padre is None:
            self.raiz = hijo  # El nodo a eliminar es la raíz del árbol
        elif nodo == nodo.padre.izquierdo:
            nodo.padre.izquierdo = hijo  # El nodo a eliminar es el hijo izquierdo de su padre
        else:
            nodo.padre.derecho = hijo  # El nodo a eliminar es el hijo derecho de su padre

    def buscar_nodo(self, nodo_actual, dato):  # Método buscar_nodo recursivo
        if nodo_actual is None or dato == nodo_actual.dato:
            return nodo_actual

        if dato < nodo_actual.dato:
            return self.buscar_nodo(nodo_actual.izquierdo, dato)
        else:
            return self.buscar_nodo(nodo_actual.derecho, dato)

    def imprimir_inorden(self):
        self.__imprimir_inorden_recursivo(self.raiz)

    def __imprimir_inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__imprimir_inorden_recursivo(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self.__imprimir_inorden_recursivo(nodo.derecho)

    def altura(self):
        return self.__altura_recursiva(self.raiz)

    def __altura_recursiva(self, nodo):
        if nodo is None:
            return 0

        altura_izquierda = self.__altura_recursiva(nodo.izquierdo)
        altura_derecha = self.__altura_recursiva(nodo.derecho)

        return max(altura_izquierda, altura_derecha) + 1