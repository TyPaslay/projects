"""Setting up the game"""

#random module required for placing the battleship
from random import randint

#Creating a gameboard. Default is 5x5.
#Can be changed by changing the 5s in reset_board to any number.
board = []

#Sets up a fresh game board
def reset_board(board):
    del board[0:len(board)]
    for i in range(0,5):
        board.append(['O'] * 5)

#Prints current board without the displaying syntax at the start of each turn
def print_board(board):
    for row in board:
        print(' '.join(row))

#Functions to randomize battleship location
#-1 used to account for Python indexing
def rand_row(board):
    return randint(0,len(board) - 1)
def rand_col(board):
    return randint(0,len(board) - 1)

"""User input section"""

print("=====Welcome to Battleship!=====\n")
#Sets turn to 0, resets gameboard and randomly places battleship
turn = 0
reset_board(board)
battleship = [rand_row(board)], [rand_col(board)]

#While loop that handles the game
while True:
    #Defines number of turns. Can be modified
    #Should not exceed length * width of game board
    if turn < 4:
        #Display current board, advance the turn and display turn number
        print(print_board(board))
        turn += 1
        print("\n=====Turn %s!=====\n" %turn)

        #User guesses where battleship is
        #-1 is used to offset Python indexing
        try:
            user_row = int(input("Which row? "))
            user_col = int(input("Which column? "))
            user_guess = [user_row - 1],[user_col - 1]

        #Exception for inputs that are not integers.
        except ValueError:
            print("That's not a number ya pox-face swine!")
            continue

        #Ensures user guesses are within the dimensions of the board
        if user_row > len(board) or user_col > len(board):
            print("That's not even in the ocean, ya scurvy bird!\n")

        #Ensures user hasn't already guessed that space
        elif board[user_row-1][user_col-1] == 'X':
            print("Ya already guessed that, ya damp squib!\n")

        #Checks user guess against battleship location
        elif user_guess == battleship:
            print("Congratulations! You sunk my Battleship!")

            #Asks user if they want to play again and resets game or quits
            play_again = input("Play again? (y/n)\n ")

            if play_again.lower() == 'y':
                turn = 0
                reset_board(board)
                battleship = [rand_row(board)], [rand_col(board)]
                print("=====Welcome to Battleship!=====\n")
                continue
            elif play_again.lower() == 'n':
                break
            else:
                print("That is not a valid response")
        else:
            #If user misses battleship, notify them and mark space on board
            print("\nMiss!\n")
            board[user_row-1][user_col-1] = 'X'

    #If user runs out of turns, ask to play again. Reset or quit based on answer.
    else:
        print("Game Over!")
        play_again = input("Play again? (y/n)\n ")
        if play_again.lower() == 'y':
            turn = 0
            reset_board(board)
            battleship = [rand_row(board)], [rand_col(board)]
            print("=====Welcome to Battleship!=====\n")
            continue
        elif play_again.lower() == 'n':
            break
        else:
            print("That is not a valid response")

#On quit print salutation.
print("\nThanks for playing!")
