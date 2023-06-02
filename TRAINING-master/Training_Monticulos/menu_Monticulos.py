from PIL import Image
from Training_Monticulos.practica_Monticulo import practica
from Training_Monticulos.Explicacion_Monticulos import explicacion

import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image

# funcion animacion

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

def menu_Monticulos():
    st.header("Los montículos nos muestran el poder de la prioridad y la eficiencia, permitiéndonos gestionar y atender tareas de manera ordenada y efectiva, escalando hacia el éxito con cada paso que damos.en nuestro caso lo adaptamos al tema de la salud")
    st.title("Capacitación de Monticulos")
    opciones = ["Inicio","Explicacion","Practica"]
    seleccion = st.selectbox("Menu monticulos",opciones)
    st.write("---")
    if seleccion =="Explicacion":
        with st.container():
            st.subheader("Bienvenido. Conoce mas sobre Monticulos")
            st.title("Introduccion sobre Monticulos")
            explicacion()

    elif seleccion =="Practica":
        with st.container():
            st.title("Practica tus saberes sobre Monticulos")
            practica()