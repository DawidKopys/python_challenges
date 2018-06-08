board = [[0,0,0], [0,0,0], [0,0,0]]

def show_board():
    for el in board:
        print(el)

def get_player_input(player_nr):
    if player_nr == 2:
        player = 'Player2: '
        mark = 'o'
    elif player_nr == 1:
        player = 'Player1: '
        mark = 'x'

    pos = input(player).split(', ')
    row = int(pos[0]) - 1
    col = int(pos[1]) - 1
    if board[row][col] == 0:
        board[row][col] = mark

show_board()
while 1:
    get_player_input(1)
    show_board()

    get_player_input(2)
    show_board()
