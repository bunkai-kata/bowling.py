import pytest
from bowling import *

@pytest.fixture
def g():
    return Game()

def roll_many(g, n, pins):
    for i in range(n):
        g.roll(pins)

def roll_spare(g):
    g.roll(5)
    g.roll(5)

def roll_strike(g):
    g.roll(10)

def test_gutter_game(g):
    roll_many(g, 20, 0)
    assert 0 == g.score()

def test_all_ones(g):
    roll_many(g, 20, 1)
    assert 20 == g.score()

def test_one_spare(g):
    roll_spare(g)
    g.roll(3)
    roll_many(g, 17, 0)
    assert 16 == g.score()

def test_one_strike(g):
    roll_strike(g)
    g.roll(3)
    g.roll(4)
    roll_many(g, 16, 0)
    assert 24 == g.score()
