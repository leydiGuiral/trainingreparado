from Colores import color

from Explicacion_Grafo import explicacion
from practica_Grafo import practica

def menu():
    while True:
        print(color.AMARILLO+"\n--Bienvenido al Training de Grafos--"+color.FIN)

        print("\n-- Menú --\n")
        print("1. Explicación")
        print("2. Práctica")
        print("3. Salir")
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            explicacion()
            
        elif opcion == "2":
            practica()
            
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor selecciona otra.")
menu()