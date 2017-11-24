class Game:

    def __init__(self):
        self._score = 0
        self._rolls = []

    def roll(self, pins):
        self._score += pins
        self._rolls.append(pins)

    def score(self):
        score = 0
        rolls = self._rolls
        for i in range(len(self._rolls) - 1):
            if rolls[i] + rolls[i+1] == 10:
                score += rolls[i+2]
            score += self._rolls[i]
        return score
