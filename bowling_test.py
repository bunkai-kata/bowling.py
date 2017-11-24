from bowling import *

def test_gutter_game():
    g = Game()

    for i in range(20):
        g.roll(0)

    assert 0 == g.score()

def test_all_ones():
    g = Game()

    for i in range(20):
        g.roll(1)

    assert 20 == g.score()
