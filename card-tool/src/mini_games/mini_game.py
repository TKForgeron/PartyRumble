class MiniGame:
    def __init__(
        self, title, category, explanation, task, solution=None, player_mode=None
    ):
        self.title = title
        self.category = category
        self.explanation = explanation
        self.task = task
        self.solution = solution
        self.player_mode = player_mode

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title") or data.get("titel"),
            category=data.get("category") or data.get("categorie"),
            explanation=data.get("explanation") or data.get("uitleg"),
            task=data.get("task") or data.get("opdracht"),
            solution=data.get("solution") or data.get("oplossing"),
            player_mode=data.get("player_mode") or data.get("vorm"),
        )

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "explanation": self.explanation,
            "task": self.task,
            "solution": self.solution,
            "player_mode": self.player_mode,
        }

    def __repr__(self):
        return (
            f"MiniGame(title={self.title!r}, category={self.category!r}, "
            f"explanation={self.explanation!r}, task={self.task!r}, solution={self.solution!r}, player_mode={self.player_mode!r})"
        )
