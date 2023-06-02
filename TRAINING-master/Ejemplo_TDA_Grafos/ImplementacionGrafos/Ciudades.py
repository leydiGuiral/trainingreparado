import networkx as nx
import matplotlib.pyplot as plt
from TDA2 import Grafo

def NivelCiudades():
    # Creando grafo del punto
    g = Grafo()
    g.agregar_nodo('Cali')
    g.agregar_nodo('Alcala')
    g.agregar_nodo('Pereira')
    g.agregar_nodo('Medellin')
    g.agregar_nodo('Cucuta')
    g.agregar_nodo('Cartagena')
    g.agregar_nodo('Barranquilla')
    g.agregar_nodo('Bucaramanga')
    g.agregar_arista('Cali', 'Alcala', 2)
    g.agregar_arista('Cali', 'Pereira', 3)
    g.agregar_arista('Cali', 'Medellin', 8)
    g.agregar_arista('Cali', 'Cucuta', 12)
    g.agregar_arista('Cali', 'Barranquilla', 8)
    g.agregar_arista('Alcala', 'Pereira', 2)
    g.agregar_arista('Alcala', 'Bucaramanga', 3)
    g.agregar_arista('Pereira', 'Medellin', 5)
    g.agregar_arista('Bucaramanga', 'Barranquilla', 4)
    g.agregar_arista('Barranquilla', 'Cartagena', 6)
    g.agregar_arista('Medellin', 'Cucuta', 5)
    g.agregar_arista('Medellin', 'Cartagena', 2)
    g.agregar_arista('Cucuta', 'Cartagena', 4)


    # Creando grafo con la libreria para graficar 
    g_nx = nx.Graph()
    g_nx.add_nodes_from(g.nodos())
    for inicio, fin, peso in g.aristas_con_pesos():
        g_nx.add_edge(inicio, fin, weight=peso)

    pos = nx.spring_layout(g_nx)  # necesitamos usar spring_layout para que las aristas se dibujen espaciadas adecuadamente

    print("Bienvenido al Training de AGMA")
    print("")
    print("A continuación te haremos unas pruebas para saber tu capacidad para hallar las mejores rutas para nuestros envios")
    print("Evaluaremos y te haremos una retroalimentación para ayudarte a mejorar tus capacidades.")
    print("")
    print("¿Estas listo? Iniciaremos con niveles básicos si respondes bien")
    print("Escoge 1: Para si   2: Para no")
    opc = input("Digita la opción: ")

    if (opc == "1"):
        salida = True
        print("")
        print("Un cliente nos ha pedido un servicio de logística a su domicilio, necesita que le enviemos una maquina pesada a cartagena,")
        print("si la maquina está en Cali ¿Cuál seria la mejor ruta para llegar lo más rápido posible?")
        while salida == True:
            print("")
            print("0: Ver grafica")
            print("1: Ver opciones")
            print("2: Salir")
            opc2 = input()

            if opc2 == "0":
                # Dibujar el grafo con networkx y matplotlib.pyplot
                nx.draw(g_nx, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=800, font_size=10, font_family='monospace')
                # agregar etiquetas de peso de las aristas (opcional)
                labels = nx.get_edge_attributes(g_nx, 'weight')
                nx.draw_networkx_edge_labels(g_nx, pos,edge_labels=labels, font_size=10 )
                plt.show()
            elif opc2 == "1":
                puntaje = 0
                salida2 = True
                while salida2 == True:
                    print("")
                    print("0. Ver grafica")
                    print("1. Cali → Cucuta → Cartagena")
                    print("2. Cali → Medellin → Cucuta → Cartagena")
                    print("3. Cali → Pereira → Medellin → Cartagena")
                    print("4. Cali → Pereira → Medellin → Cucuta → Cartagena")
                    print("5. Cali → Alcala → Pereira → Medellin → Cartagena")
                    print("6. Cali → Alcala → Pereira → Medellin → Cucuta → Cartagena")
                    print("7. Cali → Alcala → Bucaramanga → Barranquilla → Cartagenta")
                    print("8. Cali → Barranquilla → Cartagena")
                    print("")

                    seleccion = input("Escoge la mejor opción para ti: ")

                    if(seleccion == "0"):
                        # Dibujar el grafo con networkx y matplotlib.pyplot
                        nx.draw(g_nx, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=800, font_size=10, font_family='monospace')
                        # agregar etiquetas de peso de las aristas (opcional)
                        nx.draw_networkx_edge_labels(g_nx, pos,edge_labels=labels, font_size=10 )
                        plt.show()
                    elif (seleccion == "3"):
                        print("")
                        print("Buena respuesta!")
                        puntaje = puntaje + 5
                        salida = False
                        salida2 = False
                    elif(seleccion == "5"):
                        salida = False
                        salida2 = False
                        puntaje = puntaje + 4
                    elif(seleccion == "8"):
                        salida = False
                        salida2 = False
                        puntaje = puntaje + 1
                    elif(seleccion == "1" or seleccion == "2" or seleccion == "4" or seleccion == "6" or seleccion == "7" ):
                        salida = False
                        salida2 = False

            elif opc2 == "2":
                print("")
                print("Nos vemos pronto...")
                salida = False