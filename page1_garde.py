import streamlit as st
from PIL import Image

    
 # Afficher l'image en haut de la page
    image = Image.open("image/page-accueil.jpg")  # Remplacez par le chemin de votre image
    st.image(image, use_column_width=True)
