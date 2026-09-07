class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_left = [0] * numCourses

        after = [[] for _ in range(numCourses)]

        for c,p in prerequisites:
            prereq_left[c] += 1
            after[p].append(c)

        q = deque()

        for i in range(len(prereq_left)):
            if prereq_left[i] == 0:
                q.append(i)
        takened = 0
        while q:
            course = q.popleft()
            takened+=1

            for a in after[course]:
                prereq_left[a] -= 1

                if prereq_left[a] == 0:
                    q.append(a)
        return takened == numCourses

        