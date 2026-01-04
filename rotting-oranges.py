from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        q = deque()

        # If everything is already rotten return 0
        has_fresh = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell == 1:
                    has_fresh = True
                elif cell == 2:
                    q.append((row, col))

        if not has_fresh:
            return 0

        # Make rotting spread
        while len(q) != 0:
            rotted = False
            lenQ = len(q)
            for i in range(lenQ):
                row, col = q.popleft()

                # Left
                if col > 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    q.append((row, col - 1))
                    rotted = True

                # Right
                if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    q.append((row, col + 1))
                    rotted = True

                # Up
                if row > 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    q.append((row - 1, col))
                    rotted = True

                # Down
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    q.append((row + 1, col))
                    rotted = True

            if rotted:
                minutes += 1


        # If not all the oranges can rot, return -1:
        has_fresh = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell == 1:
                    has_fresh = True
                    break

            if has_fresh:
                break

        if has_fresh:
            return -1
        
        return minutes
