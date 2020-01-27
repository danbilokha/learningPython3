from games.guess.guess import (guess_game, number_of_available_guesses)
from games.snake.snake import snake_game


def play_guess():
    print('Number of guesses are %a' % number_of_available_guesses)
    guess_game()


def play_snake():
    snake_game()
