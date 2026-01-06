from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        has_path_to_pacific = set()
        has_path_to_atlantic = set()

        visited_pacific = [[False] * len(heights[0]) for _ in range(len(heights))]
        visited_atlantic = [[False] * len(heights[0]) for _ in range(len(heights))]

        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0])

        def canFlow(toR, toC, fromR, fromC):
            return heights[toR][toC] <= heights[fromR][fromC]

        for i in range(len(heights)):
            if not visited_pacific[i][0]:
                q = deque()
                q.append((i, 0))

                while len(q) != 0:
                    r, c = q.popleft()
                    has_path_to_pacific.add((r, c))

                    if valid(r - 1, c) and canFlow(r, c, r - 1, c) and not visited_pacific[r - 1][c]:
                        q.append((r - 1, c))
                        visited_pacific[r - 1][c] = True
                    if valid(r + 1, c) and canFlow(r, c, r + 1, c) and not visited_pacific[r + 1][c]:
                        q.append((r + 1, c))
                        visited_pacific[r + 1][c] = True
                    if valid(r, c - 1) and canFlow(r, c, r, c - 1) and not visited_pacific[r][c - 1]:
                        q.append((r, c - 1))
                        visited_pacific[r][c - 1] = True
                    if valid(r, c + 1) and canFlow(r, c, r, c + 1) and not visited_pacific[r][c + 1]:
                        q.append((r, c + 1))
                        visited_pacific[r][c + 1] = True

            if not visited_atlantic[i][len(heights[0]) - 1]:
                q = deque()
                q.append((i, len(heights[0]) - 1))

                while len(q) != 0:
                    r, c = q.popleft()
                    has_path_to_atlantic.add((r, c))

                    if valid(r - 1, c) and canFlow(r, c, r - 1, c) and not visited_atlantic[r - 1][c]:
                        q.append((r - 1, c))
                        visited_atlantic[r - 1][c] = True
                    if valid(r + 1, c) and canFlow(r, c, r + 1, c) and not visited_atlantic[r + 1][c]:
                        q.append((r + 1, c))
                        visited_atlantic[r + 1][c] = True
                    if valid(r, c - 1) and canFlow(r, c, r, c - 1) and not visited_atlantic[r][c - 1]:
                        q.append((r, c - 1))
                        visited_atlantic[r][c - 1] = True
                    if valid(r, c + 1) and canFlow(r, c, r, c + 1) and not visited_atlantic[r][c + 1]:
                        q.append((r, c + 1))
                        visited_atlantic[r][c + 1] = True


        for i in range(len(heights[0])):
            if not visited_pacific[0][i]:
                q = deque()
                q.append((0, i))

                while len(q) != 0:
                    r, c = q.popleft()
                    has_path_to_pacific.add((r, c))

                    if valid(r - 1, c) and canFlow(r, c, r - 1, c) and not visited_pacific[r - 1][c]:
                        q.append((r - 1, c))
                        visited_pacific[r - 1][c] = True
                    if valid(r + 1, c) and canFlow(r, c, r + 1, c) and not visited_pacific[r + 1][c]:
                        q.append((r + 1, c))
                        visited_pacific[r + 1][c] = True
                    if valid(r, c - 1) and canFlow(r, c, r, c - 1) and not visited_pacific[r][c - 1]:
                        q.append((r, c - 1))
                        visited_pacific[r][c - 1] = True
                    if valid(r, c + 1) and canFlow(r, c, r, c + 1) and not visited_pacific[r][c + 1]:
                        q.append((r, c + 1))
                        visited_pacific[r][c + 1] = True

            if not visited_atlantic[len(heights) - 1][i]:
                q = deque()
                q.append((len(heights) - 1, i))

                while len(q) != 0:
                    r, c = q.popleft()
                    has_path_to_atlantic.add((r, c))

                    if valid(r - 1, c) and canFlow(r, c, r - 1, c) and not visited_atlantic[r - 1][c]:
                        q.append((r - 1, c))
                        visited_atlantic[r - 1][c] = True
                    if valid(r + 1, c) and canFlow(r, c, r + 1, c) and not visited_atlantic[r + 1][c]:
                        q.append((r + 1, c))
                        visited_atlantic[r + 1][c] = True
                    if valid(r, c - 1) and canFlow(r, c, r, c - 1) and not visited_atlantic[r][c - 1]:
                        q.append((r, c - 1))
                        visited_atlantic[r][c - 1] = True
                    if valid(r, c + 1) and canFlow(r, c, r, c + 1) and not visited_atlantic[r][c + 1]:
                        q.append((r, c + 1))
                        visited_atlantic[r][c + 1] = True

        return list(has_path_to_atlantic.intersection(has_path_to_pacific))
