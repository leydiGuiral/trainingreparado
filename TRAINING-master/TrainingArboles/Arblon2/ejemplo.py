from TDAarbol import Arbol

# creamos el nodo raíz
arbol = Arbol("A")

# agregamos los hijos
arbol.add_node("B", "A")
arbol.add_node("C", "A")
arbol.add_node("D", "B")
arbol.add_node("E", "B")
arbol.add_node("F", "C")
arbol.add_node("G", "C")
arbol.add_node("H", "F")
arbol.add_node("I", "F")

# encontramos las hojas
hojas = arbol.find_leaves()
print("Hojas:", hojas)

# visualizamos el árbol
dot = arbol.graficar()
dot.render('arbol', view=True)