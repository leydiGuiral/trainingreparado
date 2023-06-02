import streamlit as st
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import networkx as nx
from TrainingArboles.TDA_Arbol import Arbol, Nodo, dfs_preorden, mostrar_arbol_con_networkx

# Crear el árbol con los caracteres en código Morse
raiz = Nodo('')
arbol_morse = Arbol(raiz)

arbol_morse.agregar_nodo('E', arbol_morse.raiz)
arbol_morse.agregar_nodo('T', arbol_morse.raiz)
arbol_morse.agregar_nodo('I', arbol_morse.buscar_nodo('E'))
arbol_morse.agregar_nodo('A', arbol_morse.buscar_nodo('E'))
arbol_morse.agregar_nodo('N', arbol_morse.buscar_nodo('A'))
arbol_morse.agregar_nodo('M', arbol_morse.buscar_nodo('N'))
arbol_morse.agregar_nodo('S', arbol_morse.buscar_nodo('N'))
arbol_morse.agregar_nodo('U', arbol_morse.buscar_nodo('S'))
arbol_morse.agregar_nodo('R', arbol_morse.buscar_nodo('S'))
arbol_morse.agregar_nodo('W', arbol_morse.buscar_nodo('U'))
arbol_morse.agregar_nodo('D', arbol_morse.buscar_nodo('T'))
arbol_morse.agregar_nodo('K', arbol_morse.buscar_nodo('D'))
arbol_morse.agregar_nodo('G', arbol_morse.buscar_nodo('N'))
arbol_morse.agregar_nodo('O', arbol_morse.buscar_nodo('G'))
arbol_morse.agregar_nodo('H', arbol_morse.buscar_nodo('O'))
arbol_morse.agregar_nodo('V', arbol_morse.buscar_nodo('U'))
arbol_morse.agregar_nodo('F', arbol_morse.buscar_nodo('U'))
arbol_morse.agregar_nodo('L', arbol_morse.buscar_nodo('T'))
arbol_morse.agregar_nodo('P', arbol_morse.buscar_nodo('R'))
arbol_morse.agregar_nodo('B', arbol_morse.buscar_nodo('D'))
arbol_morse.agregar_nodo('X', arbol_morse.buscar_nodo('K'))
arbol_morse.agregar_nodo('C', arbol_morse.buscar_nodo('M'))
arbol_morse.agregar_nodo('Y', arbol_morse.buscar_nodo('R'))
arbol_morse.agregar_nodo('J', arbol_morse.buscar_nodo('Y'))
arbol_morse.agregar_nodo('Z', arbol_morse.buscar_nodo('G'))
arbol_morse.agregar_nodo('Q', arbol_morse.buscar_nodo('G'))

# Función para codificar una frase en código Morse
def codificar_morse(frase):
    frase_codificada = ''
    for caracter in frase:
        if caracter.isalpha():
            caracter_morse = arbol_morse.buscar_nodo(caracter.upper())
            if caracter_morse is not None:
                morse = ''
                nodo_actual = caracter_morse
                while nodo_actual.padre is not None:
                    if nodo_actual.padre.hijos.index(nodo_actual) == 0:
                        morse += '.'
                    else:
                        morse += '-'
                    nodo_actual = nodo_actual.padre
                frase_codificada += morse[::-1] + ' '
            else:
                frase_codificada += caracter + ' '
        else:
            frase_codificada += caracter + ' '

    return frase_codificada.strip()

# Función para decodificar una frase en código Morse
def decodificar_morse(frase_morse):
    palabras = frase_morse.split('/')
    frase_decodificada = ''
    for palabra in palabras:
        letras_morse = palabra.strip().split(' ')
        for letra_morse in letras_morse:
            if letra_morse:
                nodo_actual = arbol_morse.raiz
                for simbolo in letra_morse:
                    if simbolo == '.':
                        if len(nodo_actual.hijos) > 0:
                            nodo_actual = nodo_actual.hijos[0]
                    elif simbolo == '-':
                        if len(nodo_actual.hijos) > 1:
                            nodo_actual = nodo_actual.hijos[1]
                if nodo_actual.valor:
                    frase_decodificada += nodo_actual.valor
                else:
                    frase_decodificada += '?'
        frase_decodificada += ' '

    return frase_decodificada.strip()

def morse():
    # Mostrar el formulario para ingresar la frase a codificar o decodificar
    frase = st.text_input('Ingrese la frase a codificar o decodificar en código Morse:')
    modo = st.selectbox('Seleccione el modo:', ['Codificar', 'Decodificar'])
    submitted = st.button('Enviar')

    if submitted:
        if frase:
            if modo == 'Codificar':
                codificado = codificar_morse(frase)
                st.success('Frase codificada a código Morse:')
                st.code(codificado)
            elif modo == 'Decodificar':
                decodificado = decodificar_morse(frase)
                st.success('Frase decodificada al español:')
                st.write(decodificado)
        else:
            st.warning('Ingrese la frase que desees procesar.')
