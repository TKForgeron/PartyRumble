import random
import streamlit as st
from utils.cards_loader import load_json
from decks.deck_manager import DeckManager
from mini_games.mini_game import MiniGame


def get_badge(x):
    return f":orange-badge[{x}]"


def prefix_with_index(lst):
    return [f"{i + 1}. {item}" for i, item in enumerate(lst)]


# Initialize DeckManager only once and store it in session state
if "deck_manager" not in st.session_state:
    st.session_state.deck_manager = DeckManager(
        file_loader=load_json,
        game_cards_file_path="data/mini_games.json",
        game_variants_path="data/mini_games_variants.json",
    )

deck_manager = st.session_state.deck_manager  # Access the stored DeckManager

st.title("Party Rumble 🎉🍻")  # Set the app title

# Get available categories and assign color codes for display
categories = deck_manager.get_available_categories()
color_codes = ["🟥", "🟩", "🟦", "🟪", "🍀"]
categories_with_colors = [
    f"{color} {cat}" for color, cat in zip(color_codes, categories)
]

# Let the user select a category (strip off the color code for logic)
category = st.selectbox("Kies een categorie:", categories_with_colors)[2:]

# Initialize session state for mini_game and mode if not already set
if "mini_game" not in st.session_state:
    st.session_state.mini_game = None

# When the button is pressed, draw a new card and store it in session state
if st.button("♠️ Trek een kaart"):
    mini_game = deck_manager.draw_card(category)
    st.session_state.mini_game = mini_game


# If a mini_game is stored in session state, display its details
if st.session_state.mini_game:
    mini_game = st.session_state.mini_game
    st.subheader(mini_game.title)  # Show the game title
    # Example list of strings (player modes)
    player_modes = mini_game.player_mode

    # Generate badges using HTML
    badges_html = " ".join(
        [
            f'<span style="background-color:#E95420; color:white; padding:5px 10px; border-radius:5px; margin-right:5px;">{mode}</span>'
            for mode in player_modes
        ]
    )

    # Display the badges using st.markdown
    st.markdown(badges_html, unsafe_allow_html=True)
    if "<br>" in mini_game.task:
        items = mini_game.task.split("<br>")
        for item in prefix_with_index(items):
            st.write(item)
    else:
        st.write(f"{mini_game.task}")  # Show the task/instruction
    # Toggle to show/hide the solution
    show_solution = st.toggle(
        "Toon oplossing",
        value=False,
        key=f"show_solution_{mini_game.title}",
    )
    if show_solution and mini_game.solution:
        st.info(f"{mini_game.solution}")  # Show the solution if toggled on
    # Optionally show the raw dict for debugging
    # st.write(mini_game.to_dict())
