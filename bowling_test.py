import pytest
from bowling import *

@pytest.fixture
def g():
    return Game()

def roll_many(g, n, pins):
    for i in range(n):
        g.roll(pins)

def test_gutter_game(g):
    n = 20
    pins = 0
    roll_many(g, n, pins)

    assert 0 == g.score()

def test_all_ones(g):
    for i in range(20):
        g.roll(1)

    assert 20 == g.score()
