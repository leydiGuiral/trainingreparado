import networkx as nx
import matplotlib.pyplot as plt
from Training_Monticulos.TDA_monticulo import MonticuloColaPrioridades, heap_vacio, atencion, pos_jerarquica
import streamlit as st

cola_prioridades = MonticuloColaPrioridades()

def cancelar_atencion(paciente):
    # Verificar si el paciente está en el montículo de prioridades
    if cola_prioridades.contiene(paciente):
        cola_prioridades.eliminar_paciente(paciente)
        st.write(f"Se ha cancelado la atención del paciente {paciente}.")
    else:
        st.write(f"No se encontró al paciente {paciente} en la cola de prioridades.")


def construir_grafo_orden_llegada():
    G = nx.DiGraph()
    heap_aux = cola_prioridades.heap
    pacientes = cola_prioridades.ver_pacientes_orden_llegada()

    for i in range(len(pacientes)):
        paciente = pacientes[i]
        G.add_node(paciente, pos=(i, 0))

        if i > 0:
            padre = pacientes[(i - 1) // 2]
            G.add_edge(padre, paciente)

    return G


def mostrar_grafo_orden_llegada():
    G = construir_grafo_orden_llegada()
    pos = pos_jerarquica(G)
    
    fig, ax = plt.subplots()
    nx.draw_networkx(G, pos, with_labels=True, arrows=True, ax=ax)
    st.pyplot(fig)


def construir_grafo():
    G = nx.DiGraph()
    heap_aux = cola_prioridades.heap
    for i in range(heap_aux.tamano):
        prioridad, paciente = heap_aux.vector[i]
        G.add_node(paciente, priority=prioridad)
        if i != 0:
            padre = (i - 1) // 2
            prioridad_padre, paciente_padre = heap_aux.vector[padre]
            G.add_edge(paciente_padre, paciente)
    return G


def mostrar_grafo():
    G = construir_grafo()
    pos = pos_jerarquica(G)
    
    fig, ax = plt.subplots()
    nx.draw_networkx(G, pos, with_labels=True, arrows=True, ax=ax)
    st.pyplot(fig)


def calcular_prioridad(edad, categoria):
    prioridad = 0

    if edad >= 80:
        prioridad += 5
    elif edad >= 60:
        prioridad += 4
    elif edad >= 40:
        prioridad += 3
    elif edad >= 20:
        prioridad += 2
    else:
        prioridad += 1
    
    if categoria == "Emergencia":
        prioridad += 5
    elif categoria == "Urgencia":
        prioridad += 4
    elif categoria == "Electiva":
        prioridad += 3
    elif categoria == "Consulta":
        prioridad += 2
    else:
        prioridad += 1
    
    return prioridad, categoria



def practica():
    st.title("Programa de Montículos")
    st.write("Este programa te permite reforzar tus conocimientos sobre colas de prioridades en montículos al practicar tus saberes aplicados en el funcionamiento de montículos en el sector de la salud")

    opciones = [
        "Insertar paciente",
        "Atender paciente de mayor prioridad",
        "Ver pacientes",
        "Mostrar pacientes por prioridad",
        "Mostrar Montículo en orden de llegada",
        "Mostrar Montículo por prioridades",
        "Cancelar atención"
    ]

    opcion = st.selectbox("Menú", opciones)

    if opcion == "Insertar paciente":
        st.subheader("Insertar paciente")
        form = st.form(key="insertar_paciente_form")
        with form:
            categoria = st.selectbox("Seleccione la categoría/motivo de ingreso:", ["Emergencia", "Urgencia", "Electiva", "Consulta"])
            nombre = st.text_input("Ingrese el nombre del paciente:")
            edad = st.number_input("Ingrese la edad del paciente:", min_value=0)
            problema = st.text_area("Ingrese los detalles del problema de salud:")
            submit_button = st.form_submit_button(label="Enviar")
        if submit_button:
            prioridad, motivo = calcular_prioridad(edad,categoria)
# Declarar paciente y sus atributos
            paciente = (prioridad, nombre, problema)
            
            cola_prioridades.insertar(prioridad, paciente)
            st.success(f"Paciente '{nombre}' ingresado por {motivo} ha sido agregado con éxito.")

    elif opcion == "Atender paciente de mayor prioridad":
        st.subheader("Atender paciente de mayor prioridad")
        if not heap_vacio(cola_prioridades.heap):
            maxima_prioridad, paciente = cola_prioridades.extraer_maximo()
            st.write("Paciente con la mayor prioridad:", paciente[1])
            st.success(f"Paciente '{paciente[1]}' ha sido atendido.")
        else:
            st.write("La cola de prioridades está vacía.")

    elif opcion == "Ver pacientes":
        st.subheader("Ver pacientes por orden de llegada")
        pacientes = cola_prioridades.ver_pacientes_orden_llegada()
        if pacientes:
            st.write("Pacientes por orden de llegada:")
            for paciente in pacientes:
                st.write(f"Nombre: {paciente[1]}, Motivo de ingreso: {paciente[2]}")
        else:
            st.write("No hay pacientes en espera.")


    elif opcion == "Mostrar pacientes por prioridad":
        st.subheader("Mostrar pacientes por prioridad")
        pacientes = cola_prioridades.ver_pacientes_por_prioridad()
        
        if pacientes:
            st.write("Pacientes por prioridad:")
            for paciente in pacientes:
                st.write(f"Nombre: {paciente[1]}, Prioridad: {paciente[0]}")
        else:
            st.write("No hay pacientes en la cola de prioridades.")

    elif opcion == "Mostrar Montículo en orden de llegada":
        heap_aux = cola_prioridades.heap
                  
        if not heap_vacio(cola_prioridades.heap):
            st.subheader("Atención normal de pacientes en orden de llegada")
            mostrar_grafo_orden_llegada()
        else:
            st.write("No hay pacientes en la cola.")

    elif opcion == "Mostrar Montículo por prioridades":
        st.subheader("Mostrar Montículo por prioridades")
        heap_aux = cola_prioridades.heap
        if not heap_vacio(heap_aux):
            st.write("Cola por prioridades:")
            for i in range(heap_aux.tamano):
                prioridad, paciente = heap_aux.vector[i]
                st.write(f"Prioridad: {prioridad} - Paciente: {paciente[1]}")

        if not heap_vacio(cola_prioridades.heap):
            st.subheader("Atención de pacientes según su prioridad")
            mostrar_grafo()
        else:
            st.write("No hay pacientes en la cola de prioridades.")

    elif opcion == "Cancelar atención":
        pacientes = cola_prioridades.ver_pacientes_orden_llegada()

        st.subheader("Cancelar atención")
        form = st.form(key="cancelar_atencion_form")
        with form:
            paciente_cancelar = st.selectbox("Seleccione el paciente a cancelar:", [paciente[1] for paciente in pacientes])
            submit_button = st.form_submit_button(label="Cancelar atención")
        if submit_button:
            cancelar_atencion(paciente_cancelar)

        # Eliminar el paciente de la lista de pacientes
        pacientes = [paciente for paciente in pacientes if paciente[1] != paciente_cancelar]

    else:
        st.write("Opción inválida. Por favor, seleccione una opción válida.")
