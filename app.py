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

# Importer les pages
import page1_garde
import page2_introduction
import page3_dataviz
import page4_production
import page5_renouvelable_fossile
import page6_prediction
import page7_conclusion
import page8_source

# Dictionnaire pour les pages
PAGES = {
    "Accueil": page1_garde,
    "Introduction": page2_introduction,
    "Data Visualisation": page3_dataviz,
    "Production": page4_production,
    "Renouvelables vs Fossile": page5_renouvelable_fossile,
    "Prédiction": page6_prediction,
    "Conclusion": page7_conclusion,
    "Source": page8_source
}

# Barre de navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

