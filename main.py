import random
import time


BOARD = [" "] * 9
PLAYER = "X"


def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")



def player_move():
    print(f"Player {PLAYER}'s Turn.")
    move = int("Enter Place  between 1-9 : ")
    if BOARD[move]==" ":
        BOARD[move] = PLAYER
    else:
        print("This spot is already taken! Try again.")
        player_move()

def ai_move():
    print("Player O's Turn.")
    time.sleep(2)
    move = random.randint(0,9)
    if BOARD[move]==" ":
        BOARD[move] = "O"
    else:
        print("This spot is already taken! Try again.")
        ai_move()
    
def check_winner(board, mark):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark:
            return True
    return False

def board_full():
    if " " not in BOARD:
        return True
    return False

def tic_tac_toe():
    game_running = True

    while game_running:
        print_board()
        player_move()
        ai_move()
        if check_winner(BOARD, "X"):
            print("Player X has won")
            game_running = False
        elif check_winner(BOARD, "O"):
            print("Player O has won")
            game_running = False
        elif board_full():
            print("It's a draw")
            game_running = False
        
print('''  1 | 2 | 3
 -----------
  4 | 5 | 6
 -----------
  7 | 8 | 9
''')
print("Welcome to Haider's Tic Tac Toe Assigment")
tic_tac_toe()