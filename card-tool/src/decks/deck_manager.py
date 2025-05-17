from typing import Callable, Any
from mini_games.mini_game import MiniGame
import copy


class DeckManager:
    def __init__(
        self,
        file_loader: Callable[[str], list[dict[str, Any]]],
        game_cards_file_path: str,
        game_variants_path: str,
    ):
        self.file_loader = file_loader
        self.game_cards_file_path: str = game_cards_file_path
        self.game_variants_path: str = game_variants_path
        self.original_decks: dict[str, list[MiniGame]] = self.load_decks(file_loader)
        self.decks: dict[str, list[MiniGame]] = copy.deepcopy(self.original_decks)
        self.available_categories: list[str] = self.get_available_categories()

    def load_decks(
        self, file_loader: Callable[[str], list[dict[str, Any]]]
    ) -> dict[str, list[MiniGame]]:
        games: list[dict[str, Any]] = file_loader(self.game_cards_file_path)
        variants: list[dict[str, Any]] = file_loader(self.game_variants_path)

        games_by_title: dict[str, dict[str, Any]] = {
            game["titel"]: game for game in games
        }

        mini_games: list[MiniGame] = []
        for variant in variants:
            base_game: dict[str, Any] | None = games_by_title.get(variant["titel"])
            if base_game:
                merged: dict[str, Any] = {**base_game, **variant}
                mini_game: MiniGame = MiniGame.from_dict(merged)
                mini_games.append(mini_game)
            else:
                # Optionally handle missing base game
                pass

        decks: dict[str, list[MiniGame]] = {}
        for mini_game in mini_games:
            cat: str = str(mini_game.category).lower()
            decks.setdefault(cat, []).append(mini_game)
        return decks

    def reshuffle_deck(self, category: str) -> None:
        self.decks[category] = copy.deepcopy(self.original_decks[category])

    def draw_card(self, category: str) -> MiniGame:
        if category not in self.available_categories:
            raise ValueError(f"Categorie '{category}' bestaat niet.")
        if not self.decks[category]:
            # self.reshuffle_deck(category)
            self.decks[category] = self.load_decks(self.file_loader)[category]
        card = self.decks[category].pop()
        print("card popped:", card)
        return card

    def get_available_categories(self) -> list[str]:
        return list(self.decks.keys())
