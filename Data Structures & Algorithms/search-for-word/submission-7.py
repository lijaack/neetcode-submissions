class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        res=False
        def dfs(c,i,j):
            if (i,j) in visited:
                return False
            else:
                visited.add((i,j))
            if c == len(word)-1 and board[i][j] == word[c] :
                return True
            n,s,e,w = False,False,False,False
            if board[i][j] == word[c]:
                if i+1 < len(board):
                    n=dfs(c+1,i+1,j) 
                if i-1 >= 0: 
                    s=dfs(c+1,i-1,j)
                if j+1 < len(board[i]):
                    e=dfs(c+1,i,j+1)
                if j-1 >= 0:
                    w=dfs(c+1,i,j-1)
            visited.remove((i,j))
            return n or s or e or w

            



        for i in range(len(board)):
            for j in range(len(board[i])):

                if dfs(0, i, j):
                    res=True
                    break
        return res