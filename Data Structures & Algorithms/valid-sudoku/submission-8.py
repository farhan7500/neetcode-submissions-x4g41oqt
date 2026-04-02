class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for column in range(9):
                num = board[row][column]
                if num in seen:
                    return False
                if num != '.':
                    seen.add(num)

        for column in range(9):
            seen = set()
            for row in range(9):
                num = board[row][column]
                if num in seen:
                    return False
                if num != '.':
                    seen.add(num)

        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    column = (box % 3) * 3 + j
                    num = board[row][column]
                    if num in seen:
                        return False
                    if num != '.':
                        seen.add(num)

        return True
