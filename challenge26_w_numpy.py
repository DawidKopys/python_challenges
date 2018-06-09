# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
# 	     [2, 1, 0],
# 	     [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.
import numpy

def tic_tac_toe_find_winner(board):
    board_t = numpy.transpose(board)
    board_t = [list(board_t[0]), list(board_t[1]), list(board_t[2])]
    if [1, 1, 1] in board or [1, 1, 1] in board_t:
        return 1
    elif [2, 2, 2] in board or [2, 2, 2] in board_t:
        return 2
    # diagonal match
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1]

    return 0

def present(board):
    for el in board:
        print(el)
    print(tic_tac_toe_find_winner(board), end='\n\n')

if __name__=='__main__':
    winner_is_2 = [[2, 2, 0],
        	       [2, 1, 0],
        	       [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
    	           [2, 1, 0],
    	           [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
    	                [2, 1, 0],
    	                [2, 1, 1]]

    winner_is_also_11 = [[1, 1, 1],
    	                [2, 1, 0],
    	                [2, 2, 1]]

    no_winner = [[1, 2, 0],
    	         [2, 1, 0],
    	         [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
    	              [2, 1, 0],
    	              [2, 1, 0]]

    present(winner_is_2)
    present(winner_is_1)
    present(winner_is_also_1)
    present(winner_is_also_11)
    present(no_winner)
    present(also_no_winner)
