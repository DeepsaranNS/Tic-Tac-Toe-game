from random import randint

def display_board(board):
    print("\n" * 100)

    print(f""" 
   tic-tac-toe
    {board[7]} | {board[8]} | {board[9]}
    ---------
    {board[4]} | {board[5]} | {board[6]}
    ---------
    {board[1]} | {board[2]} | {board[3]}
    """)

def player_input():
    marker = " "
    while marker not in ["X", "O"]:
        marker = input("Player 1,please choose your marker:[X or O]")
        if marker not in ["X", "O"]:
            print("Sorry please choose X or O")
    player_1 = marker
    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"

    return (player_1, player_2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    # checking the 8 possiblities,(i.e) 2 diagnols,centre row,centre column,and 4 corner sides.
    if board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark or board[7] == board[4] == \
            board[1] == mark or board[7] == board[8] == board[9] == mark or board[9] == board[6] == board[3] == mark or \
            board[1] == board[2] == board[3] == mark or board[8] == board[5] == board[2] == mark or board[4] == board[
        5] == board[6] == mark:
        return True
    else:
        return False

def choose_first():
    if randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == ""

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

def replay():
    return input("Do you want to play again?:['Yes','No']").lower().startswith("y")

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [""] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    game_on = True

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            print(turn + " will play first!")
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("This game is a Tie")
                    game_on = False
                    break
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            print(turn + " will play first!")
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won the game!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("This game is a Tie")
                    game_on = False
                    break
                else:
                    turn = "Player 1"

    if not replay():
        break




