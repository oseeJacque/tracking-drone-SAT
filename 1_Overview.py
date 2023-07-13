import streamlit as st
from PIL import Image


st.set_page_config(
page_title="Multipage App",
    page_icon="👋",
layout="wide"
)
image_path = "E:/AllProject/AllProject/dronetrack/src/testdata/13.jpg"

with st.sidebar:
    st.sidebar.image(Image.open(image_path), use_column_width=True, width=st.sidebar.width)

with st.sidebar:
    st.sidebar.success("Success")


with st.sidebar:
    st.title("Conteneur 1")
    st.text("Contenu du conteneur 1")
    st.button("Bouton 1")

# Contenu du deuxième conteneur
with st.sidebar:
    st.title("Conteneur 2")
    st.text("Contenu du conteneur 2")
    st.button("Bouton 2")






