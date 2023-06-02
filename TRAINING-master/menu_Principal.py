from Training_Grafos_Interfaz.Menu_Grafo import menu_Grafos
from Training_Monticulos.menu_Monticulos import menu_Monticulos
from TrainingArboles.menu_Arbol import menu_Arboles

import streamlit as st 
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from PIL import Image


# Función para cargar animaciones Lottie
def cargar_lottieurl(url):
    r = requests.get(url)       
    if r.status_code != 200:
        return None
    return r.json()

# Cargar animaciones Lottie
lottie_codigo = cargar_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")
lottie_study = cargar_lottieurl("https://assets4.lottiefiles.com/packages/lf20_phjobus6.json")
lottie_conexion = cargar_lottieurl("https://assets10.lottiefiles.com/packages/lf20_Fdv4mj.json")
saludo = cargar_lottieurl("https://assets2.lottiefiles.com/packages/lf20_khtt8ejx.json")
holograma = cargar_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_vtbeu3qj.json")
conexion = cargar_lottieurl("https://assets1.lottiefiles.com/packages/lf20_p856l7zn.json")
imagen_video = Image.open("src/Ajma.jpeg")

# Menú de selección
st.sidebar.title("Menu Principal")
st.sidebar.subheader("Por favor seleccione el tema que desea conocer de una mejor manera")
opciones = ["Inicio", "Grafos", "Árboles", "Montículos"]
seleccion = st.sidebar.selectbox("Menú", opciones)

if seleccion == "Inicio":
# Diseño de la página
    with st.container():
        columna_izq,columna_der = st.columns(2)

        with columna_izq:
            st.header("Bienvenido: Avanza hacia el Dominio de los Grafos, Montículos y Árboles")
            # """ --> Salto de linea
        with columna_der:
            st_lottie(lottie_codigo, height=230, key="coding0")
            
    st.markdown("---")
    st.title("Capacitación en Soluciones Operativas y Logística AJMA")

    st.write("¡Bienvenidos a nuestra página de capacitación!")

    st.write("Aquí encontrarán recursos y materiales diseñados para fortalecer sus conocimientos y habilidades en el campo de la logística y las soluciones operativas. Nuestro objetivo es proporcionarles las herramientas necesarias para optimizar sus procesos, mejorar la eficiencia y aumentar la rentabilidad de su empresa.")

    with st.container():
        st_lottie(saludo, height=230, key="coding2")
    st.markdown("---")
    st.write("En esta plataforma de capacitación, tendrán acceso a contenido actualizado y relevante, desde conceptos fundamentales hasta las últimas tendencias y mejores prácticas en el campo de la logística de puertos, monticulos basados en el campo de la salud y Morse. Nuestros cursos y materiales están desarrollados por expertos en la industria, con una amplia experiencia y conocimientos especializados.")
    st.write("Ya sea que estén buscando mejorar la gestión de inventario, optimizar rutas de distribución, implementar sistemas de seguimiento y control, o desarrollar estrategias de cadena de suministro más eficientes, encontrarán recursos prácticos y ejemplos reales que les ayudarán a abordar los desafíos específicos de su negocio.")
    st.write("Nuestra plataforma de capacitación ofrece una experiencia interactiva, con oportunidades para realizar ejercicios prácticos, participar en discusiones y recibir retroalimentación personalizada de nuestros instructores. Estamos comprometidos con su éxito y queremos asegurarnos de que obtengan el máximo provecho de su experiencia de capacitación.")
    st.write("Los invitamos a explorar nuestros cursos. Estamos aquí para apoyar su crecimiento profesional y ayudarles a alcanzar sus metas en el campo de las soluciones operativas y logística.")
    st.write("¡Gracias por elegir nuestra plataforma de capacitación y esperamos que disfruten de su experiencia de aprendizaje!")

elif seleccion == "Grafos":
    menu_Grafos()

elif seleccion == "Árboles":
    menu_Arboles()

elif seleccion == "Montículos":
    menu_Monticulos()

st.markdown("---")

with st.container():
    columna_imagen, columna_texto = st.columns((1, 2))
    with columna_imagen:
        st.image(imagen_video)
    with columna_texto:
        st.write("Bienvenido/a : Avanza hacia el Dominio de los Grafos, Montículos y Árboles")
