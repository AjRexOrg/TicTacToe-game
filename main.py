from tic_tac_toe import *

# The tic-tac-toe Game
print("------------WELCOME TO TIC TAC TOE-------------- \n")
#while True:
while True:
    #resting the board
    tictactoe = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_one, player_two = player_input()
    print(f'player one is {player_one}, player two is {player_two}')
    turn = choose_first()
    print(turn + ' Will be first.\n')

    lets_play = input('Are you ready to play Y or N:')
    if lets_play.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on is True:
        #Player 1 Turn
        if turn == 'player one':
            clear()
            display_board(tictactoe)
            position = player_choice(tictactoe)
            place_marker(tictactoe,player_one,position)

            if win_check(tictactoe, player_one):
                display_board(tictactoe)
                print('Congratulation player one has won the game !')
                game_on = False

            else:
                if full_board_check(tictactoe):
                    display_board(tictactoe)
                    print("it's a draw !")
                    break
                else:
                    turn = 'player two'
        else:
            #player two's turn
            if turn == 'player two':
                clear()
                display_board(tictactoe)
                position = player_choice(tictactoe)
                place_marker(tictactoe,player_two,position)

            if win_check(tictactoe, player_two):
                display_board(tictactoe)
                print('Congratulation player two has won the game !')
                game_on = False

            else:
                if full_board_check(tictactoe):
                    display_board(tictactoe)
                    print("it's a draw !")
                    break
                else:
                    turn = 'player one'

    if not replay():
        break
