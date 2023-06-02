import networkx as nx
import matplotlib.pyplot as plt
from Training_Monticulos.TDA_monticulo import MonticuloColaPrioridades, heap_vacio, atencion,pos_jerarquica
import streamlit as st

import networkx as nx
import matplotlib.pyplot as plt
from Training_Monticulos.TDA_monticulo import MonticuloColaPrioridades, heap_vacio, atencion,pos_jerarquica
import streamlit as st

def mostrar_monticulo_explicacion():
    st.title("Montículo - Cola de Prioridades aplicados en el sector de la salud")

    cola_prioridades = MonticuloColaPrioridades()

    # Agregar nodos por defecto al montículo
    cola_prioridades.insertar(5, "A")
    cola_prioridades.insertar(2, "B")
    cola_prioridades.insertar(8, "C")
    cola_prioridades.insertar(3, "D")

    explicacion = st.selectbox("Seleccione una opción", ["Agregar Elemento", "Extraer Máximo"])

    if explicacion == "Agregar Elemento":
        elemento = st.text_input("Ingrese el elemento a agregar")
        prioridad = st.number_input("Ingrese la prioridad del elemento", value=0)
        cola_prioridades.insertar(prioridad, elemento)

    elif explicacion == "Extraer Máximo":
        maxima_prioridad, elemento = cola_prioridades.extraer_maximo()
        st.write(f"Elemento extraído: {elemento}")
        st.write(f"Prioridad del elemento extraído: {maxima_prioridad}")

    G = nx.DiGraph()
    for i in range(cola_prioridades.heap.tamano):
        prioridad, elemento = cola_prioridades.heap.vector[i]
        G.add_node(elemento)
        if i > 0:
            padre = (i - 1) // 2
            padre_elemento = cola_prioridades.heap.vector[padre][1]
            G.add_edge(padre_elemento, elemento)

    pos = pos_jerarquica(G)
    nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightblue', edge_color='gray', arrows=True)
    plt.title("Montículo - Cola de Prioridades en el sector de la salud")
    plt.axis('off')
    st.pyplot()



# Función para mostrar información sobre un Montículo
def mostrar_info_monticulo():
    st.write("\n\n\nUn montículo es un árbol binario balanceado que cumple con la premisa de que ningún padre tiene un hijo mayor (montículo de máximos) o menor (montículo de mínimos) a él.\n\n\n")

# Función para mostrar las dos clases de montículos
def Tipos_de_monticulos():
    st.write("\n\n\nHay dos tipos principales de montículos: el montículo máximo y el montículo mínimo.\n"
             "\nMontículo Máximo: Un montículo máximo es una estructura de datos basada en un árbol binario completo en la cual el valor almacenado en cada nodo es mayor o igual que los valores almacenados en sus hijos. Esto significa que el elemento más grande siempre se encuentra en la raíz del montículo.\n"
             "\nMontículo Mínimo: Un montículo mínimo es una estructura de datos basada en un árbol binario completo en la cual el valor almacenado en cada nodo es menor o igual que los valores almacenados en sus hijos. Esto significa que el elemento más pequeño siempre se encuentra en la raíz del montículo.\n\n\n")

# Función para mostrar para qué sirven los montículos
def mostrar_para_que_sirve():
    st.write("\n\n\nSus funciones son:\n"
             "\nCola de prioridad: Un montículo se utiliza a menudo como una cola de prioridad, donde los elementos se organizan según su prioridad y se pueden extraer de acuerdo con dicha prioridad. El elemento de mayor prioridad se encuentra en la raíz del montículo. Esto es útil cuando se necesita procesar elementos en un orden específico basado en su importancia o prioridad.\n"
             "\nAlgoritmos de búsqueda y ordenación: Los montículos también se utilizan en algoritmos de búsqueda y ordenación eficientes, como el algoritmo de ordenación heapsort. Los montículos permiten ordenar una colección de elementos de manera eficiente y encontrar rápidamente el elemento mínimo o máximo.\n"
             "\nImplementación de colas de prioridad: Al utilizar montículos, se pueden implementar colas de prioridad eficientes, donde los elementos se insertan y se extraen según su prioridad en tiempo logarítmico. Esto es útil en algoritmos de planificación, sistemas de eventos, algoritmos de búsqueda óptima, entre otros.\n\n\n")

# Función para mostrar información sobre las partes de los montículos
def mostrar_partes_de_los_monticulos():
    st.write("\n\n\nEstas son las partes de la implementación de los montículos:\n"
             "\nFlotar: La acción de flotar se emplea cuando se agrega un elemento nuevo a la estructura. Lo más simple, dado que el montículo se implementa en un vector, es agregar al final del vector el elemento y flotarlo hasta que su peso nos diga que está en el lugar idóneo. Esto hace que el coste del algoritmo sea lineal y, por lo cual, sea óptimo.\n"
             "\nHundir: Sería la contrapartida a flotar. En este caso, lo que se hace es que, si eliminamos la cima del montículo, la acción rápida sería mover el último elemento del vector al principio, cambiar el dimensionamiento del vector y realizar este algoritmo para llevar (o hundir) al elemento a su posición correcta. Igualmente, el algoritmo es lineal.\n"
             "\nInsertar: En este método, insertamos (como bien dijimos en flotar) un elemento en la estructura, por lo que hacemos eso mismo, agregamos el elemento y lo flotamos.\n"
             "\nPrimero: Nos da el primer elemento del montículo (la cima), pero sin eliminarlo de la estructura.\n"
             "\nCima: Igual que el anterior, pero eliminando el elemento de la cima. Para ello, como se comentó en hundir, se toma el último elemento, se inserta en la cima (que queda vacía) y se hunde hacia su posición correcta.\n\n\n")
def cola_prioridades():
    st.write("\nUna cola de prioridades es una estructura de datos en la que los elementos se atienden en el orden indicado por una prioridad asociada a cada uno. Si varios elementos tienen la misma prioridad, se atenderán de modo convencional según la posición que ocupen.")
    st.write("\nUn ejemplo de la vida diaria sería la sala de urgencias de un hospital, ya que los enfermos se van atendiendo en función de la gravedad de su enfermedad.")
    st.write("\nEn el ejemplo explicativo, el montículo representa una cola de prioridades donde los elementos se insertan con una prioridad determinada y se pueden extraer de acuerdo con dicha prioridad.")
    
# Función del menú
def explicacion():
    # Bucle principal del programa
    # Creamos el menú
    menu = [
        "¿Qué es un montículo?",
        "¿Qué es un Montículo máximo y mínimo?",
        "¿Para qué sirven los montículos?",
        "¿Cuáles son las partes de los montículos?",
        "¿Qué es una cola de prioridades en un montículo?",
        "Mostrar Ejemplo de Monticulos"
    ]

    # Mostramos el menú
    st.write("\n--Bienvenido a conocer mas sobre Montículos--")
    st.write("\nEn este capítulo tendrás una breve explicación en la cual aprenderás lo necesario sobre los montículos.")
    st.write("\n")
    
    opcion = st.selectbox("Menú", menu)

    # Ejecutamos la opción seleccionada
    if opcion =="¿Qué es un montículo?":
        mostrar_info_monticulo()
        
    elif opcion == "¿Qué es un Montículo máximo y mínimo?":
        Tipos_de_monticulos()
        
    elif opcion == "¿Para qué sirven los montículos?":
        mostrar_para_que_sirve()
        
    elif opcion == "¿Cuáles son las partes de los montículos?":
        mostrar_partes_de_los_monticulos()
        
    elif opcion == "¿Qué es una cola de prioridades en un montículo?":
        cola_prioridades()
    elif opcion == "Mostrar Ejemplo de Monticulos":
        mostrar_monticulo_explicacion()
    else:
        st.write("\nOpción inválida, por favor selecciona otra.")
