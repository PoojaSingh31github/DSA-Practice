def is_safe(board, row, col, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N):
    if attacked_rows[row] or attacked_cols[col] or attacked_diag1[row - col] or attacked_diag2[row + col]:
        return False
    return True

def place_queens(board, row, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N):
    if row == N:
        return 0

    max_queens = 0
    for col in range(N):
        if board[row][col] == '.' and is_safe(board, row, col, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N):
            attacked_rows[row] = True
            attacked_cols[col] = True
            attacked_diag1[row - col] = True
            attacked_diag2[row + col] = True

            max_queens = max(max_queens, 1 + place_queens(board, row + 1, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N))

            attacked_rows[row] = False
            attacked_cols[col] = False
            attacked_diag1[row - col] = False
            attacked_diag2[row + col] = False

    max_queens = max(max_queens, place_queens(board, row + 1, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N))
    
    return max_queens

def max_queens_on_board(board, N):
    attacked_rows = [False] * N
    attacked_cols = [False] * N
    attacked_diag1 = [False] * (2 * N - 1) 
    attacked_diag2 = [False] * (2 * N - 1) 

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'Q':
                attacked_rows[i] = True
                attacked_cols[j] = True
                attacked_diag1[i - j] = True
                attacked_diag2[i + j] = True

    return place_queens(board, 0, attacked_rows, attacked_cols, attacked_diag1, attacked_diag2, N)

N = int(input())
board = [input().strip() for _ in range(N)]

print(max_queens_on_board(board, N))
