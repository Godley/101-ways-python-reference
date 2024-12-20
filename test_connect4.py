from connect4 import init_board, place_piece

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