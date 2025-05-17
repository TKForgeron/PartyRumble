import random
import streamlit as st
from utils.cards_loader import load_json
from decks.deck_manager import DeckManager
from mini_games.mini_game import MiniGame

deck_manager = DeckManager(
    file_loader=load_json,
    game_cards_file_path="data/mini_games.json",
    game_variants_path="data/mini_games_variants.json",
)

st.title("Party Rumble")

categories = deck_manager.get_available_categories()
category = st.selectbox("Kies een categorie:", categories)

if st.button("Trek een kaart"):
    try:
        mini_game = deck_manager.draw_card(category)
        st.subheader(mini_game.title)

        st.write(f"**Vorm:** {mini_game.player_mode}")
        st.write(f"**Uitleg:** {mini_game.task}")
    except ValueError as e:
        st.error(str(e))
