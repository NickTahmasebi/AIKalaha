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


def is_valid_move(player, hole): #Nick
    if player == 1 and hole < 6 and board[hole] != 0:
        return True
    elif player == 2 and hole > 6 and hole < 13 and board[hole] != 0:
        return True
    else:
        return False

