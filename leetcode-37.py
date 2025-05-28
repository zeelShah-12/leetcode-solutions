class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Initialize sets and store empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3) * 3 + (c//3)].add(num)
        
        def backtrack(idx):
            if idx == len(empty_cells):  # If all empty cells are filled, sudoku is solved
                return True
            
            r, c = empty_cells[idx]
            box_idx = (r//3) * 3 + (c//3)
            
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    if backtrack(idx + 1):  # Move to the next empty cell
                        return True
                    
                    # Undo the placement (backtrack)
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            
            return False  # No valid number found, backtrack
        
        backtrack(0)