import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

url = "streamlit3.csv"
users = pd.read_csv(url)
users = users.to_dict(orient="records")
dico_users = dict()
for user in users:
    dico_users.update({user["name"]: user})
dico_users = dict({"usernames": dico_users})
dico_users["root"] = {
    "name": "root",
    "password": "rootMDP",
    "email": "quilbeuf.e@wanadoo.fr",
    "failed_login_attemps": 0,  # Sera géré automatiquement
    "logged_in": False,  # Sera géré automatiquement
    "role": "administrateur",
}


authenticator = Authenticate(
    dico_users,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire
)

authenticator.login()


def accueil(selection):
    if selection == "Accueil":
        st.title("Bienvenue sur ce sublime site web... enjoy")
        st.image(
            "https://gifdb.com/images/high/standing-ovation-crowd-applause-oscar-awards-ai72icmh1ac7apdz.gif"
        )
        st.write("powered by Streamlit")
    elif selection == "Photos":
        st.header("Voici 3 films à voir")
        st.subheader(" :rainbow: 3 films, 3 styles, 3 ambiances... :rainbow:")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("Le fabuleux destin d'Amélie Poulain")
            st.image(
                "https://antreducinema.fr/wp-content/uploads/2020/04/AMELIE-POULAIN.jpg"
            )

        with col2:
            st.write("Retour vers le futur // Back to the future")
            st.image(
                "https://fr.web.img6.acsta.net/c_310_420/pictures/22/07/22/15/00/2862661.jpg"
            )

        with col3:
            st.write("Astérix et Obélix : Mission Cléopâtre")
            st.image(
                "https://fr.web.img3.acsta.net/c_310_420/pictures/23/06/21/12/06/4953335.jpg"
            )
        st.video("https://www.youtube.com/watch?v=FBh0Bt5fmEo", autoplay=True)


if st.session_state["authentication_status"]:
    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue chèr(e): {st.session_state['name']}")
        selection = option_menu(menu_title=None, options=["Accueil", "Photos"])
    accueil(selection)


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
