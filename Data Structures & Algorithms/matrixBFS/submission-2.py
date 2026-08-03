from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][columns-1] == 1:
            return -1

        queue = deque()
        visit = set()

        visit.add((0, 0))
        queue.append((0, 0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == columns - 1:
                    return length
                
                neighbours = [
                    [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0]
                ]

                for dr, dc in neighbours:
                    row = r + dr
                    column = c + dc
                    if min(row, column) < 0 or row == rows or column == columns or (row, column) in visit or grid[row][column] == 1:
                        continue
                    visit.add((row, column))
                    queue.append((row, column))
            length += 1
        return -1
        