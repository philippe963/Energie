import streamlit as st
from PIL import Image

def app():
    st.title("Page de Garde")
    st.write("Bienvenue dans le Projet Énergie")
    image = Image.open('path_to_your_image.jpg')  # Remplacez par le chemin de votre image
    st.image(image, use_column_width=True)