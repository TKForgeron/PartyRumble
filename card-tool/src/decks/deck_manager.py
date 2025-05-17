from utils.deck_utils import remove_duplicates, shuffle_decks, enrich_with_variants


class DeckManager:
    def __init__(
        self,
        file_loader,
        game_cards_file_path: str,
        game_card_variants_path: str = None,
    ):
        self.game_cards_file_path = game_cards_file_path
        self.game_card_variants_path = game_card_variants_path
        self.decks = self.load_decks(file_loader)
        self.available_categories = self.get_available_categories()

    def load_decks(self, file_loader):
        data = file_loader(self.game_cards_file_path)
        # Optionally enrich with variants
        # if self.game_card_variants_path:
        #     card_variants = file_loader(self.game_card_variants_path)
        #     data = enrich_with_variants(data, card_variants)
        # Remove duplicates
        data = remove_duplicates(data)
        # Group by category
        decks = {}
        for game in data:
            cat = game["categorie"].lower()
            decks.setdefault(cat, []).append(game)
        # Shuffle decks
        shuffle_decks(decks)
        return decks

    def draw_card(self, category):
        if category not in self.available_categories:
            raise ValueError(f"Categorie '{category}' bestaat niet.")
        if not self.decks[category]:
            raise ValueError(
                f"Geen kaarten meer beschikbaar in categorie '{category}'."
            )
        return self.decks[category].pop()

    def get_available_categories(self):
        return list(self.decks.keys())
