import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt

def generarmenu():
    with st .sidebar:
        col1, col2 = st.columns(2)
        with col1:
            imagen = Image.open("media\Da.png")
            st.image(imagen, use_container_width=False, width=900)
        with col2:
            st.header('Torneo 2024')
        st.page_link('app.py', label='Home', icon='☔')
        st.page_link('Pages\informe.py', label='informe', icon='☔')


