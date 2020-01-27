# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# import random
#
#
# def guess_game():
#     guesses_made = 0
#     number = random.randint(0, 20)
#     name = input('Tell me your name.\n')
#
#     print('So let\'s play the game. Guess the number from 0 to 20, {0}'.format(name))
#
#     while guesses_made < 6:
#         guess = int(input('Make a guess: '))
#         guesses_made += 1
#
#         if guess < number:
#             print('Too low')
#         elif guess > number:
#             print('Too high')
#         else:
#             print('Right!')
#             break
#
# guess_game

# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# import itertools
#
#
# def iter_primes():
#     # an iterator of all numbers between 2 and +infinity
#     numbers = itertools.count(2)
#
#     # generate primes forever
#     while True:
#         # get the first number from the iterator (always a prime)
#         prime = next(numbers)
#         yield prime
#
#         # this code iteratively builds up a chain of
#         # filters...slightly tricky, but ponder it a bit
#         numbers = filter(prime.__rmod__, numbers)
#
#
# for p in iter_primes():
#     if p > 1000:
#         break
#     print(p)

# BOARD_SIZE = 8
#
#
# def under_attack(col, queens):
#     left = right = col
#
#     for r, c in reversed(queens):
#         left, right = left - 1, right + 1
#
#         if c in (left, col, right):
#             return True
#     return False
#
#
# def solve(n):
#     if n == 0:
#         return [[]]
#
#     smaller_solutions = solve(n - 1)
#
#     return [solution + [(n, i + 1)]
#             for i in range(BOARD_SIZE)
#             for solution in smaller_solutions
#             if not under_attack(i + 1, solution)]
#
#
# for answer in solve(BOARD_SIZE):
#     print(answer)

# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# import csv
#
#
# # need to define cmp function in Python 3
# def cmp(a, b):
#     return (a > b) - (a < b)
#
#
# # write stocks data as comma-separated values
# with open('stocks.csv', 'w', newline='') as stocksFileW:
#     writer = csv.writer(stocksFileW)
#     writer.writerows([
#         ['GOOG', 'Google, Inc.', 505.24, 0.47, 0.09],
#         ['YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22],
#         ['CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.4901]
#     ])
#
# # read stocks data, print status messages
# with open('stocks.csv', 'r') as stocksFile:
#     stocks = csv.reader(stocksFile)
#
#     status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
#     for ticker, name, price, change, pct in stocks:
#         status = status_labels[cmp(float(change), 0.0)]
#         print('%s is %s (%.2f). Current price is %s' % (name, status, float(pct), price))

# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# import unittest

#
# def median(pool):
#     '''Statistical median to demonstrate doctest.
#         >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
#         6 #change to 7 in order to pass the test
#         '''
#     copy = sorted(pool)
#     size = len(copy)
#     if size % 2 == 1:
#         return copy[int((size - 1) / 2)]
#     else:
#         return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()

# import unittest
#
#
# def median(pool):
#     copy = sorted(pool)
#     size = len(copy)
#     if size % 2 == 1:
#         return copy[int((size - 1) / 2)]
#     else:
#         return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2
#
#
# class TestMedian(unittest.TestCase):
#     def testMedian(self):
#         self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print('You\'ve successfully deposited', amount)
#
#     def withdraw(self, amount):
#         after_withdrawal = self.balance - amount
#         if after_withdrawal < 0:
#             print('Cannot withdraw, you have only %s, but trying to withdraw %s.' % (self.balance, amount))
#         else:
#             self.balance = after_withdrawal
#             print('You\'ve received %s!' % amount)
#             print('You have %s left.' % self.balance)
#
#
# bankAccount = BankAccount(0)
# bankAccount.withdraw(5)
# bankAccount.deposit(15)
# bankAccount.withdraw(10)

# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# REFRAIN = '''
# %d bottles of beer on the wall,
# %d bottles of beer,
# take one down, pass it around,
# %d bottles of beer on the wall!
# '''
# bottles_of_beer = 9
#
# while bottles_of_beer > 1:
#     print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
#     bottles_of_beer -= 1


# ====-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #

# from time import localtime
#
# activities = {8: 'Sleeping',
#               9: 'Commuting',
#               17: 'Working',
#               18: 'Commuting',
#               20: 'Eating',
#               22: 'Resting'}
#
# timeNow = localtime()
# hour = timeNow.tm_hour
# print(timeNow, hour)
#
# for activityTime in sorted(activities.keys()):
#     print('For activity %s.' % activities[activityTime])
#
#     if hour < activityTime:
#         print('It\'s {time} for {activity}.'.format(
#             time=activityTime,
#             activity=activities[activityTime])
#         )
#         break
# else:
#     print('UNKNOWN')

# import glob
#
# python_files = glob.glob('*.py')
# for file in sorted(python_files):
#     print(file)
#
#     with open(file) as f:
#         for line in f:
#             print('          ', line.rstrip())

# import sys
#
# print(sys.argv)
#
# try:
#     print('sys.argv[1:]', sys.argv)
#     total = sum(int(arg) for arg in sys.argv[5:])
#     print(total)
# except ValueError:
#     print('Wrong value')

# basicList = [1, 2, 3, 4]
#
# basicList[1] = 'Changed'
# print(basicList)
#
# tupleList = tuple(basicList)
# for i, tLI in enumerate(tupleList):
#     print('Tuple list item {idx}: {name}'.format(idx=i, name=str(tLI)))
#
#
# def hi(name):
#     print('Hi, my name is ', name)
#
#
# hi('Dan')
