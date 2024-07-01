import streamlit as st
from PIL import Image

def app():
    # Afficher l'image en haut de la page
    image = Image.open("image/page-accueil.jpg")  # Remplacez par le chemin de votre image
    st.image(image, use_column_width=True)
    
    # Utiliser la classe container pour structurer le contenu
    st.markdown(
        """
        <div class="container">
            <h1>Bienvenue dans le Projet Énergie</h1>
            <p>Dans un contexte mondial où la transition énergétique est devenue une priorité, la France se positionne en tant qu'acteur engagé dans la recherche d'un équilibre optimal entre la production d'énergie et les impératifs environnementaux.</p>
            <p>Ce projet vise à prédire la consommation d'énergie en utilisant des techniques avancées de machine learning pour optimiser la production et répondre aux besoins de manière efficace et durable.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()