from Training_Grafos_Interfaz.Explicacion_Grafo import explicacion
from Training_Grafos_Interfaz.practica_Grafo import practica
from Training_Grafos_Interfaz.grafos_Puertos import puerto
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image

# funcion animacion
# Configuración de la página de la aplicación web

def cargar_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_codigo = cargar_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_study = cargar_lottieurl("https://assets4.lottiefiles.com/packages/lf20_phjobus6.json")
lottie_conexion = cargar_lottieurl("https://assets10.lottiefiles.com/packages/lf20_Fdv4mj.json")
saludo = cargar_lottieurl("https://assets2.lottiefiles.com/packages/lf20_khtt8ejx.json")

imagen_video = Image.open("src/Ajma.jpeg")

def menu_Grafos():
    # Diseño de la página
    with st.container():
        columna_izq,columna_der = st.columns(2)

        with columna_izq:
            st.header("AJMA: Soluciones operativas y de logistica")
            # """ --> Salto de linea
        with columna_der:
            st_lottie(lottie_conexion, height=230, key="coding0")
            
    st.markdown("---")

    st.title("Capacitación de Grafos")
    
    st.write('"Los grafos son como mapas que nos permiten explorar y comprender las interconexiones y relaciones complejas que existen en el mundo."')
    opciones = ["Inicio","Explicacion","Practica","Practica Puertos"]
    
    seleccion = st.selectbox("Menu",opciones)
    st.write("---")
    
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido. Conoce mas sobre Grafos")
            st.title("Introduccion sobre Grafos")
            explicacion()
            st.write("lo que sea")
            st.write("[Mas informacion>](https://www.youtube.com/watch?v=zeS2FlxF_0s)")
    elif seleccion =="Practica":
        with st.container():
            
            st.title("Practica tus saberes sobre Grafos")
            practica()
            
    elif seleccion =="Practica Puertos":
        with st.container():
            
            st.title("Practica tus saberes sobre Grafos aplicandolos de una forma practica")
            puerto()




        
