class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for column in range(9):
                if board[row][column] != '.':
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])


        for column in range(9):
            seen = set()
            for row in range(9):
                if board[row][column] != '.':
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])

        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    column = (box % 3) * 3 + j
                    if board[row][column] != '.':
                        if board[row][column] in seen:
                            return False
                        seen.add(board[row][column])

        return True


