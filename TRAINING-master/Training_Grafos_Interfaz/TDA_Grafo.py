class Grafo:
    def _init_(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def eliminar_vertice(self, vertice):
        if vertice in self.vertices:
            del self.vertices[vertice]
            # Eliminar aristas conectadas al vértice
            self.eliminar_aristas_conectadas(vertice)

    def agregar_arista(self, vertice_origen, vertice_destino, peso=1):
        if vertice_origen in self.vertices and vertice_destino in self.vertices:
            self.aristas[(vertice_origen, vertice_destino)] = peso
            self.aristas[(vertice_destino, vertice_origen)] = peso

    def eliminar_arista(self, vertice_origen, vertice_destino):
        if (vertice_origen, vertice_destino) in self.aristas:
            del self.aristas[(vertice_origen, vertice_destino)]
            del self.aristas[(vertice_destino, vertice_origen)]

    def eliminar_aristas_conectadas(self, vertice):
        for arista in list(self.aristas):
            if vertice in arista:
                del self.aristas[arista]

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        return self.aristas

    def obtener_peso_arista(self, vertice_origen, vertice_destino):
        return self.aristas.get((vertice_origen, vertice_destino), None)

    def es_conexo(self):
        visitados = set()
        self._dfs(self.vertices.keys()[0], visitados)
        return len(visitados) == len(self.vertices)

    def _dfs(self, vertice, visitados):
        visitados.add(vertice)
        for vecino in self.vertices[vertice]:
            if vecino not in visitados:
                self._dfs(vecino, visitados)
@staticmethod
def exportar_tda_grafo():
    return Grafo()