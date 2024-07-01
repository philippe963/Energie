""" Commande à exécuter sur Powershell Prompt pour visualiser streamlit sur le web
cd '1 - Formation data analyst'
cd 'Sprint 3  Machine Learning Supervisé - Streamlit'
cd 'Streamlit'
streamlit run 'streamlit_app.py'

Une la page streamlit affichée - cliquer sur "Always re-run" pour afficher les modifications au fil de l'eau
"""

import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Projet Énergie",
    page_icon="🔋",
    layout="wide"
)

# Charger le CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Intégrer Chart.js via CDN et le fichier JavaScript de configuration
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="chart_config.js"></script>
""", unsafe_allow_html=True)

# Ajouter un conteneur pour le graphique
st.markdown("""
    <div>
        <canvas id="myChart" width="400" height="400"></canvas>
    </div>
""", unsafe_allow_html=True)

# Dictionnaire pour les pages
import page1_garde
import page2_introduction
import page3_dataviz
import page4_production
import page5_renouvelable_fossile
import page6_prediction
import page7_conclusion
import page8_source

PAGES = {
    "Page de Garde": page1_garde,
    "Introduction": page2_introduction,
    "Data Visualisation": page3_dataviz,
    "Production": page4_production,
    "Énergies Renouvelables vs Énergie Fossile": page5_renouvelable_fossile,
    "Prédiction": page6_prediction,
    "Conclusion": page7_conclusion,
    "Source": page8_source
}

# Barre de navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Aller à", list(PAGES.keys()))
page = PAGES[selection]
page.app()
