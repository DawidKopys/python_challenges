board = [[0,0,0], [0,0,0], [0,0,0]]

def show_board(board):
    for el in board:
        print(el)

def get_player_input(player_nr, board):
    if player_nr == 2:
        player = 'Player2: '
        mark = 2
    elif player_nr == 1:
        player = 'Player1: '
        mark = 1

    pos = input(player).split(', ')
    row = int(pos[0]) - 1
    col = int(pos[1]) - 1
    if board[row][col] == 0:
        board[row][col] = mark

    return [row, col]

if __name__=='__main__':
    show_board()
    while 1:
        get_player_input(1, board)
        show_board(board)

        get_player_input(2, board)
        show_board(board)
