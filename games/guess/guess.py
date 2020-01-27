import random

__all__ = ['guess_game', 'number_of_available_guesses']

number_of_available_guesses = 6


def guess_game():
    guesses_made = 0
    number = random.randint(0, 20)
    name = input('Tell me your name.\n')

    print('So let\'s play the game. Guess the number from 0 to 20, {0}. '
          'Number of available guesses are {1}'.format(name, number_of_available_guesses))

    while guesses_made < number_of_available_guesses:
        guess = int(input('Make a guess: '))
        guesses_made += 1

        if guess < number:
            print('Too low')
        elif guess > number:
            print('Too high')
        else:
            print('Right!')
            break
