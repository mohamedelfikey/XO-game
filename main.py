import random

print("hello tic tac game")
print("--------------------------")

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
columns = 3


def print_game_board():
    for x in range(rows):
        print("\n+--+--+--+")
        print(" ", end="")
        for y in range(columns):
            print(game_board[x][y], end=" |")
    print("\n+--+--+--+")


### print_game_board()

def modify_array(num, turn):
    num -= 1
    if num == 0:
        game_board[0][0] = turn
    elif num == 1:
        game_board[0][1] = turn
    elif num == 2:
        game_board[0][2] = turn
    elif num == 3:
        game_board[1][0] = turn
    elif num == 4:
        game_board[1][1] = turn
    elif num == 5:
        game_board[1][2] = turn
    elif num == 6:
        game_board[2][0] = turn
    elif num == 7:
        game_board[2][1] = turn
    elif num == 8:
        game_board[2][2] = turn


def check_for_winner(game_board):
    ### x axis
    ### X won
    if (game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X"):
        print("X is won")
        return "X"
    elif (game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X"):
        print("X is won")
        return "X"
    elif (game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X"):
        print("X is won")
        return "X"
    ### O won
    elif (game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O"):
        print("O is won")
        return "O"
    elif (game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O"):
        print("O is won")
        return "O"
    elif (game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O"):
        print("O is won")
        return "O"
    ### y axis
    ### X won
    elif (game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X"):
        print("X is won")
        return "X"
    elif (game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X"):
        print("X is won")
        return "X"
    elif (game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X"):
        print("X is won")
        return "X"
    ### O won
    elif (game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O"):
        print("O is won")
        return "O"
    elif (game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O"):
        print("O is won")
        return "O"
    elif (game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O"):
        print("O is won")
        return "O"
    ### cross axis
    ### X won
    elif (game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X"):
        print("X is won")
        return "X"
    elif (game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X"):
        print("X is won")
        return "X"
    ### O won
    elif (game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O"):
        print("O is won")
        return "O"
    elif (game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O"):
        print("O is won")
        return "O"
    else:
        return "N"


leave_loops = False
# turn="X"
turn_counter = 0

while (leave_loops == False):
    ### it's the player turn
    if (turn_counter % 2 == 1):
        print_game_board()
        number_picked = int(input("\n choose number [1:9] "))
        if (number_picked >= 1) and (number_picked <= 9):
            modify_array(number_picked, "X")
            possible_numbers.remove(number_picked)
        else:
            print("invalid input please try again")
        turn_counter += 1
    ### it's the computer turn
    else:
        while True:
            computer_choice = random.choice(possible_numbers)
            print("\n computer choice", computer_choice)
            if (computer_choice in possible_numbers):
                modify_array(computer_choice, "O")
                possible_numbers.remove(computer_choice)
                turn_counter += 1
                break
    winner = check_for_winner(game_board)
    if (winner != "N"):
        print("\n Thank you for playing :)")
        break
