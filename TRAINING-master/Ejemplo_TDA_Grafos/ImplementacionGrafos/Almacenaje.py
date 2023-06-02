import networkx as nx
import matplotlib.pyplot as plt
from TDA2 import Grafo
def grafica():
    # Creando grafo del proceso de almacenaje
    g = Grafo()
    g.agregar_nodo('Recepción')
    g.agregar_nodo('Almacenamiento')
    g.agregar_nodo('Control de inventario')
    g.agregar_nodo('Preparación de pedidos')
    g.agregar_nodo('Despacho')
    g.agregar_arista('Recepción', 'Almacenamiento', 2)
    g.agregar_arista('Almacenamiento', 'Control de inventario', 3)
    g.agregar_arista('Control de inventario', 'Preparación de pedidos', 5)
    g.agregar_arista('Preparación de pedidos', 'Despacho', 4)
    g.agregar_arista('Recepción', 'Control de inventario', 6)
    g.agregar_arista('Recepción', 'Preparación de pedidos', 7)
    g.agregar_arista('Recepción', 'Despacho', 9)
    g.agregar_arista('Almacenamiento', 'Preparación de pedidos', 8)
    g.agregar_arista('Almacenamiento', 'Despacho', 10)
    g.agregar_arista('Control de inventario', 'Despacho', 11)

    # Creando grafo con la librería para graficar
    g_nx = nx.Graph()
    g_nx.add_nodes_from(g.nodos())
    for inicio, fin, peso in g.aristas_con_pesos():
        g_nx.add_edge(inicio, fin, weight=peso)

    pos = nx.spring_layout(g_nx)
    
    # Dibujar el grafo con networkx y matplotlib.pyplot
    nx.draw(g_nx, pos, with_labels=True, node_color='lightblue', edge_color='red', node_size=800, font_size=10, font_family='monospace')
    # agregar etiquetas de peso de las aristas (opcional)
    labels = nx.get_edge_attributes(g_nx, 'weight')
    nx.draw_networkx_edge_labels(g_nx, pos,edge_labels=labels, font_size=10 )
    plt.show()
    
def NivelAlmacenaje():  # necesitamos usar spring_layout para que las aristas se dibujen espaciadas adecuadamente
    print("Bienvenido al simulador de gestión de riesgo en el proceso de almacenaje")
    print("")
    print("El objetivo del juego es encontrar la forma más óptima de hacer el almacenaje del producto y aprender de ello.")
    print("Se te presentará un escenario en el que tendrás que tomar decisiones para minimizar los riesgos.")
    print("")

    print("¿Estás listo para comenzar? Iniciaremos con un nivel básico.")
    print("Escoge 1: Para sí   2: Para no")
    opc = input("Digita la opción: ")

    if (opc == "1"):
        salida = True
        print("")
        print("Se ha recibido un nuevo producto en la bodega y es necesario almacenarlo.")
        print("El producto es un material inflamable y es necesario tomar medidas de seguridad para evitar cualquier tipo de riesgo.")
        while salida == True:
            print("")
            print("0: Ver gráfica")
            print("1: Ver opciones")
            print("2: Salir")
            opc2 = input()

            if opc2 == "0":
                grafica()
            elif opc2 == "1":
                puntaje = 0
                salida2 = True
                while salida2 == True:
                    print("")
                    print("0: Ver gráfica")
                    print("1: Recepción → Almacenamiento → Control de inventario → Preparación de pedidos → Despacho")
                    print("2: Recepción → Control de inventario → Almacenamiento → Preparación de pedidos → Despacho")
                    print("3: Recepción → Almacenamiento → Control de inventario → Despacho")
                    print("7: Regresar")
                    opc3 = input()
                    if opc3 == "0":
                        grafica()
                    elif opc3 == "1":
                        puntaje = 0
                        print("")
                        print("Has elegido la opción 1: Recepción → Almacenamiento → Control de inventario → Preparación de pedidos → Despacho")
                        print("Recuerda que el objetivo del juego es minimizar los riesgos en el proceso de almacenaje.")
                        print("Almacenarás el producto inflamable en el Almacenamiento y luego lo enviarás al Control de inventario.")
                        print("Si el producto llega al Control de inventario sin ningún tipo de riesgo, ganarás 5 puntos.")
                        print("Si hay algún tipo de riesgo en el proceso, perderás 10 puntos.")
                        print("Al final del juego se te dará un puntaje de acuerdo a las decisiones que hayas tomado.")
                        print("")
                        print("¿Estás seguro de tu elección?")
                        print("Escoge 1: Para sí   2: Para no")
                        opc4 = input()

                        if opc4 == "1":
                            print("")
                            print("¡Excelente elección!")
                            print("Has almacenado el producto sin ningún tipo de riesgo.")
                            puntaje += 5
                            print("Tu puntaje actual es de:", puntaje)
                            print("")
                            print("¿Quieres seguir con el siguiente paso del proceso?")
                            print("Escoge 1: Para sí   2: Para no")
                            opc5 = input()

                        if opc5 == "1":
                            print("")
                            print("Enviarás el producto al Control de inventario.")
                            print("¿Estás seguro de que quieres hacer esta acción?")
                            print("Escoge 1: Para sí   2: Para no")
                            opc6 = input()

                        if opc6 == "1":
                            print("")
                            print("El tiempo total de proceso para la opción 1 es de 14 días.")
                            print("Esta opción es la más óptima ya que se realiza en el menor tiempo posible, lo que disminuye el riesgo de incidentes en la bodega.")
                            puntaje += 5
                            salida2 = False
                            
                        elif opc6 == "2":
                            print("")
                            print("El tiempo total de proceso para la opción 2 es de 15 días.")
                            print("Esta opción no es la más óptima ya que se demora un día más que la opción 1, lo que aumenta el riesgo de incidentes en la bodega.")
                            puntaje -= 2
                            salida2 = False
                            
                        else:
                            print("")
                            print("Opción no válida, por favor intenta de nuevo.")
                    elif opc3 == "2":
                        print("")
                        print("Iniciando el proceso de almacenaje...")
                        # Almacenando el producto en el nodo 'Almacenamiento'
                        print("Almacenando el producto en el nodo 'Almacenamiento'...")
                        print("Se ha completado el almacenamiento del producto de forma segura.")
                        # Enviando el producto al nodo 'Control de inventario'
                        print("Enviando el producto al nodo 'Control de inventario'...")
                        riesgo = input("¿Hay algún tipo de riesgo? Escoge 1: Para sí   2: Para no")
                        if riesgo == "1":
                            puntaje -= 10
                            print("Ha ocurrido un riesgo en el proceso de almacenaje.")
                        else:
                            puntaje += 5
                            print("El producto ha llegado al nodo 'Control de inventario' sin ningún tipo de riesgo.")
                        # Enviando el producto al nodo 'Preparación de pedidos'
                        print("Enviando el producto al nodo 'Preparación de pedidos'...")
                        riesgo = input("¿Hay algún tipo de riesgo? Escoge 1: Para sí   2: Para no")
                        if riesgo == "1":
                            puntaje -= 10
                            print("Ha ocurrido un riesgo en el proceso de almacenaje.")
                        else:
                            puntaje += 5
                            print("El producto ha llegado al nodo 'Preparación de pedidos' sin ningún tipo de riesgo.")
                        # Enviando el producto al nodo 'Despacho'
                        print("Enviando el producto al nodo 'Despacho'...")
                        riesgo = input("¿Hay algún tipo de riesgo? Escoge 1: Para sí   2: Para no")
                        if riesgo == "1":
                            puntaje -= 10
                            print("Ha ocurrido un riesgo en el proceso de almacenaje.")
                        else:
                            puntaje += 5
                            print("El producto ha llegado al nodo 'Despacho' sin ningún tipo de riesgo.")
                        print("")
                        print("Proceso de almacenaje finalizado.")
                        print("Tu puntaje actual es:", puntaje)
                    elif opc3 == "3":
                        puntaje = 0
                        print("")
                        print("Has elegido la opción 3: Recepción → Almacenamiento → Control de inventario → Despacho")
                        print("Recuerda que el objetivo del juego es minimizar los riesgos en el proceso de almacenaje.")
                        print("Almacenarás el producto inflamable en el Almacenamiento y lo enviarás directamente al Despacho.")
                        print("Si el producto llega al Despacho sin ningún tipo de riesgo, ganarás 4 puntos.")
                        print("Si hay algún tipo de riesgo en el proceso, perderás 10 puntos.")
                        print("Al final del juego se te dará un puntaje de acuerdo a las decisiones que hayas tomado.")
                        print("")
                        print("¿Estás seguro de tu elección?")
                        print("Escoge 1: Para sí   2: Para no")
                        opc4 = input()

                        if opc4 == "1":
                            print("")
                            print("¡Excelente elección!")
                            print("Has enviado el producto directamente al Despacho sin ningún tipo de riesgo.")
                            puntaje += 4
                            print("Tu puntaje actual es de:", puntaje)
                            print("")
                            print("¿Quieres seguir con el siguiente paso del proceso?")
                            print("Escoge 1: Para sí   2: Para no")
                            opc5 = input()
                            if opc5 == "1":
                                print("")
                                print("Felicidades, has completado el proceso de almacenaje sin riesgos.")
                                print("Tu puntaje final es de:", puntaje)
                                print("")
                                salida2 = False
                                salida = False
                            elif opc5 == "2":
                                print("")
                                print("Gracias por jugar.")
                                print("Tu puntaje final es de:", puntaje)
                                print("")
                                salida2 = False
                                salida = False
                        elif opc4 == "2":
                            print("")
                            print("Elige otra opción.")

            elif opc2 == "2":
                print("")
                print("Tu puntaje final fue de:", puntaje)
                print("¡Gracias por jugar!")
                salida = False
            else:
                print("")
                print("Opción no válida, por favor intenta de nuevo.")
                
        