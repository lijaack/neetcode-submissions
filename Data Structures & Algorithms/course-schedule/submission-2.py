class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites_left[i] = how many prerequisites course i has
        prerequisites_left = [0] * numCourses

        # after[i] = courses that depend on course i
        after = [[] for _ in range(numCourses)]

        # [course, prerequisite]
        # We need to take prerequisite BEFORE course.
        for course, prerequisite in prerequisites:
            prerequisites_left[course] += 1
            after[prerequisite].append(course)

        # Start with courses that have no prerequisites
        q = deque()

        for course in range(numCourses):
            if prerequisites_left[course] == 0:
                q.append(course)

        # Number of courses we successfully take
        taken = 0

        while q:
            # Take a course that has no prerequisites left
            course = q.popleft()
            taken += 1

            # Taking this course satisfies one prerequisite
            # for every course that depends on it.
            for next_course in after[course]:
                prerequisites_left[next_course] -= 1

                # All prerequisites are now satisfied,
                # so we can take this course next.
                if prerequisites_left[next_course] == 0:
                    q.append(next_course)

        # If we took every course, there was no cycle.
        return taken == numCourses
