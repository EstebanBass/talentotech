import pandas as pd
import streamlit as st
import utilidades as util
from PIL import Image


#Pagina de presentacion o index

st.set_page_config(
    page_title="Info Liga Colombiana",
    initial_sidebar_state="expanded",
    layout="centered",
    page_icon="🆚"
)
#llamamos la función utilidades

util.generarmenu()

#Estructura de presentacion

left_col, center_col, right_col = st.columns([1, 4, 1], vertical_alignment="center")

#Edito la columna central

with center_col:
    st.title("informe de la liga colombiana 2024-2")
    st.write("""
              En este espacio se puede mostrar cual fue el 
              desempeño de los equipos de futbol durante la liga bet play, en el año 2024 segundo semestre
              
              """)
    imagen2 = Image.open("media\Futbol.png")
    st.image(imagen2, use_container_width=True, caption="Seleccion Colombia")