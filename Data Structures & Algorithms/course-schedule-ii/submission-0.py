class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_left = [0] * numCourses

        after = [[] for _ in range(numCourses)]

        for c,p in prerequisites:
            prereq_left[c] += 1
            after[p].append(c)

        q = deque()

        for i in range(len(prereq_left)):
            if prereq_left[i] == 0:
                q.append(i)
        takened = []
        while q:
            course = q.popleft()
            takened.append(course)

            for a in after[course]:
                prereq_left[a] -= 1

                if prereq_left[a] == 0:
                    q.append(a)
        return takened if len(takened) == numCourses else []