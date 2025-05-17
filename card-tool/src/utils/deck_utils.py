def remove_duplicates(games):
    """Remove duplicate games based on 'titel' and 'categorie'."""
    seen = set()
    unique_games = []
    for game in games:
        key = (game.get("titel"), game.get("categorie"))
        if key not in seen:
            unique_games.append(game)
            seen.add(key)
    return unique_games


def shuffle_decks(decks, random_module=None):
    """Shuffle the cards in each deck."""
    import random

    rnd = random_module or random
    for deck in decks.values():
        rnd.shuffle(deck)


def enrich_with_variants(games, variants):
    """Add variants as new games, matching on 'titel'."""
    base_by_title = {g["titel"]: g for g in games}
    enriched = list(games)
    for variant in variants:
        titel = variant["titel"]
        if titel in base_by_title:
            base = base_by_title[titel]
            new_game = {
                "categorie": base["categorie"],
                "titel": base["titel"],
                "vorm": base.get("vorm", []),
                "uitleg": variant["uitleg"],
                "antwoord": variant.get("antwoord"),
            }
            enriched.append(new_game)
    return enriched
