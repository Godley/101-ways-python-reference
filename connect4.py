from typing import Tuple

def init_board(rows: int, cols: int) -> list:
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append('.')
        board.append(row)
    return board


def place_piece(player: str, row: int, col: int, board: list) -> list:
    if row >= len(board):
        return None
    if col >= len(board[row]):
        return None
    if board[row][col] != '.':
        return None
    board[row][col] = player
    return board


def check_sequence(seq: list) -> str:
    result = "".join(seq).find("xxxx")
    if result == -1:
        o_result = "".join(seq).find("oooo")
        if o_result != -1:
            return 'o'
    else:
        return 'x'


def get_col_diag_indexes(row: list, row_index: int, grid_height: int, connect_length: int) -> Tuple[list, list]:
    row_str = "".join(row)
    first_x = row_str.find("x")
    first_o = row_str.find("o")
    print("row_id: {}, first_o: {}".format(row_index, first_o))
    row_indices_x = []
    row_indices_o = []
    diag_indices_x = []
    diag_indices_o = []
    if first_x != -1:
        stop = connect_length + row_index
        if stop <= grid_height:
            for i in range(connect_length):
                row_indices_x.append((i + row_index, first_x))

                col = first_x + i
                if col < len(row):
                    diag_indices_x.append((i + row_index, col))
    if first_o != -1:
        stop = connect_length + row_index
        if stop <= grid_height:
            for i in range(connect_length):
                row_indices_o.append((i + row_index, first_o))
                col = first_o + i
                if col < len(row):
                    diag_indices_o.append((i + row_index, col))
    return row_indices_x, row_indices_o, diag_indices_x, diag_indices_o


def check_col(board: list, row_index: int, connect_length: int) -> str:
    x_indices, o_indices, x_diag, o_diag = get_col_diag_indexes(board[row_index], row_index, len(board), connect_length)
    print(x_diag)
    word = []
    diag_word = []
    if len(x_indices) >= connect_length:
        for coord in x_indices:
            word.append(board[coord[0]][coord[1]])
    if len(o_indices) >= connect_length:
        for coord in o_indices:
            word.append(board[coord[0]][coord[1]])
    if len(x_diag) >= connect_length:
        for coord in x_diag:
            diag_word.append(board[coord[0]][coord[1]])
    if len(o_diag) >= connect_length:
        for coord in o_diag:
            diag_word.append(board[coord[0]][coord[1]])
    col = check_sequence(word)
    diag = check_sequence(diag_word)
    return col or diag

def check_winner(board: list) -> str:
    for i, row in enumerate(board):
        result = check_sequence(row)
        if result is not None:
            return result
        col_result = check_col(board, i, 4)
        if col_result is not None:
            return col_result


def play(board: list, player: str, row: int, col: int):
    updated = place_piece(player, row, col, board)
    winner = check_winner(updated)
    if winner:
        return winner

def display_board():
    pass


def main():
    session = init_board()



if __name__ == '__main__':
    main()