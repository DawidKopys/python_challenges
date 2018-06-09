from challenge24 import list_game_board, lst_to_str
from challenge26_w_numpy import tic_tac_toe_find_winner
from challenge27 import get_player_input, show_board

def insert_into_board(player_nr, graph_board, row, col):
    if row == 0:
        row = 1
    elif row == 1:
        row = 3
    elif row == 2:
        row = 5

    if col == 0:
        col = 2
    elif col == 1:
        col = 6
    elif col == 2:
        col = 10

    if player_nr == 2:
        mark = 'x'
    elif player_nr == 1:
        mark = 'o'

    graph_board[row] = graph_board[row][:col] + mark + graph_board[row][col+1:]


if __name__=='__main__':
    winner = 0
    board = [[0,0,0], [0,0,0], [0,0,0]]
    gr_board = list_game_board(3,3)
    print(lst_to_str(gr_board))
    print('Welcome in Tic Tac Toe game!')
    while winner == 0:
        pos = get_player_input(1, board)
        row = pos[0]
        col = pos[1]
        insert_into_board(1, gr_board, row, col)
        show_board(board)
        print(lst_to_str(gr_board))

        winner = tic_tac_toe_find_winner(board)
        if winner != 0:
            break

        pos = get_player_input(2, board)
        row = pos[0]
        col = pos[1]
        insert_into_board(2, gr_board, row, col)
        show_board(board)
        print(lst_to_str(gr_board))

        winner = tic_tac_toe_find_winner(board)
    print('The winner is player number :', winner)
