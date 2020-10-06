import sys, os

def clear():
    os.system('cls')

# function that displays the board.
def display_board(board):
    print("------------TIC TAC TOE-------------- \n")
    print(' '+' '+' | '+' '+ ' | '+' ')
    print(' '+board[7] +' | '+ board[8]+' | '+board[9])
    print(' '+' '+' | '+' '+ ' | '+' ')
    print('------------')
    print(' '+' '+' | '+' '+ ' | '+' ')
    print(' '+board[4] +' | '+ board[5]+' | '+board[6])
    print(' '+' '+' | '+' '+ ' | '+' ')
    print('------------')
    print(' '+' '+' | '+' '+ ' | '+' ')
    print(' '+board[1] +' | '+ board[2]+' | '+board[3])
    print(' '+' '+' | '+' '+ ' | '+' ')

# Fucntion that takes in player input and assign place_marker
def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function that places player input and marker on board position
def place_marker(tictactoe,marker,position):
        tictactoe[position] = marker

# Function to check if player has won based on marker position on the full_board_check
def win_check(board, mark):
    # across the top
    return ((board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[4]==mark and board[5]==mark and board[6]==mark) or # across the middle
    (board[1]==mark and board[2]==mark and board[3]==mark) or # across the bottom
    (board[8]==mark and board[5]==mark and board[2]==mark) or # down the middle
    (board[7]==mark and board[4]==mark and board[1]==mark) or  # down the left
    (board[9]==mark and board[6]==mark and board[3]==mark) or  # down the right
    (board[7]==mark and board[5]==mark and board[3]==mark) or   # diagonal 1
    (board[9]==mark and board[5]==mark and board[1]==mark)) # diagonal 2

# Function that assigns turn by random
import random

def choose_first():
    random_no = random.randint(1,2)

    if random_no == 1:
        return 'Player one'
    elif random_no == 2:
        return'player two'
    else:
        print('broken code')
# Function that checks for available space on the board
#if there is space it returns True
def space_check(tictactoe,position):
    return tictactoe[position] == ' '

# Function that checks if board is full (Determines game draw)
def full_board_check(tictactoe):

    for i in range(len(tictactoe)):
        if space_check(tictactoe, i):
            return False
    return True

# Function that requests player's input
def player_choice(tictactoe):
    your_pick = int(input('Pick A next position from 1-9 ( keyboard Number pad ) : '))

    if space_check(tictactoe, your_pick):
        return your_pick

# Function that asks for replay
def replay():
    dontstop = True

    while dontstop is True:
        keep_going = input('Do you want to keep going (Y or N) :').lower()
        if keep_going == 'y':
            dontstop = False
            return True
        else:
            return False
