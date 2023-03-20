board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

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

# method to check if the game is over or not
def is_game_over():
    if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        return True
    else:
        return False


def is_valid_move(player, hole):
    if player == 1 and hole < 6 and board[hole] != 0:
        return True
    elif player == 2 and hole > 6 and hole < 13 and board[hole] != 0:
        return True
    else:
        return False

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

def evaluate(board):
    return board[6] - board[13]

def generate_moves(board):
    moves = []
    for i in range(6):
        if board[i] != 0:
            moves.append(i)
    return moves

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


# the minimax algo to find the best move for the player.
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
