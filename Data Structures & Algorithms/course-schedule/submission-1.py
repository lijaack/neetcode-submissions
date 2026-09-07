class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree[i] = how many prerequisites course i still has
        indegree = [0] * numCourses

        # adj[i] = courses that become available after finishing course i
        adj = [[] for i in range(numCourses)]

        # [src, dst] means: dst must be taken before src
        # So we create an edge: dst → src
        for src, dst in prerequisites:
            indegree[src] += 1
            adj[dst].append(src)

        # Courses with 0 prerequisites can be taken immediately
        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # Count how many courses we successfully finish
        finish = 0

        while q:
            # Take a course that currently has no prerequisites
            node = q.popleft()
            finish += 1

            # "Remove" this course from the graph.
            # Every course depending on it loses one prerequisite.
            for nei in adj[node]:
                indegree[nei] -= 1

                # If this was the last prerequisite,
                # that course is now available to take.
                if indegree[nei] == 0:
                    q.append(nei)

        # If we finished every course, there was no cycle.
        # If some courses remain, they are stuck in a dependency cycle.
        return finish == numCourses
