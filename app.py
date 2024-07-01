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

# Importer les pages
import page1_garde
import page2_introduction
import page3_dataviz
import page4_production
import page5_renouvelable_fossile
import page6_prédiction
import page7_conclusion
import page8_source

# Dictionnaire pour les pages
PAGES = {
    "Introduction": page2_introduction,
    "Data Visualisation": page3_dataviz,
    "Production": page4_production,
    "Énergies Renouvelables vs Énergie Fossile": page5_renouvelable_fossile,
    "Prédiction": page6_prédiction,
    "Conclusion": page7_conclusion,
    "Source": page8_source
}

# Barre de navigation
st.sidebar.title("Navigation")

# Ajouter l'image de l'icône
st.sidebar.image("path_to_your_icon_image.png", use_column_width=True)

# Afficher la page de garde en premier
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Page de Garde"
    page1_garde.app()
else:
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()), index=list(PAGES.keys()).index(st.session_state.selected_page))
    page = PAGES[selection]
    page.app()
    st.session_state.selected_page = selection
