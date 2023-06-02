from Explicacion import explicacion
from practica_Grafo import practica

def menu():
    while True:
        print("\n-- Bienvenido al training de Grafos --")
        print("-- Menú --")
        print("\n-- Menú --")
        print("1. Explicación")
        print("2. Práctica")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

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