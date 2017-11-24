class Game:

    def __init__(self):
        self._score = 0
        self._rolls = []

    def roll(self, pins):
        self._score += pins
        self._rolls.append(pins)

    def score(self):
        score = 0
        i = 0
        for i in range(10):
            score += self._rolls[i] + self._rolls[i+1]
            i += 2
        return score
