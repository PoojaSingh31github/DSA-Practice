def solveNQueens(n):
    def backtrack(row, cols, posDiags, negDiags):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            posDiag = row + col
            negDiag = row - col
            if col in cols or posDiag in posDiags or negDiag in negDiags:
                continue
            cols.add(col)
            posDiags.add(posDiag)
            negDiags.add(negDiag)
            count += backtrack(row + 1, cols, posDiags, negDiags)
            cols.remove(col)
            posDiags.remove(posDiag)
            negDiags.remove(negDiag)
        return count

    return backtrack(0, set(), set(), set())

n = int(input())
print(solveNQueens(n))
