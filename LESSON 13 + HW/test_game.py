# test_game

# START

import pytest
from game import validity_check, check_winner

# Testing validity_check function
def test_validity_check_rock():
    assert validity_check("rock") == 2

def test_validity_check_paper():
    assert validity_check("paper") == 0

def test_validity_check_scissors():
    assert validity_check("scissors") == 1

def test_validity_check_uppercase():
    assert validity_check("ROCK") == 2
    assert validity_check("PAPER") == 0
    assert validity_check("SCISSORS") == 1

def test_validity_check_invalid():
    with pytest.raises(ValueError):
        validity_check("invalid")

# Testing check_winner function
def test_check_winner_tie_rock():
    assert check_winner(2, 2) == 0

def test_check_winner_tie_paper():
    assert check_winner(0, 0) == 0

def test_check_winner_tie_scissors():
    assert check_winner(1, 1) == 0

def test_check_winner_player1_rock_scissors():
    assert check_winner(2, 1) == 1

def test_check_winner_player2_paper_rock():
    assert check_winner(0, 2) == 1

def test_check_winner_player1_paper_rock():
    assert check_winner(0, 2) == 1

def test_check_winner_player2_rock_paper():
    assert check_winner(2, 0) == 2

def test_check_winner_player1_scissors_paper():
    assert check_winner(1, 0) == 1

def test_check_winner_player2_scissors_rock():
    assert check_winner(1, 2) == 2

def test_check_winner_invalid():
    with pytest.raises(ValueError):
        check_winner(3, 1)

# END