class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack():
            def isSafe():
                for j in range(9):
                    if board[r][j] ==val:
                        return False
                for i in range(9):
                    if board[i][c] == val:
                        return False
                box_row = (r //3)*3
                box_col = (c //3)*3
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        if board[row][col] == val:
                            return False
                return True            

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for val in map(str, range(1,10)):
                            if isSafe():
                                board[r][c] = val
                                if backtrack():
                                    return True
                                else:
                                    board[r][c]="."
                        return False
            return True
        backtrack()
solution = Solution()
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solution.solveSudoku(sudoku_board)

# Print the solved Sudoku board
for row in sudoku_board:
    print(row)
