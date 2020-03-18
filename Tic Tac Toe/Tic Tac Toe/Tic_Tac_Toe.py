# ---- Global Variables ----


# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#If game is still going 
game_still_going = True

#Who won? or tie?
winner = None


# Whos turn is it
current_player = "X"

def display_board():
    print(board[0]+ " | " + board[1] + " | " + board[2])
    print(board[3]+ " | " + board[4] + " | " + board[5])
    print(board[6]+ " | " + board[7] + " | " + board[8])
 
#Play a game of tic tac toe 
def play_game():

    #display initial board 
    display_board()

    #While the game is still going 
    while game_still_going:

        #handle a single of an player 
        handle_turn(current_player)

        #Check if the game has ended 
        check_if_game_over()

        #Flip to the other player
        flip_player()

    #Game has ended 
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")
  
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    #searches for invalid inputs
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. choose a position from 1-9:")

        position = int(position) - 1 

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")

 

    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #Set up global variables 
    global winner 

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    #Get the row winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None 
    return

def check_rows(): 
    #set up global variables
    global game_still_going
    #check if any of the rows have all the same values (an is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False 
    #return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return borad[6]
    return


def check_columns():
    #set up global variables
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False 
    #return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return borad[2]
    return


def check_diagonals():
    #set up global variables
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False 
    #return the winner (X or O)
    if diagonals_1 :
        return board[0]
    elif diagonals_2:
        return board[2]
    return
 

def check_if_tie():
    #global variable neededw
    global game_still_going 
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #global variable we need
    global current_player
    #if current player X we change it to O
    if current_player == "X":
        current_player = "O"
    #if current player O we change it to X
    elif current_player == "O":
        current_player = "X"

    return
    



play_game()

#board
#display board
#play game
#check win
    #check rows
    #check columns 
    #check diagonals 
#check tie
#flip player