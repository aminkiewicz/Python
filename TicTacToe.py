from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|  ", board[row][col], "  ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        move = int(input("Enter your move: "))

        if move < 1 and move > 9:
            print("Please choose number ranging from 1 to 9.")
            continue
        elif move not in board[0] and move not in board[1] and move not in board[2]:
            print("This field is already taken! Please choose another field.")
            continue
        else:
            break

    for row in range(3):
        for column in range(3):
            if board[row][column] == move:
                board[row][column] = "O"


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free = []

    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["X", "O"]:
                free.append(([row], [column]))
    return free


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[2][1] == sign and board[2][0] == sign:
        return True
    else:
        return


def draw_move(board):
    # The function draws the computer's move and updates the board.

    free = make_list_of_free_fields(board)
    while True:

        row = randrange(3)
        column = randrange(3)

        if ([row], [column]) not in free:
            continue
        else:
            board[row][column] = "X"
            return


#Creating the board.
board = [[0 for r in range(3)] for c in range(3)]

board[0][0] = 1
board[0][1] = 2
board[0][2] = 3
board[1][0] = 4
board[1][1] = "X"
board[1][2] = 6
board[2][0] = 7
board[2][1] = 8
board[2][2] = 9

number_of_moves = 1
human = 'O'
computer = "X"

print("Welcome to Tic-Tac-Toe game. Good luck!")
print("I will start.")


while number_of_moves < 9:
    # User's turn.
    display_board(board)
    print()
    print("Your turn!")
    enter_move(board)
    number_of_moves += 1
    display_board(board)

    if victory_for(board, human) == True:
        print("You won! Congrats!")
        break
    else:
        free = make_list_of_free_fields(board)

    # Computer's turn.
    print()
    print("My turn!")
    draw_move(board)
    number_of_moves += 1

    if victory_for(board, computer) == True:
        display_board(board)
        print("I won!")
        break
    else:
        free = make_list_of_free_fields(board)

#End of the game.
else:
    display_board(board)
    print("It's a tie!")

print("Thanks for playing!")