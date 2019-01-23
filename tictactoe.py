import random


def get_players():
    letter = ''
    while letter not in ('X', 'O'):
        letter = str(input('Do you want to be X or O? '))

    return ('X', 'O') if letter.upper() == 'X' else ('O', 'X')


def get_first_turn():
    return 'X' if random.randint(0, 1) else 'O'


def game_over(board):
    return is_board_full(board) or is_winner(board, 'X') or is_winner(board, 'O')


def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])


def get_player_move(board):
    move = ''
    while move not in (1, 2, 3, 4, 5, 6, 7, 8, 9) or board[move] != ' ':
        move = int(input('What is your next move? (1-9) '))
    return move


def get_cpu_move(board, cpu):  # TODO - add fork opportunities
    # check if cpu can win with next move
    for i in range(1, 10):
        if board[i] == ' ' and test_win_move(board, i, cpu):
            return i

    # check if player can win with next move - block player if so
    player = 'X' if cpu == 'O' else 'O'
    for i in range(1, 10):
        if board[i] == ' ' and test_win_move(board, i, player):
            return i

    # take free corner
    for i in (1, 3, 5, 7):
        if board[i] == ' ':
            return i

    # take free center
    if board[5] == ' ':
        return 5

    # take free side
    for i in (2, 4, 6, 8):
        if board[i] == ' ':
            return i


def get_winner(board):
    if is_winner(board, 'X'):
        return 'X'
    elif is_winner(board, 'O'):
        return 'O'
    else:
        return None


def is_winner(board, player):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
                        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # cols
                        [1, 5, 9], [3, 5, 7]]  # diagonals

    for combo in win_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True

    return False


def is_board_full(board):
    for i in range(1, 9):
        if board[i] == ' ':
            return False
    return True


def test_win_move(board, move, mark):
    board_copy = board.copy()
    board_copy[move] = mark
    return is_winner(board_copy, mark)


def main():
    # initialize board and players
    board = [' '] * 10  # ignore 0 index

    player, cpu = get_players()
    turn = get_first_turn()

    if turn == player:
        print('You will go first!')
    else:
        print('The computer will go first.')

    # main game thread
    while not game_over(board):
        if turn == player:
            print_board(board)
            move = get_player_move(board)
            board[move] = player
        else:
            print_board(board)
            move = get_cpu_move(board, cpu)
            board[move] = cpu

        # switch turns
        turn = cpu if turn == player else player

    # print game board after final move
    print_board(board)

    # get winner
    winner = get_winner(board)
    if winner is not None:
        if winner == player:
            print('You won!')
        else:
            print('The CPU won! Sorry.')
    else:
        print('It was a tie - no one won.')


if __name__ == "__main__":
    main()
