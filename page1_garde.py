import streamlit as st
from PIL import Image

def app():
    # Utilisation de CSS pour enlever les marges et paddings par défaut du body et centrer le titre
    st.markdown(
        """
        <style>
        body {
            margin: 0;
            padding: 0;
        }
        .image-container {
            text-align: center;
            margin: 0;
            padding: 0;
        }
        .centered-title {
            text-align: center;
            font-size: 24px;  /* Ajustez la taille de la police si nécessaire */
            margin-top: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
 # Afficher l'image en haut de la page
    image = Image.open("image/page-accueil.jpg")  # Remplacez par le chemin de votre image
    st.image(image, use_column_width=True)
