import streamlit as st
from PIL import Image

def app():
    st.markdown(
        """
        <style>
        body {
            margin: 0;
            padding: 0;
        }
        .centered-title {
            text-align: center;
            font-size: 24px;  /* Vous pouvez ajuster la taille de la police si nécessaire */
            margin: 0;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Afficher l'image en haut de la page
    image = Image.open("image/image-accueil2.jpg")  # Remplacez par le chemin de votre image
    st.markdown(
        f'<div class="image-container"><img src="data:image/jpeg;base64,{st.image(image, use_column_width=True).data}" alt="Image" style="width: 100%;"></div>',
        unsafe_allow_html=True
    )
    # Utilisation de HTML et CSS pour centrer le titre
    st.markdown('<div class="centered-title">Bienvenue dans le Projet Énergie</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
