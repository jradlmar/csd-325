"""Cho-Han, by Al Sweigart
Modified by Jared Morris
Module 3 Assignment

Changes made:
1. Changed the input prompt to use my initials: jm:
2. Changed the house fee from 10 percent to 12 percent.
3. Added a program notice explaining that rolling a 2 or 7 gives a 10 mon bonus.
4. Added logic to give the player a 10 mon bonus if the dice total is 2 or 7.
"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus Rule: If the dice roll equals 2 or 7, you get a 10 mon bonus!
''')

purse = 5000

while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:
        pot = input('jm: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('jm: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    if roll_total == 2 or roll_total == 7:
        print('The total roll was', roll_total, 'so you get a 10 mon bonus!')
        purse = purse + 10

    rollIsEven = roll_total % 2 == 0

    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        print('The house collects a', pot * 12 // 100, 'mon fee.')
        purse = purse - (pot * 12 // 100)
    else:
        purse = purse - pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()