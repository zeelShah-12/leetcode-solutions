class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                count += backtrack(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col})
            return count       
        return backtrack(0, set(), set(), set())