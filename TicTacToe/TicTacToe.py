import copy
def winner(game_board, player):
    ''' winner(game_board, player) returns 1 if player has won, -1 for  tie, or 0 otherwise'''
    row = 0
    while row <= 2:
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            return 1
        row = row + 1

    col = 0
    while col <= 2:
        if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
            return 1
        col = col + 1

    if (game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player):
        return 1
    if (game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player):
        return 1

    play_count = 0
    row = 0
    while (row <= 2):
        col = 0
        while (col <= 2):
            if (game_board[row][col] != 0):
                play_count += 1
            col = col + 1
        row = row + 1
    
    if play_count == 9:
         return -1
    return 0


def print_board(board):
    ''' print_board(board) prints board so it is readable for the user'''

    row = 0
    
    print(" ____ ____ ____ ")
    print("|    |    |    |")
    print("| ", end = '')
    print_idx(board, 2, 0) 
    print(" | ", end = '')
    print_idx(board, 2, 1) 
    print(" | ", end = '')
    print_idx(board, 2, 2)
    print(" |")
    print(" ____ ____ ____ ")
    print("|    |    |    |")
    print("| ", end = '')
    print_idx(board, 1, 0) 
    print(" | ", end = '')
    print_idx(board, 1, 1) 
    print(" | ", end = '')
    print_idx(board, 1, 2)
    print(" |")
    print(" ____ ____ ____ ")
    print("|    |    |    |")
    print("| ", end = '')
    print_idx(board, 0, 0) 
    print(" | ", end = '')
    print_idx(board, 0, 1) 
    print(" | ", end = '')
    print_idx(board, 0, 2)
    print(" |")
    print(" ____ ____ ____ ")

def print_idx(board, indx_row, indx_col):
    val =board[indx_row][indx_col]
    if val == 1:
        print("X ", end = '')
    elif val == -1:
        print("O ", end = '')
    else:
        if indx_col == 0:
            print("A", end = '')
        elif indx_col == 1:
            print("B", end = '')
        elif indx_col == 2:
            print("C", end = '')
        print(str(indx_row + 1), end = '')




empty_board = [[0,0,0],
               [0,0,0,],
               [0,0,0]]
game_board = copy.deepcopy(empty_board)
X = 1
O = -1
play = True

player = X

print('''Welcome to Python Tic-Tac-Toe. The game is what it sounds like. You will enter any move as co-ordinates as shown on the board.
i.e. if you would like to place an X or A at A1, then type A1 when the prompt asks you to do so.
Let's get this party started!
''')
move_count = 0
while (play == True):
    if player == X:
        player_name =  "X"
    else:
        player_name = "O"
    if move_count == 0:
        print_board(game_board)
        move_count += 1
    print("")
    valid_input = False
    while (valid_input == False):
        move = input("Where would you like to place your " + player_name + " : ")
        if ((len(move) == 2) and (move[0] == "A" or move[0] == "B" or move[0] == "C") 
            and (move[1] == "1" or move[1] == '2' or move[1] == '3')):
            

            if move[0] == "A":
                col = 0
            elif move[0] == "B":
                col = 1
            elif move[0] == "C":
                col = 2

            row = int(move[1]) - 1

            if game_board[row][col] != 0:
                print("invalid move")
            else:
                valid_input = True

    game_board[row][col] = player
    print_board(game_board)
    won = winner(game_board, player)
    if (abs(won) == 1):
        
        invalid_ans = True
        while (invalid_ans == True):
            if won == 1:
                pl_ag = input(player_name + " won! Play again (Type YES or NO): ")
            else:
                pl_ag = input("Tie Game! Play again (Type YES or NO): ")
            if pl_ag == "YES":
               game_board = copy.deepcopy(empty_board)
               player = 1
               invalid_ans = False
               move_count = 0
            elif pl_ag == "NO":
                play = False
                invalid_ans = False
    elif won == 0:
        player = -1 * player
    









