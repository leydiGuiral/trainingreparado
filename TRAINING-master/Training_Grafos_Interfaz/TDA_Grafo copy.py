# from TDA_Cola import Cola, arribo, atencion, cola_vacia, tamaño, en_frente
# from TDA_Pila import Pila, desapilar, pila_vacia, apilar

class nodoArista(object):
    # Clase nodo vertice.
    
    def __init__(self, info, destino):
        #Crea un nodo arista con la informacion cargada
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice(object):
    #clase nodo vertice.
    
    def __init__(self, info):
        #Crea un nodo vertice con la info cargada.
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo(object):
    #clase grafo implementacion lista de listas de adycencia
    def __init__(self, dirigido=True):
        #crea grafo vacio
        self.inicio = None
        self.dirigido = dirigido
        self.tamano = 0
        
class Arista(object):
    #crea lista de aristas implementacion sobre lista.
    def __init__(self):
        self.inicio = None
        self.tamano = 0
        
    ############################
    
def insertar_vertice(grafo, dato): 
    nodo = nodoVertice(dato)
    if(grafo.inicio is None or grafo.inicio.fin > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig =act
        ant.sig =nodo
        grafo.tamano += 1
        
def insertar_arista(grafo, dato, origen, destino):
    agregar_arista(origen.adyacentes, dato, origen.info)
    if(not grafo.dirigido):
        agregar_arista(destino.adyacentes, dato, origen.info)
        
def agregar_arista(origen, dato, destino):
    nodo = nodoArista(dato, destino)
    if(origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig =act
        ant.sig = nodo
    origen.tamano += 1

  ############################            

def eliminar_vertice(grafo, clave):
    x = None
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamano -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig 
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamano -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inico is not None):
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
            
    return x

def buscar_vertice (grafo, buscado):
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_aristas(vertice,buscado):
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux

############################

def tamano(grafo):
#  Devuelve el numero de vertices 
    return grafo.tamano

def grafo_vacio(grafo):
    # devuelve true si el grafo esta vacio
    return grafo.inicio is None

def eliminar_arista(vertice, destino):
    # elimina una arista del vertice y lo devuelve si lo encuentra
    x = None
    if (vertice.inicio.destino == destino):
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamano -= 1
    else:
        ant= vertice.inicio
        act = vertice.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamano -= 1
    return x
    
##################################
  
def existe_paso(grafo, origen, destino):
    resultado = False
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while(vadyacentes is not None and not resultado):
            adyacente = buscar_aristas(grafo, vadyacentes.destino)
            if(adyacente.info == destino.info):
                return True
            elif(not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

def adyacentes(vertice):
    aux = vertice.adyacente.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig

def es_adyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    while( aux is not None and not resultado):
        if(aux.destino == resultado):
            resultado = True
        aux = aux.sig
    return resultado
    

###################################

def marcar_no_visitado(grafo): 
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_vertice(grafo):
    aux =grafo.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig
        
def barrido_profundidad(grafo, vertice):
    if not vertice.visitado:
        vertice.visitado = True
        print(vertice.info)
        adyacentes = vertice.adyacentes.inicio
        while adyacentes is not None:
            adyacente = buscar_vertice(grafo, adyacentes.destino)
            if not adyacente.visitado:
                barrido_profundidad(grafo, adyacente)
            adyacentes = adyacentes.sig
    vertice = vertice.sig
