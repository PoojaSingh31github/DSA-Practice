def nQueen(n):

    def backtrack(row, cols, dia, anti_dia):
        if row == n:
            sol.append(["".join(row) for row in board])
            return 
        for col in range(n):
            cur_dia = row - col
            curr_anti_dia = row + col
            if col in cols or cur_dia in dia or curr_anti_dia in anti_dia:
                continue
            board[row][col] = "Q"
            cols.add(col)
            dia.add(cur_dia)
            anti_dia.add(curr_anti_dia)
            backtrack(row+1 , cols, dia, anti_dia )
            board[row][col]="."
            cols.remove(col)
            dia.remove(cur_dia)
            anti_dia.remove(curr_anti_dia)


    sol =[]
    board = [["."] * n for _ in range(n)]
    backtrack(0, set(),set(),set())
    return sol


n=4
ans = nQueen(n)
print(ans)
































# def solveNQueens(n):
#     def backtrack(row, diagonals, anti_diagonals, cols, board, solutions):
#         # If we've placed queens on all rows, we have a solution
#         if row == n:
#             solutions.append(["".join(row) for row in board])
#             return

#         for col in range(n):
#             # Calculate diagonal and anti-diagonal indexes
#             curr_diag = row - col
#             curr_anti_diag = row + col

#             # Check if placing queen here is valid
#             if col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals:
#                 continue

#             # Place the queen
#             board[row][col] = 'Q'
#             cols.add(col)
#             diagonals.add(curr_diag)
#             anti_diagonals.add(curr_anti_diag)

#             # Move to the next row
#             backtrack(row + 1, diagonals, anti_diagonals, cols, board, solutions)

#             # Backtrack: remove the queen and reset the state
#             board[row][col] = '.'
#             cols.remove(col)
#             diagonals.remove(curr_diag)
#             anti_diagonals.remove(curr_anti_diag)

#     # Initialize the board and result container
#     n
#     solutions = []
#     board = [["."] * n for _ in range(n)]
#     backtrack(0, set(), set(), set(), board, solutions)

#     print(solutions)

# n=4
# ans = solveNQueens(n)    
