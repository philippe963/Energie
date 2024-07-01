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
    st.markdown(f'<div class="image-container"><img src="data:image/jpeg;base64,{st.image(image, use_column_width=True).data}" alt="Image" style="width: 100%; margin: 0; padding: 0;"></div>', unsafe_allow_html=True)
    
    # Utilisation de HTML et CSS pour centrer le titre
    st.markdown('<div class="centered-title">Bienvenue dans le Projet Énergie</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
