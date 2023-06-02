class Grafo:
    def __init__(self):
        self.nodos_set = set()
        self.aristas_dic = dict()

    def agregar_nodo(self, valor):
        self.nodos_set.add(valor)
        if valor not in self.aristas_dic:
            self.aristas_dic[valor] = dict()

    def agregar_arista(self, inicio, fin, peso=None):
        self.agregar_nodo(inicio)
        self.agregar_nodo(fin)

        if peso:
            self.aristas_dic[inicio][fin] = peso
            self.aristas_dic[fin][inicio] = peso
        else:
            self.aristas_dic[inicio][fin] = None
            self.aristas_dic[fin][inicio] = None

    def nodos(self):
        return list(self.nodos_set)

    def aristas(self):
        resultado = set()
        for inicio in self.aristas_dic:
            for fin in self.aristas_dic[inicio]:
                resultado.add((inicio, fin))
        return list(resultado)

    def aristas_con_pesos(self):
        resultado = set()
        for inicio in self.aristas_dic:
            for fin in self.aristas_dic[inicio]:
                if self.aristas_dic[inicio][fin] is not None:
                    resultado.add((inicio, fin, self.aristas_dic[inicio][fin]))
        return list(resultado)
    
# En este TDA de Grafo, (grafo no dirigido) estamos utilizando diccionarios. 
# Para implementar este grafo, la clase Grafo contiene los siguientes métodos:

# __init__(self): inicializa el grafo como un conjunto vacío de nodos y un diccionario vacío de aristas.
# agregar_nodo(self, valor): agrega un nodo al grafo con el valor especificado. 
# agregar_arista(self, inicio, fin, peso=None): agrega una arista entre los nodos especificados. Si los nodos no existen, se agregan automáticamente al grafo. 
#                                               Si se asigna un peso, las aristas serán ponderadas (tienen peso), de lo contrario serán no ponderadas (sin peso).
# nodos(self): devuelve una lista de todos los nodos en el grafo.
# aristas(self): devuelve una lista de todas las aristas en el grafo.
# aristas_con_pesos(self): devuelve una lista de todas las aristas ponderadas (que tienen pesos) 