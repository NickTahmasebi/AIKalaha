board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

#This method just prints the initial board
def print_board():
    print("  {12}{11}{10}{9}{8}{7}\n")

    print("   ", end="")
    for i in range(12, 6, -1):
        print("{:2d} ".format(board[i]), end="")
    print("\n{:2d}".format(board[13]), " "*16, "{:2d}".format(board[6]))
    print("   ", end="")
    for i in range(0, 6):
        print("{:2d} ".format(board[i]), end="")
    print("\n")
    print("   {0}{1}{2}{3}{4}{5}")

# Method to check if the game is over or not
def is_game_over():
    if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return True
    else:
        return False

#Checks if player one chooses a hole from 0-6 and player two from 7-12
def is_valid_move(player, hole):
    if player == 1 and hole < 6 and board[hole] != 0:
        return True
    elif player == 2 and hole > 6 and hole < 13 and board[hole] != 0:
        return True
    else:
        return False

#Puts stones in the correct holes after a move is chosen
def make_move(player, hole):
    stones = board[hole]
    board[hole] = 0
    while stones > 0:
        hole = (hole + 1) % 14
        if player == 1 and hole == 13:
            continue
        if player == 2 and hole == 6:
            continue
        board[hole] += 1
        stones -= 1

#Compares the goals of player 1 and 2
def evaluate(board):
    return board[6] - board[13]

#Generates a list of valid moves for player 1
def generate_moves(board):
    moves = []
    for i in range(6):
        if board[i] != 0:
            moves.append(i)
    return moves

#Returns a board after a move would have been made, to be used by minimax to find the best move
def apply_move(board, move):
    player = board[13]
    nextBoard = board.copy()
    seeds = nextBoard[move]
    nextBoard[move] = 0
    i = move + 1
    while seeds > 0:
        if i == 12 and player == 0:
            i = 0
        elif i == 5 and player == 1:
            i = 7
        nextBoard[i] += 1
        seeds -= 1
        i = (i + 1) % 14
    if i == 5 and player == 0:
        nextBoard[5] += 1
    elif i == 12 and player == 1:
        nextBoard[12] += 1
    elif nextBoard[i] == 1 and ((i < 5 and player == 0) or (i > 5 and i < 12 and player == 1)):
        opposite = 11 - i
        nextBoard[player * 7 + 5] += nextBoard[opposite] + 1
        nextBoard[opposite] = 0
    nextBoard[13] = 1 - player
    return nextBoard


# the minimax algo to find the value of a designated move for player 1.
def minimax(board, depth, maxPlayer):
    if depth == 0 or board[6] == 0 or board[13] == 0:
        return evaluate(board)
    if maxPlayer:

        bestValue = -float("inf")
        for move in generate_moves(board):
            nextBoard = apply_move(board, move)
            value = minimax(nextBoard, depth-1, False)
            bestValue = max(bestValue, value)
        return bestValue
    else:
        bestValue = float("inf")
        for move in generate_moves(board):
            nextBoard = apply_move(board, move)
            value = minimax(nextBoard, depth-1, True)
            bestValue = min(bestValue, value)
        return bestValue

#Method uses the minimax method with a designated depth and selects the move with the highest value
def choose_move(board, depth):
    moves = generate_moves(board)
    bestValue = -float("inf")
    bestMove = None
    for move in moves:
        nextBoard = apply_move(board, move)
        value = minimax(nextBoard, depth-1, False)
        if value > bestValue:
            bestValue = value
            bestMove = move
    return bestMove

#Just the gameloop that runs until the game is over
def play_game():
    player = 1
    while not is_game_over():
        print_board()
        move = choose_move(board, 8)
        if player==1:
            print("Best move:", move)
            hole = int(input("Player " + str(player) + ", choose a hole (0-5):  "))
        else:
            hole = int(input("Player " + str(player) + ", choose a hole (7-12):  "))

        if is_valid_move(player, hole):
            make_move(player, hole)
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print("Invalid move. Please try again. ")
#Method compares the final score between player 1 and 2
def determine_winner():
    if board[6] > board[13]:
        print("Player 1 wins!")
    elif board[6] < board[13]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

play_game()
determine_winner()