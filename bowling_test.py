from bowling import *

def test_gutter_game():
    g = Game()

    for i in range(20):
        g.roll(0)

    assert 0 == g.score()
