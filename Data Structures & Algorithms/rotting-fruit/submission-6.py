class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        temp = deque()
        res = 0
        ff = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #loop, count fruit, if rotten put in q
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    ff +=1
                if grid[i][j] == 2:
                    q.append([i,j])
        #while q, bfs, if 0 return. if rotten fruit return. if fresh fruit, add to q and change fruit to rotten.
        def bfs(i,j):
            nonlocal ff
            if (i < 0 or j < 0 or
                i == ROWS or j == COLS or
                grid[i][j] == 0 or grid[i][j] == 2):
                return
            if grid[i][j] == 1:
                ff -= 1
            grid[i][j] = 2
            temp.append([i, j])
        while q:
            i,j = q.popleft()
            for dr,dc in directions:
                bfs(i+dr, j+dc)
            if not q and temp:
                res += 1
                q = temp
                temp = deque()
        return res if ff == 0 else -1


        #if no more q, return if fruits turned rotten = fresh fruit count

        