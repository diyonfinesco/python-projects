from random import choice

ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR:  '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_guess = input(f'Rock, paper, or scissor? ({ROCK}/{PAPER}/{SCISSOR}): ').lower()

        if user_guess in choices:
            return user_guess
        
        print("Invalid choice")

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Game tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or 
        (user_choice == SCISSOR and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You won')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (y/n): ").lower()

        if should_continue == 'n':
            break

play_game()