import random
import time

BOARD = [" "] * 9
PLAYER = "X"


def print_board():
    print("\n")
    print(f"{BOARD[0]} | {BOARD[1]} | {BOARD[2]}")
    print("--|---|--")
    print(f"{BOARD[3]} | {BOARD[4]} | {BOARD[5]}")
    print("--|---|--")
    print(f"{BOARD[6]} | {BOARD[7]} | {BOARD[8]}")
    print("\n")


def player_move():
    global PLAYER
    print(f"Player {PLAYER}'s Turn.")
    move = int(input("Enter place between 1-9: ")) - 1  # Subtract 1 to match list indexing
    if BOARD[move] == " ":
        BOARD[move] = PLAYER
    else:
        print("This spot is already taken! Try again.")
        player_move()


def ai_move():
    print("Player O's Turn.")
    time.sleep(2)
    move = random.randint(0, 8)  # Correct range to 0-8
    if BOARD[move] == " ":
        BOARD[move] = "O"
    else:
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
    return " " not in BOARD


def tic_tac_toe():
    game_running = True

    while game_running:
        print_board()
        player_move()
        if check_winner(BOARD, "X"):
            print_board()
            print("Player X has won!")
            game_running = False
            break
        if board_full():
            print_board()
            print("It's a draw!")
            game_running = False
            break

        ai_move()
        if check_winner(BOARD, "O"):
            print_board()
            print("Player O has won!")
            game_running = False
            break
        if board_full():
            print_board()
            print("It's a draw!")
            game_running = False
            break


print('''  1 | 2 | 3
 ----------- 
  4 | 5 | 6
 -----------
  7 | 8 | 9
''')
print("Welcome to Haider's Tic Tac Toe Assignment")
tic_tac_toe()
