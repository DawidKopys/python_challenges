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

def check_full(l_board):
    flat_board = [x for sublist in l_board for x in sublist]
    if 0 not in flat_board:
        u_d = input("check_full No winner, do you want to quit? \'q\' to quit, \'c\' to continue: ")
        return u_d

if __name__=='__main__':
    user_decision = ''
    winner = 0
    board = [[0,0,0], [0,0,0], [0,0,0]]
    gr_board = list_game_board(3,3)
    print('Welcome in Tic Tac Toe game!')
    print(lst_to_str(gr_board))

    while user_decision != 'q':
        # player1
        user_decision = check_full(board)
        if user_decision == 'c':
            board = [[0,0,0], [0,0,0], [0,0,0]]
            gr_board = list_game_board(3,3)
            continue

        pos = get_player_input(1, board)
        while pos == [-1, -1]:
            print('You cant place your mark there!')
            pos = get_player_input(1, board)
        row = pos[0]
        col = pos[1]
        insert_into_board(1, gr_board, row, col)
        show_board(board)
        print(lst_to_str(gr_board))

        winner = tic_tac_toe_find_winner(board)
        if winner != 0:
            print('The winner is player number :', winner)
            user_decision = input("Do you want to quit? \'q\' to quit, \'c\' to continue: ")
            if user_decision == 'c':
                board = [[0,0,0], [0,0,0], [0,0,0]]
                gr_board = list_game_board(3,3)
                continue

        # player2
        user_decision = check_full(board)
        if user_decision == 'c':
            board = [[0,0,0], [0,0,0], [0,0,0]]
            gr_board = list_game_board(3,3)
            continue

        pos = get_player_input(2, board)
        while pos == [-1, -1]:
            print('You cant place your mark there!')
            pos = get_player_input(2, board)
        row = pos[0]
        col = pos[1]
        insert_into_board(2, gr_board, row, col)
        show_board(board)
        print(lst_to_str(gr_board))

        winner = tic_tac_toe_find_winner(board)
        if winner != 0:
            print('The winner is player number :', winner)
            user_decision = input("Do you want to quit? \'q\' to quit, \'c\' to continue: ")

    print("Good bye!")
