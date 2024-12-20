def init_board(rows: int, cols: int) -> list:
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append('.')
        board.append(row)
    return board


def place_piece(player: str, row: int, col: int, board: list):
    if row >= len(board):
        return
    if col >= len(board[row]):
        return
    if board[row][col] != '.':
        return
    board[row][col] = player
    return board


def display_board():
    pass


def main():
    session = init_board()



if __name__ == '__main__':
    main()