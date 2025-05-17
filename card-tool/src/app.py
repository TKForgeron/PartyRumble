import random
import streamlit as st
from utils.cards_loader import load_json
from decks.deck_manager import DeckManager

deck_manager = DeckManager(
    file_loader=load_json,
    game_cards_file_path="data/mini_games.json",
    game_card_variants_path="data/mini_games_variants.json",
)

st.title("Party Rumble Card Tool")

categories = deck_manager.get_available_categories()
category = st.selectbox("Kies een categorie:", categories)

if st.button("Trek een kaart"):
    try:
        card = deck_manager.draw_card(category)
        st.subheader(card["titel"])

        vorm = (
            random.choice(card["vorm"])
            if isinstance(card["vorm"], list)
            else card["vorm"]
        )
        st.write(f"**Vorm:** {vorm}")
        st.write(f"**Uitleg:** {card['uitleg']}")
    except ValueError as e:
        st.error(str(e))
