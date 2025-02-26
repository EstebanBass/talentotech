import pandas as pd
import streamlit as st
import seaborn as sb
from PIL import Image
from matplotlib import pyplot as plt
import utilidades as util

#Configuramos encabezados de pagina

st.set_page_config(page_title="Informe de la liga", page_icon="",initial_sidebar_state="expanded", layout="centered")


util.generarmenu()

#Visualizacion

st.title("Datos de la Liga Colombiana 2024")
path = 'data/todosContraTodos_Ok.csv'
df = pd.read_csv(path)

# Configuramos la visualizacion
col1, col2, col3 = st.columns([0.5, 5, 0.5], vertical_alignment="top")
with col2:
    st.markdown("Cantidad de Goles Marcado por cada equipo")
    st.write(df, unsafe_allow_html=False)


