import streamlit as st

def app():
    st.markdown(
        """
        <style>
        .centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Afficher le bandeau en haut de la page avec une largeur maximale de 1200 pixels et centré
    st.markdown('<img src="image/Bandeau-page.jpg" class="centered-image" width="1200">', unsafe_allow_html=True)
    

    # Contenu de la page
    st.markdown(
        """
        <div class="container">
            <h1>Introduction</h1>
            <p>Dans un contexte mondial où la transition énergétique est devenue une priorité, la France se positionne en tant qu'acteur engagé dans la recherche d'un équilibre optimal entre la production d'énergie et les impératifs environnementaux.</p>
            <p>Ce rapport vise à éclairer les dynamiques de la production et de la consommation d’électricité en France métropolitaine, à travers une analyse rigoureuse des données de 2013 à 2022, fournies par l’Open Data Réseaux Énergies (ODRÉ).</p>
            <p>L'ODRÉ, fruit de la collaboration entre les principaux acteurs du secteur énergétique français tels que GRTgaz et RTE, et rejoint par d'autres entités telles que Teréga, Storengy, Elengy, se veut un catalyseur dans la mise à disposition de données fiables et transparentes.</p>
            <p>Le jeu de données qui sert de socle à notre étude est une véritable cartographie de l'électricité métropolitaine française, illustrant non seulement la consommation totale mais également la répartition détaillée de la production par filière énergétique par région.</p>
            <p>Dans cette optique, notre analyse s'articule autour de la valorisation des connaissances accumulées par les membres de notre équipe, issus pour certains du secteur énergétique, pour déchiffrer et contextualiser les informations contenues dans ces données. Cependant, le monde de l’énergie est vaste et complexe. Notre travail a donc d’abord été d’appréhender et comprendre l’ensemble des variables présentes dans le jeu de données.</p>
            <h1>Nos objectifs :</h1>
            <ul>
                <li>Est-il possible grâce à ce jeu de données de construire un modèle précis de forecasting de la consommation pour un jour et une heure donnée afin de pouvoir adapter la production en conséquence ?</li>
                <li>Que peut-on dire de la répartition à la maille régionale des différents moyens de production d’électricité ?</li>
                <li>Quelle évolution sur les dix dernières années entre les ENR et les énergies fossiles ? Observe-t-on un basculement vers les ENR ? Peut-on prédire cette évolution ?</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
