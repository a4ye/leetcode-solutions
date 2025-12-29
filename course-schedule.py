class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for prereq in prerequisites:
            if prereq[0] in adj:
                adj[prereq[0]].append(prereq[1])
            else:
                adj[prereq[0]] = [prereq[1]]

        visited = {}
        def hasCycleDfs(node):
            if node not in adj:
                return False

            neighbours = adj[node]
            for n in neighbours:
                if n in visited and visited[n] == 0:
                    return True
                elif n not in visited:
                    visited[n] = 0
                    hasCycle = hasCycleDfs(n)
                    visited[n] = 1
                    if hasCycle:
                        return True

            visited[node] = 1
            return False

        for node in range(numCourses):
            if node not in visited:
                hasCycle = hasCycleDfs(node)
                if hasCycle:
                    return False

        return True
