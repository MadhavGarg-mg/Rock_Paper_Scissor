"""This is a rock paper scissors game made in python"""
import random

games_played = 0
games_won = 0
games_drawn = 0

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
# https://www.asciiart.eu/people/body-parts/hand-gestures
# Rock, paper, scissors by Veronica Karlsson

while True:
    games_played += 1
    user_choice = input('What will you choose? Rock, Paper, or Scissor: \n').lower()
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)
    while user_choice not in choices:
        print('Invalid input!')
        user_choice = input('What will you choose? Rock, Paper, or Scissor: \n').lower()

    if user_choice == 'rock' and computer_choice == 'rock':
        print('Your Choice')
        print(rock)
        print('Computer\'s choice')
        print(rock)
        print('You have drawn!')
        games_drawn += 1
    elif user_choice == 'rock' and computer_choice == 'paper':
        print('Your Choice')
        print(rock)
        print('Computer\'s choice')
        print(paper)
        print('You have lost!')
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print('Your Choice')
        print(rock)
        print('Computer\'s choice')
        print(scissors)
        print('You have won!')
        games_won += 1
    elif user_choice == 'paper' and computer_choice == 'paper':
        print('Your Choice')
        print(paper)
        print('Computer\'s choice')
        print(paper)
        print('You have drawn!')
        games_drawn += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('Your Choice')
        print(paper)
        print('Computer\'s choice')
        print(rock)
        print('You have won!')
        games_won += 1
    elif user_choice == 'paper' and computer_choice == 'scissor':
        print('Your Choice')
        print(paper)
        print('Computer\'s choice')
        print(scissors)
        print('You have lost!')
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print('Your Choice')
        print(scissors)
        print('Computer\'s choice')
        print(paper)
        print('You have won!')
        games_won += 1
    elif user_choice == 'scissor' and computer_choice == 'rock':
        print('Your Choice')
        print(scissors)
        print('Computer\'s choice')
        print(rock)
        print('You have lost!')
    elif user_choice == 'scissor' and computer_choice == 'scissor':
        print('Your Choice')
        print(scissors)
        print('Computer\'s choice')
        print(scissors)
        print('You have drawn!')
        games_drawn += 1

    games_lost = games_played - (games_won + games_drawn)
    play_again = input('Play again? Y or N: \n').lower()
    while play_again not in ['y', 'n']:
        play_again = input('Play again? Y or N: \n').lower()
    if play_again != 'y':
        print(f'You played {games_played} game -> won {games_won}, drew {games_drawn}, '
              f'and lost {games_lost}.')
        break
