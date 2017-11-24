class Game:

    def __init__(self):
        self._score = 0
        self._pins = []

    def roll(self, pins):
        self._score += pins
        self._pins.append(pins)

    def score(self):
        score = 0
        for pins in self._pins:
            score += pins
        return self._score
