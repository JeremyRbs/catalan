from http.client import responses

import streamlit as st
import random
from enum import Enum

from streamlit import columns

# Dictionnaire des mots français-catalans
mots = {
    "Bonjour": "Hola",
    "Merci": "Gràcies",
    "Bonjour tout le monde": "Hola a tothom",
    "Merci beaucoup": "Moltes gràcies"
}

class Step(Enum):
    INITIAL = 1
    PLACEHOLDER_SELECTION = 2
    PROCESSING = 3

    @classmethod
    def next_value(cls, current_value):
        next_value = (current_value.value % len(cls)) + 1
        return Step(next_value)


if "step" not in st.session_state:
    st.session_state.step = Step.INITIAL

colsPrincipal = st.columns([1])
cols = st.columns([1, 1])

def handle_placeholder_click(message=None, reponses_possibles=mots):
    # Mélange des questions
    mots_possibles = list(mots.items())
    random.shuffle(mots_possibles)

    # Initialisation des variables
    index = 0
    bonnes_reponses = 0
    fautes = []

    # Titre du test
    with colsPrincipal[0]:
        st.markdown("<h1 style='text-align: center; color: white;'>Catalan</h1>", unsafe_allow_html=True)

        # Affichage de la question et des boutons de réponses
        st.subheader(f"'toto' en catalan ?")

        if st.session_state.step == Step.PROCESSING:
            st.session_state.step = Step.INITIAL
        else:
            st.session_state.step = Step.next_value(st.session_state.step)

        if st.session_state.step.value == Step.INITIAL.value:
            st.button(
                "Démarrer le test",
                on_click=handle_placeholder_click,
                args=("",),
            )
        elif st.session_state.step.value == Step.PLACEHOLDER_SELECTION.value:
            with cols[0]:
                st.button(
                    reponses_possibles[0], use_container_width=True, on_click=handle_placeholder_click, args=(reponses_possibles[0],)
                )
            with cols[0]:
                st.button(
                    reponses_possibles[1], use_container_width=True, on_click=handle_placeholder_click, args=(reponses_possibles[1],)
                )
            with cols[1]:
                st.button(
                    reponses_possibles[2], use_container_width=True, on_click=handle_placeholder_click, args=(reponses_possibles[2],)
                )
            with cols[1]:
                st.button(
                    reponses_possibles[3], use_container_width=True, on_click=handle_placeholder_click, args=(reponses_possibles[3],)
                )
        else:
            st.write("The message has been sent and is being processed.")
            st.button("RESET", on_click=handle_placeholder_click, args=("RESET BUTTON",))

# Fonction pour gérer le test
def passer_test():
    # Mélange des questions
    mots_possibles = list(mots.items())
    random.shuffle(mots_possibles)

    # Initialisation des variables
    index = 0
    bonnes_reponses = 0
    fautes = []

    # Titre du test
    st.title("Catalan")

    # Variable pour suivre la question actuelle
    if 'index' not in st.session_state:
        st.session_state.index = 0
    if 'bonnes_reponses' not in st.session_state:
        st.session_state.bonnes_reponses = 0
    if 'fautes' not in st.session_state:
        st.session_state.fautes = []

    # Affichage de la question actuelle
    fr, ca = mots_possibles[st.session_state.index]

    # Liste des options possibles : on génère 3 fausses réponses et une correcte
    reponses_possibles = [ca]
    while len(reponses_possibles) < 4 :
        fausse_reponse = random.choice(list(mots.values()))
        if fausse_reponse != ca and fausse_reponse not in reponses_possibles:
            reponses_possibles.append(fausse_reponse)

    # Mélange des réponses pour que la bonne réponse ne soit pas toujours au même endroit
    random.shuffle(reponses_possibles)

    # Affichage de la question et des boutons de réponses
    st.subheader(f"'{fr}' en catalan ?")

    left, right = st.columns(2)
    # Variables pour vérifier la réponse
    reponse_correcte = False
    if left.button(reponses_possibles[0], use_container_width=True):
        if reponses_possibles[0].strip() == ca:
            reponse_correcte = True
            st.session_state.bonnes_reponses += 1
            st.success(f"Juste ! La traduction correcte de '{fr}' est '{ca}'.")
        else:
            reponse_correcte = False
            st.error(f"Faux ! La traduction correcte de '{fr}' est '{ca}', mais vous avez répondu '{reponses_possibles[0]}'.")
            st.session_state.fautes.append((fr, ca, reponses_possibles[0]))
    if right.button(reponses_possibles[1], use_container_width=True):
        if reponses_possibles[1].strip() == ca:
            reponse_correcte = True
            st.session_state.bonnes_reponses += 1
            st.success(f"Juste ! La traduction correcte de '{fr}' est '{ca}'.")
        else:
            reponse_correcte = False
            st.error(f"Faux ! La traduction correcte de '{fr}' est '{ca}', mais vous avez répondu '{reponses_possibles[1]}'.")
            st.session_state.fautes.append((fr, ca, reponses_possibles[1]))
    if left.button(reponses_possibles[2], use_container_width=True):
        if reponses_possibles[2].strip() == ca:
            reponse_correcte = True
            st.session_state.bonnes_reponses += 1
            st.success(f"Juste ! La traduction correcte de '{fr}' est '{ca}'.")
        else:
            reponse_correcte = False
            st.error(f"Faux ! La traduction correcte de '{fr}' est '{ca}', mais vous avez répondu '{reponses_possibles[2]}'.")
            st.session_state.fautes.append((fr, ca, reponses_possibles[2]))
    if right.button(reponses_possibles[3], use_container_width=True):
        if reponses_possibles[3].strip() == ca:
            reponse_correcte = True
            st.session_state.bonnes_reponses += 1
            st.success(f"Juste ! La traduction correcte de '{fr}' est '{ca}'.")
        else:
            reponse_correcte = False
            st.error(f"Faux ! La traduction correcte de '{fr}' est '{ca}', mais vous avez répondu '{reponses_possibles[3]}'.")
            st.session_state.fautes.append((fr, ca, reponses_possibles[3]))

    if st.button("Suivant"):
        st.session_state.index += 1

    # Vérification de la fin du test
    if st.session_state.index >= len(mots_possibles):
        # Calcul de la note finale
        note = (st.session_state.bonnes_reponses / len(mots)) * 100
        st.subheader(f"\nVotre note : {note:.2f}%")

        # Affichage des fautes
        if st.session_state.fautes:
            st.subheader("Fautes :")
            for (fr, ca, reponse) in st.session_state.fautes:
                st.error(f"Mot/phrase: '{fr}'\nAttendu: '{ca}'\nVotre réponse: '{reponse}'")
        else:
            st.success("Aucune faute ! Félicitations !")


if __name__ == "__main__":
    handle_placeholder_click()