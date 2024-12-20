from connect4 import init_board, place_piece, check_winner, play

def test_init_board():
    board = init_board(4, 3)
    assert len(board) == 4
    assert len(board[0]) == 3


def test_place_piece_validation():
    board = init_board(6, 7)
    new_board = place_piece('x', 7, 0, board)
    assert new_board == None
    new_board_2 = place_piece('x', 5, 7, board)
    assert new_board_2 == None


def test_place_piece_success():
    board = init_board(6, 7)
    new_board = place_piece('o', 0, 0, board)
    assert new_board[0][0] == 'o'


def test_check_winner_none():
    board = init_board(6,7)
    assert check_winner(board) == None


def test_check_winner_row_0():
    board = init_board(6,7)
    board[0] = ['.', '.', '.', 'x', 'x', 'x', 'x']
    assert check_winner(board) == 'x'

def test_check_winner_col_0():
    board = init_board(6, 7)
    board[0][0] = 'o'
    board[1][0] = 'o'
    board[2][0] = 'o'
    board[3][0] = 'o'
    assert check_winner(board) == 'o'

def test_check_winner_col_4_row_2():
    board = init_board(6, 7)
    board[1][4] = 'o'
    board[2][4] = 'o'
    board[3][4] = 'o'
    board[4][4] = 'o'
    assert check_winner(board) == 'o'


def test_check_winner_col_4_row_3():
    board = init_board(6, 7)
    board[2][4] = 'o'
    board[3][4] = 'o'
    board[4][4] = 'o'
    board[5][4] = 'o'
    assert check_winner(board) == 'o'

def test_check_winner_col_4_row_6_no_exception():
    board = init_board(6, 7)
    board[2][5] = 'o'
    assert check_winner(board) == None

def test_check_winner_diag_row_0():
    board = init_board(6, 7)
    board[0][0] = 'o'
    board[1][1] = 'o'
    board[2][2] = 'o'
    board[3][3] = 'o'
    assert check_winner(board) == 'o'


def test_check_winner_diag_row_1():
    board = init_board(6, 7)
    board[1][0] = 'x'
    board[2][1] = 'x'
    board[3][2] = 'x'
    board[4][3] = 'x'
    assert check_winner(board) == 'x'

def test_check_winner_diag_row_1_col_1():
    board = init_board(6, 7)
    board[1][1] = 'x'
    board[2][2] = 'x'
    board[3][3] = 'x'
    board[4][4] = 'x'
    assert check_winner(board) == 'x'

def test_check_winner_diag_row_1_col_0():
    board = init_board(6, 7)
    board[1][0] = 'o'
    board[2][1] = 'o'
    board[3][2] = 'o'
    board[4][3] = 'o'
    assert check_winner(board) == 'o'

def test_play():
    board = init_board(6, 7)
    play(board, 'o', 0, 0)
    play(board, 'x', 1, 0)
    play(board, 'o', 1, 1)
    play(board, 'x', 2, 0)
    play(board, 'o', 2, 2)
    play(board, 'x', 3, 0)
    winner = play(board, 'o', 3, 3)
    assert winner == 'o'